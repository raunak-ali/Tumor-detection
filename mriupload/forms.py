from django import forms
from .models import POST 

class ImageForm(forms.ModelForm):
    class Meta:
        model=POST
        fields=["MRI_IMAGE",]
