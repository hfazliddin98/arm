from django import forms
from django.forms import ModelForm
from .models import ArmAdmin



# yangi kitob kiritish
class Arm_adminForm(ModelForm):
    class Meta:
        model = ArmAdmin
        fields = (
            'familiya_arm',
            'ism',
            'arm_bolim',
            'viloyat',
            'shahar_tuman',
            'kocha',
            'uy_nomeri',
            'lavozimi',
            'tel_nomer',
            'rasm',
        )
        labels = {
            'familiya_arm': 'Familiya',
            'ism': 'Ism',
            'arm_bolim': 'ARM bo`lim',
            'viloyat': 'Viloyat',
            'shahar_tuman': 'Shahar tuman',
            'kocha': 'Ko`cha',
            'uy_nomeri': 'Uy nomeri',
            'lavozimi' : 'Lavozimi',
            'tel_nomer' : 'Telefon nomer',
            'rasm': 'Rasm',
        }
        widgets = {
           
            'familiya_arm' : forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'ism' : forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'arm_bolim' : forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'viloyat' : forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'shahar_tuman' : forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'kocha' : forms.TextInput(attrs={'class':'form-control', 'placeholder':"Ko`cha"}),
            'uy_nomeri' : forms.TextInput(attrs={'class':'form-control', 'placeholder':"Ko`cha"}),
            'lavozimi' : forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
            'tel_nomer' : forms.TextInput(attrs={'class':'form-control', 'placeholder':"Ko`cha"}),
            'rasm' : forms.Select(attrs={'class':'form-control', 'placeholder':"Foydalanuvchi"}),
        }
