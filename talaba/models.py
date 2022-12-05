from django.contrib.auth import get_user_model
from django.db import models
#from phonenumber_field.phonenumber import PhoneNumber
from django.urls import reverse
from ism.models import Ism
from sharif.models import Sharif
from viloyat.models import Viloyat
from tuman.models import Tuman
from familiya.models import Familiya
from fakultet.models import Fakultet
from yonalish.models import Yonalish
from guruh.models import Guruh


KURS_CHOICES = (
    ('1', '1'),    
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

# yangi kitob kiritish uchun
class Talaba(models.Model):
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    kurs = models.CharField(choices=KURS_CHOICES, max_length=200)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    familiya = models.ForeignKey(Familiya, on_delete=models.CASCADE)
    ism = models.ForeignKey(Ism, on_delete=models.CASCADE)
    sharif = models.ForeignKey(Sharif, on_delete=models.CASCADE)
    tugilgan_kun_oy_yil = models.CharField('Tug`ilgan kun/oy/yil', max_length=100)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    kocha_uy = models.CharField(max_length=200)
    tel_raqami = models.CharField('Telefon raqam', max_length=13)
    pasport_seryasi = models.CharField(max_length=2)
    pasport_raqami = models.IntegerField()   
    sana = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    

    def __str__(self):
        return str(self.familiya)

    def get_absolute_url(self):
        return reverse('talaba_detail', args=[str(self.id)])
    
   



