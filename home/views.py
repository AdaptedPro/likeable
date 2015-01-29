from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from home.forms import UploadFileForm
from home.myAscii import myAscii
from home.myCouch import myCouch
import PIL.Image as Image

dbname   = 'user_images'
dbserver = 'http://127.0.0.1:5984/'
# dbserver = 'https://adaptedpro.iriscouch.com/user_images/'
  
@csrf_exempt
def index(request):
    request.upload_handlers.pop(0)    
    return _index(request)
   
@csrf_protect    
def _index(request):
    message       = 'ASCII me anything'
    form_status   = False
    hash          = ''
    ascii_data    = ''
    converted     = ''
    
    #Process Form
    if request.method == 'POST':
        imageFile        = request.FILES['starterImage']
        path             = imageFile.temporary_file_path()
        ascii            = myAscii()
        ascii.image_path = path   
        ascii_data       = ascii.convert()
        form_status = True 
#         SAVE DOCUMENT IN COUCH
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():  
#             couch              = myCouch()
#             couch.dbname       = dbname
#             couch.COUCH_SERVER = dbserver
#             if couch.select_db():
#                 couch.post_payload = { 'title':form.cleaned_data['imageName'] }
#                 if couch.insert_doc():
#                     imageFile      = request.FILES['starterImage']
#                     path           = imageFile.temporary_file_path()                 
#                     couch.filename = path 
#                     if couch.put_doc_attachment():
#                         img_url = couch.get_doc_image_by_id()
#                         hash    = couch.id
#                         if img_url != False:
#                             form_status = True
#                     else:
#                         message = "Couldn't add image"
#                 else:
#                     message = "Couldn't create doc!"
#             else:
#                 message = "Can't select the database"
        
    context = RequestContext(request, {
        'message': message,
        'ascii_data': ascii_data,
        'form_status': form_status,
    })
    template = loader.get_template('home/index.html')    
    return HttpResponse(template.render(context))

def download(request,doc_id):
    message            = 'test'
#     couch              = myCouch()
#     couch.dbname       = dbname
#     couch.COUCH_SERVER = dbserver
#     couch.id           = doc_id
#     img_url            = couch.get_doc_image_by_id()
#     ascii              = myAscii()
#     ascii.image_page   = img_url    
#     ascii_result       = ascii.convert()    
    context = RequestContext(request, {
        'message': message,
    })    
    template = loader.get_template('home/converted.html')    
    return HttpResponse(template.render(context))
        