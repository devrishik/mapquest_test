import requests
import json

from django.conf import settings

from geoposition import Geoposition


def get_geolocation(sender, instance, **kwargs):
    """
    A signal for hooking up automatic ``Geo Position`` creation.
    Takes the 1st result of the response from MapQuest
    """
    if instance.position == Geoposition(1,2):
        url = settings.MAPQUEST_BASE_URL
        address = instance.address
        location = ''
        
        if address.street:
        	location = location + ', ' + address.street    
        if address.city:
        	location = location + ', ' + address.city    
        if address.state:
        	location = location + ', ' + address.state    
        if address.country:
        	location = location + ', ' + address.country

        payload = {
        	'location': location
        }

        resp = requests.get(url, params=payload)
        reponse = json.loads(resp.content)
        latitude = reponse['results'][0]['locations'][0]['latLng']['lat']
        longitude = reponse['results'][0]['locations'][0]['latLng']['lng']
        instance.position.latitude = latitude
        instance.position.longitude = longitude
        instance.save()
        return requests.get(url, params=payload)
    return 'done'
