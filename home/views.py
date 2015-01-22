from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from home.forms import UploadFileForm

def index(request):
    template = loader.get_template('home/index.html')
    message = 'Convert Your Image to ASCII'
    form_message = ''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            form_message += 'so good'
#     else:
#         form = UploadFileForm()
#     return render_to_response('home/uploaded.html', {'form': form})    

    context = RequestContext(request, {
        'title':'What Fun',
        'message': message,
        'upload_message' : request.method,
        'form_message' : form_message
    })
    return HttpResponse(template.render(context)) 