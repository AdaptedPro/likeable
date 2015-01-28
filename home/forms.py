from django import forms

class UploadFileForm(forms.Form):
#     imageName = forms.CharField(max_length=50)
    starterImage = forms.ImageField()