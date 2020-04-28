from cachetools import TTLCache
import requests
from django.conf import settings
import json

cache = TTLCache(maxsize=1, ttl=0)


def get_token():
    global cache
    try:
        return cache['token']
    except:
        data = {
            'client_id': settings.EMSI_CLIENT_ID,
            'client_secret': settings.EMSI_SECRET,
            'grant_type': 'client_credentials',
            'scope': settings.EMSI_SCOPE
        }
        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = requests.post('https://auth.emsicloud.com/connect/token',
                                 data=data, headers=headers).json()
        cache = TTLCache(maxsize=1, ttl=response['expires_in'])
        cache['token'] = response['access_token']
        return cache['token']


def get_keywords(text):
    headers = {
        'authorization': f'Bearer {get_token()}',
        'content-type': 'application/json'
    }
    response = requests.post(
        'https://skills.emsicloud.com/versions/latest/extract?trace=true',
        data=json.dumps({'full_text': text}), headers=headers).json()

    keywords = map(lambda x: {
        'value': x['surfaceForm']['value'],
        'skill': x['classificationData']['skills'][0]['skill']['name']
    }, response['trace'])

    duplicate_removed = []
    marker = set()
    for keyword in keywords:
        if keyword['skill'] not in marker:
            marker.add(keyword['skill'])
            duplicate_removed.append(keyword)

    return list(duplicate_removed)
