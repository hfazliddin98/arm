from django.contrib.auth.models import AbstractUser
from django.db import models



BOLIM_CHOICES = (
    ('arm-1', 'arm-1'),
    ('arm-2', 'arm-2'),
    ('arm-3', 'arm-3'),
    ('arm-4', 'arm-4'),
)
LAVOZIM_CHOICES = (
    ('o`qtuvchi', 'o`qtuvchi'),
    ('talaba', 'talaba'),
)
# ro'yhatdan o'tish jarayonida yangi qator qo'shish uchun ishlatiladi
class Foydalanuvchi(AbstractUser):   
    familiya_a = models.CharField('Familiya', max_length=200)
    ism_a = models.CharField('Ism', max_length=200)
    arm_bolim = models.CharField('ARM bo`lim', choices=BOLIM_CHOICES, max_length=100, blank=True)
    viloyat_a = models.CharField('Viloyat', max_length=200)
    shahar_tuman = models.CharField('Shahar tuman', max_length=200)
    kocha = models.CharField('Ko`cha nomi', max_length=200)
    uy_nomeri = models.CharField('Uy nomer', max_length=200)
    lavozimi = models.CharField('Lavozim', choices=LAVOZIM_CHOICES, max_length=200, blank=True)
    tel_nomer = models.CharField('Telefon raqam', max_length=200)
    rasm = models.ImageField(upload_to='images/', null = True, blank=True)
