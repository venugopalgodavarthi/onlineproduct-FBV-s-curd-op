from django import forms
from product.models import Productdb
from django.core.files.storage import FileSystemStorage

class Productform(forms.ModelForm):
    class Meta:
        model=Productdb
        fields='__all__'

'''
class Productform(forms.Form):
    pname=forms.CharField()
    pdesc=forms.CharField()
    pprice=forms.FloatField()
    pdiscount=forms.FloatField()
    pimg=forms.ImageField()
''' 