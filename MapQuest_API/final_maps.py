################################
#finalmaps.py API URL interactions
#
#
#author:Brian Porter
#
#
#
#05/11/2018 BP initial version
#################################
import urllib.request
import urllib.error
import urllib.parse
import json

APP_KEY = 'vu0UahkLcKVemd7cuA5Zu1PgvzVHscGs'
URL = 'http://open.mapquestapi.com/directions/v2/route?key={}&'.format(APP_KEY)

def format_url(start_loc:str, end_loc:str)->str:
    query_parameters = [('from', start_loc), ('to', end_loc)]
    url_encode = urllib.parse.urlencode(query_parameters)
    return (URL + url_encode)
def get_result(url:str)->'json':
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))
        print()
    finally:
        if response != None:
             response.close()
def parse_steps(json_result:'json')->list:
    result =[]
    step_list = json_result['route']['legs']
    for i in step_list:
        for j in i['maneuvers']:
            result.append(j['narrative'])
        return result
def parse_distance(json_result:'json')->list:
    result = json_result['route']['distance']
    return [result]
def parse_time(json_result:'json')->list:
    seconds = json_result['route']['time']
    return [seconds]
def map_direction(parameter:str, n:float)->str:
    if parameter == 'lat':
        if n <= 90:
            return '{0:.2f}N'.format(n)
        return '{0:.2f}S'.format(n)
    elif parameter == 'long':
        if n <= 90:
            return '{0:.2f}E'.format(n)
        return '{0:.2f}W'.format(n)
def parse_latlong(json_result:'json')->list:
    result = []
    coord = json_result['route']['boundingBox']
    start_lat = abs(coord['ul']['lat'])
    start_long = abs(coord['ul']['lng'])
    result.append((map_direction('lat', start_lat), map_direction('long', start_long)))
    end_lat = abs(coord['lr']['lat'])
    end_long = abs(coord['lr']['lng'])
    result.append((map_direction('lat', end_lat), map_direction('long', end_long)))
    return result








