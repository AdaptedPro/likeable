from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from songzgalore.myCouchDB import myCouchDB

# dbname   = 'million_song_db'
# dbserver = 'http://127.0.0.1:5984/'

def index(request):
    message       = 'Hello Wolrd 2'