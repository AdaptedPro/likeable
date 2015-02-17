import json
import requests

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect

beats_key = '2qjvsuz97553nfacsmfraenx'
  
def index(request):
    end_point       = 'tracks'
    activities_list = beats_request_and_response(end_point);
    message         = ''
    
    # Build list on popular songs
    str = "<ul>"
    if 'data' in activities_list:
        total = activities_list['info']['count']
        s     = 's' if (total > 1) else ''
        for i in activities_list['data']:
            if i['type'] == 'track':
                str += "<li trkid='"+i['id']+"'>" + i['artist_display_name'] + '<br />' + i['title']+ "</li>"
    str += "</ul>"   
    context = RequestContext(request, {
        'message':str,
    })
    
    template = loader.get_template('beats/index.html')    
    return HttpResponse(template.render(context))
  

def beats_request_and_response(end_point):
    beats_request  = requests.get('https://partner.api.beatsmusic.com/v1/api/'+end_point+'?client_id='+beats_key)
    beats_response = beats_request.json();
    return beats_response    
    