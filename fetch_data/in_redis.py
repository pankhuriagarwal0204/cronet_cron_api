"""
The initialisation of the data needed by the apis
currently has morcha data which is the place where intrusion happens
"""
import redis
import time
#redis config
# db 1 denotes persistent cache
config = {'host':'localhost','db':1}
conn = redis.Redis(**config)

morcha_status = [
    {
        "uuid": "8d2b5e48-d33f-456f-bd18-138b475dab1f",
        "data": {
            "repr": "KV-101s-ce01",
            "location_name": "Malabela",
            "latitude": "33.884097379274905",
            "longitude": "74.23187255859376",
            "last_updated": time.time(),
            "uuid": "8d2b5e48-d33f-456f-bd18-138b475dab1f"
        }
    },
    {
        "uuid": "3c72a975-6863-429d-9de1-5aedf9b12af3",
        "data": {
            "repr": "KV-101s-ce02",
            "location_name": "Malabela",
            "latitude": "33.884097379274905",
            "longitude": "74.23187255859376",
            "last_updated": time.time(),
            "uuid": "3c72a975-6863-429d-9de1-5aedf9b12af3",
        }
    },
    {
        "uuid": "880a7be7-76a2-41d8-a6fc-d88a1671701c",
        "data": {
            "repr": "KV-101s-ce03",
            "location_name": "Malabela",
            "latitude": "34.73709847578162",
            "longitude": " 74.21813964843751",
            "last_updated": time.time(),
            "uuid": "880a7be7-76a2-41d8-a6fc-d88a1671701c",
        }
    },
    {
        "uuid": "c86128fb-16ac-4a26-81a2-ab912ee5c7b2",
        "data": {
            "repr": "KV-101s-ce04",
            "location_name": "Malabela",
            "latitude": "34.73709847578162",
            "longitude": " 74.21813964843751",
            "last_updated": time.time(),
            "uuid": "c86128fb-16ac-4a26-81a2-ab912ee5c7b2"
        }
    },
    {
        "uuid": "8dee87b7-9f45-4adc-850c-5d8cc9747f4f",
        "data": {
            "repr": "KV-101s-ce05",
            "location_name": "Malabela",
            "latitude": "33.884097379274905",
            "longitude": "74.23187255859376",
            "last_updated": time.time(),
            "uuid": "8dee87b7-9f45-4adc-850c-5d8cc9747f4f"

        }
    }
]

for morcha in morcha_status:
    print morcha['uuid']
    print morcha['data']
    conn.hmset(morcha['uuid'], morcha['data'])
    conn.sadd("morcha_uuid", morcha['uuid'])
