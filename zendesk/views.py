from django.shortcuts import render

from django.http import HttpResponse


# Zenpy accepts an API token
creds = {
        'email' : 'jniravel@truu.ai',
        'token' : 'F67aiJQK17TEgVxEr8t0eSQPrbgAF5sbwhDObmc9',
        'subdomain': 'truu1662144512'
}

# Import the Zenpy Class
from zenpy import Zenpy



def index(request):
    zenpy_client = Zenpy(**creds)
    print(zenpy_client.__dict__)
    #for imp in zenpy_client.get_cache_names():
        #print(zenpy_client.get_cache_impl_name(imp))
        #print(zenpy_client.get_cache_max(imp))

    results = zenpy_client.search(type='ticket')
    #for ticket in zenpy_client.search_export(type='ticket'):
        #print(ticket.to_json())
    return HttpResponse(zenpy_client.__dict__)

