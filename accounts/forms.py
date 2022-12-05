from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Foydalanuvchi
from django import forms

# foydalanuvchi  ro`yhatdan o`tishda kiritishi kerak qatarlar
class FoydalanuvchiCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Foydalanuvchi
        fields = (  
            'username',          
            'familiya_a',
            'ism_a',
            'arm_bolim',
            'email',
            'tel_nomer',
            'lavozimi',
            'viloyat_a',
            'shahar_tuman',
            'kocha',
            'uy_nomeri',
            'rasm'
        )
        labels = {
            'username':'Foydalanuvchi nomi',
            'familiya_a':'Familiya',
            'ism_a':'Ism',
            'arm_bolim':'ARM bo`lim',
            'email':'Email',
            'tel_nomer':'Telefon nomer',
            'lavozimi':'Lavozimi',
            'viloyat_a':'Viloyat',
            'shahar_tuman':'Shahar Tuman',
            'kocha':'Ko`cha',
            'uy_nomeri':'Uy nomer',
            
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi nomi"}),
            'familiya_a': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Familiya"}),
            'ism_a': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Ism"}),
            'arm_bolim': forms.Select(attrs={'class':'form-control', 'placeholder':"Arm bolim"}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Email"}),
            'tel_nomer': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Telefon nomer"}),
            'lavozimi': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Lavozimi"}),
            'viloyat_a': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Viloyat"}),
            'shahar_tuman': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Shahar Tuman"}),
            'kocha': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Ko`cha"}),
            'uy_nomeri': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Uy nomiri"}),
           
           
        }

# foydalanuvchi malumotlarini o'zgartirish huquqi
class FoydalanuvchiChangeForm(UserChangeForm):
    class Meta:
        model = Foydalanuvchi
        fields = ('arm_bolim', 'lavozimi', 'email', 'tel_nomer')
