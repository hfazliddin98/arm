from xml.parsers.expat import model
from django import forms
from django.forms import ModelForm
from .models import Talaba_kitob



# yangi kitob kiritish
class Talaba_kitobForm(ModelForm):
    class Meta:
        model = Talaba_kitob
        fields = (
            'invertor',
            'kitob',
            'familya',
            'ism',
            'sharifi',
        )
        labels = {
            'invertor':'Invertor nomer',
            'kitob':'Kitob nomi',
            'familya':'Familiya',
            'ism':'Ism',
            'sharifi':'Sharif',
        }
        widgets = {
            'invertor': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Invertor nomer"}),
            'kitob': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Kitob nomi"}),
            'familya': forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'ism': forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'sharifi': forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
        }
