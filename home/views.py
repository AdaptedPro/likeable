from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.utils import timezone
from django.views import generic
    
class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = ''
    
    def get_queryset(self):
        test = 'hello'
        return test