from xml.parsers.expat import model
from django import forms
from django.forms import ModelForm
from .models import Kitob



# yangi kitob kiritish
class KitobForm(ModelForm):
    class Meta:
        model = Kitob
        fields = ('formulyar_raqami','foy', 'tel_raqami', 'pasport_seryasi', 'pasport_raqami')
        labels = {
            'formulyar_raqami':'',
            'foy':'Your name',
            'tel_raqami':'',
            'pasport_seryasi':'',
            'pasport_raqami':'',
            # 'sana':'',
        }
        widgets = {
            'formulyar_raqami': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Formulyar Raqami"}),
            'foy': forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'tel_raqami': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Telefon Raqami"}),
            'pasport_seryasi': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Passwd Seriyasi"}),
            'pasport_raqami': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Paswd Raqami"}),
            # 'sana': forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
        }
