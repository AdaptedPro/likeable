from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import PIL.Image as Image
from home.forms import UploadFileForm
from home.myCouch import myCouch

#https://adaptedpro.iriscouch.com/user_images/
#http://127.0.0.1:5984/_utils/
  
@csrf_exempt
def index(request):
    request.upload_handlers.pop(0)    
    return _index(request)
   
@csrf_protect    
def _index(request):
    template    = loader.get_template('home/index.html')
    message     = 'Convert Your Image to ASCII'
    form_status = False
    img_url     = ''
    #Process Form
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():              
            couch = myCouch()
            couch.dbname = 'user_images'
            couch.COUCH_SERVER = 'http://127.0.0.1:5984/'
            if couch.select_db():
                couch.post_payload = { 'title':form.cleaned_data['imageName'] }
                if couch.insert_doc():
                    imageFile      = request.FILES['starterImage']
                    path           = imageFile.temporary_file_path()
                    couch.filename = path 
                    if couch.put_doc_attachment():
                        message = 'Image Uploaded!'
                        img_url = couch.get_doc_image_by_id()
                        if img_url != False:
                            form_status = True
                    else:
                        message = "Couldn't add image"
                else:
                    message = "Couldn't create doc!"
            else:
                message = "Can't select the database"         

    context = RequestContext(request, {
        'message': message,
        'img': img_url,
        'form_status': form_status,
    })
    return HttpResponse(template.render(context))

def convert(request):
    template    = loader.get_template('home/converted.html')
    return HttpResponse(template.render(context))    