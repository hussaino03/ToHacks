from django import forms
from .models import *
  
class ConvertForm(forms.ModelForm):
  
    class Meta:
        model = Convert
        fields = ['name', 'convert_Main_Img']