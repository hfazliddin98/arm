from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import Foydalanuvchi
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


class Kitob(models.Model):
    formulyar_raqami = models.CharField(max_length=200)
    foy = models.ForeignKey(Foydalanuvchi, on_delete=models.CASCADE)
    tel_raqami = models.CharField(max_length=200)
    pasport_seryasi = models.CharField(max_length=200)
    pasport_raqami = models.CharField(max_length=200)
    # sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.foy)
