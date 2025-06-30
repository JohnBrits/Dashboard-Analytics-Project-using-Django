from django import forms
from .models import DataUpload

class DataUploadForm(forms.ModelForm):
    class Meta:
        model = DataUpload
        fields = ['file']
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()