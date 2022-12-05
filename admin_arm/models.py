from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
BOLIM_CHOICES = (
    ('arm-1', 'arm-1'),
    ('arm-2', 'arm-2'),
    ('arm-3', 'arm-3'),
    ('arm-4', 'arm-4'),
)
LAVOZIM_CHOICES = (
    ('hodim', 'hodim'),   
)


# ro'yhatdan o'tish jarayonida yangi qator qo'shish uchun ishlatiladi
class ArmAdmin(models.Model):   
    familiya_arm = models.CharField('Familiya', max_length=200)
    ism = models.CharField('Ism', max_length=200)
    arm_bolim = models.CharField('ARM bo`lim', choices=BOLIM_CHOICES, max_length=100)
    viloyat = models.CharField('Viloyat', max_length=200)
    shahar_tuman = models.CharField('Shahar tuman', max_length=200)
    kocha = models.CharField('Ko`cha nomi', max_length=200)
    uy_nomeri = models.CharField('Uy nomer', max_length=200)
    lavozimi = models.CharField('Lavozim', choices=LAVOZIM_CHOICES, max_length=200)
    tel_nomer = models.CharField('Telefon raqam', max_length=200)
    rasm = models.ImageField(upload_to='images/', null = True, blank=True)
    sana = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.familiya_arm

   

