from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from home.models import Image

class ImageModelFormPreview(FormPreview):

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponseRedirect('/form/success')