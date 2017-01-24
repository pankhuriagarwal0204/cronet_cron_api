import time
from django.http import JsonResponse
from django.conf import settings
from django.core.cache import caches
import redis
import pickle

#use redis connection config from settings.py
conn = redis.Redis(**settings.REDIS_CONN_SETTINGS)

#list complete morcha data from redis
def fetchMorchas(request):
    morcha_status = []
    #morcha_ids contains list of all the uuids of morcha
    morcha_ids = conn.smembers('morcha_uuid')
    morcha_ids = list(morcha_ids)

    for morcha in morcha_ids:

        #retrieve the detail of the morcha
        morcha_data = conn.hgetall(morcha)

        # if intrusion has happened on morcha
        if "intrusion" in morcha_data:
            #intrsuion_id refers to key of intrusion associated with the morcha
            intrusion_id = morcha_data['intrusion']
            intrusion_info = conn.hgetall(intrusion_id)
            #set intrusion info to data fetched from intrusion table
            morcha_data['intrusion'] = intrusion_info
        morcha_status.append(morcha_data)
    return JsonResponse(morcha_status, safe=False)

#returns details of a single morcha
def fetchIntrudedMorchaDetails(request, morcha_id):
    morcha_data = conn.hgetall(morcha_id)
    if morcha_data.has_key("intrusion"):
        intrusion_id = morcha_data['intrusion']
        intrusion_info = conn.hgetall(intrusion_id)
        morcha_data['intrusion'] = intrusion_info
    return JsonResponse(morcha_data, safe=False)

#testing cache
def test(request):
    cache_persistent = caches['persistent']
    mock_data = {
        "1": {
            "data": {
                "repr": "KV-101s-ce01",
                "location_name": "Malabela",
                "latitude": "33.884097379274905",
                "longitude": "74.23187255859376",
                "last_updated": time.time(),
                "uuid": "1",
                "intrusion": {"detected": {"time": "ass"}}
            }
        },
        "2": {
            "data": {
                "repr": "KV-101s-ce01",
                "location_name": "Malabela",
                "latitude": "33.884097379274905",
                "longitude": "74.23187255859376",
                "last_updated": time.time(),
                "uuid": "2",
                "intrusion": {"detected": {"time": "ass"}}
            }
        },
        "3": {
            "data": {
                "repr": "KV-101s-ce01",
                "location_name": "Malabela",
                "latitude": "33.884097379274905",
                "longitude": "74.23187255859376",
                "last_updated": time.time(),
                "uuid": "3",
                "intrusion": {"detected": {"time": "ass"}}
            }
        }
    }
    cache_persistent.set_many(mock_data)
    mock_ids = ["1", "2", "3"]
    mock_morcha_ids = ['8dee87b7-9f45-4adc-850c-5d8cc9747f4f',
                       '8d2b5e48-d33f-456f-bd18-138b475dab1f',
                       '3c72a975-6863-429d-9de1-5aedf9b12af3',
                       '880a7be7-76a2-41d8-a6fc-d88a1671701c',
                       'c86128fb-16ac-4a26-81a2-ab912ee5c7b2']

    id = "8dee87b7-9f45-4adc-850c-5d8cc9747f4f"
    conn.set(':1:key',pickle.dumps({'value':1, 'data':
        {
            'case' : 2
        }}))
    a= cache_persistent.get('key')
    print a
    return JsonResponse(a, safe=False)
