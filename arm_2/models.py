from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from fakultet.models import Fakultet
from tuman.models import Tuman
from yonalish.models import Yonalish
from guruh.models import Guruh
from viloyat.models import Viloyat
from familiya.models import Familiya
from ism.models import Ism
from sharif.models import Sharif



DARAJA_CHOICES = (
    ('bakalavr', 'bakalavr'),
    ('magistr', 'magistr'),
)
KURS_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)
TUMAN_CHOICES = (
    ('Dang`ara', 'Dang`ara'),
    ('Buvayda', 'Buvayda'),
)


class Arm_2(models.Model):
    formulyar_raqami = models.CharField(max_length=200)
    darajasi = models.CharField(choices=DARAJA_CHOICES, max_length=200)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    kurs = models.CharField(choices=KURS_CHOICES, max_length=200)
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    familya = models.ForeignKey(Familiya, on_delete=models.CASCADE)
    ism = models.ForeignKey(Ism, on_delete=models.CASCADE)
    sharifi = models.ForeignKey(Sharif, on_delete=models.CASCADE)
    tugilgan_kun_oy_yil = models.CharField('Tug`ilgan kun/oy/yil', max_length=100)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    kocha_uy = models.CharField(max_length=200)
    tel_raqami = models.CharField(max_length=200)
    pasport_seryasi = models.CharField(max_length=200)
    pasport_raqami = models.CharField(max_length=200)
    sana = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.familya)


    def get_absolute_url(self):
        return reverse('arm_2_detail', args=[str(self.id)])



class Talaba_kitob(models.Model):
    invertor = models.CharField(max_length=200)
    kitob = models.CharField(max_length=200)
    familya = models.ForeignKey(Familiya, on_delete=models.CASCADE)
    ism = models.ForeignKey(Ism, on_delete=models.CASCADE)
    sharifi = models.ForeignKey(Sharif, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.familya)
