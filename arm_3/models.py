from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

TIL_CHOICES = (
    ('uz', 'uzbekcha'),
    ('ru', 'ruscha'),
    ('eng', 'ingilizcha'),
    ('boshqa', 'boshqa'),
)
ALFABIT_CHOICES = (
    ('lotin', 'lotin'),
    ('kiril', 'kiril'),
    ('boshqa', 'boshqa'),
)     
DARLIK_CHOICES = (
    ('darslik', 'darslik'),
    ('o`quv qo`llanma', 'o`quv qo`llanma'),
    ('uslubiy qo`llanma', 'uslubiy qo`llanma'),
    ('badiiy', 'badiiy'),
    ('siyosiy', 'siyosiy'),
    ('ilmiy', 'ilmiy'),
    ('lug`at', 'lug`at'),
    ('managrafiya', 'managrafiya'),
)
KITOB_CHOICES = (
    ('kitob', 'kitob'),
    ('elektron', 'elektron'),
)

# yangi kitob kiritish uchun
class Arm_3(models.Model):
    shifr = models.CharField(max_length=200)
    aftor_belgisi = models.CharField(max_length=200)
    invertor_nomeri = models.CharField(max_length=200)
    mualiflar = models.CharField(max_length=200)
    kitob_nomi = models.CharField(max_length=200)
    nashriyot = models.CharField(max_length=200)
    nashr_yili = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    kitob_narxi = models.CharField(max_length=200)
    tili = models.CharField(choices=TIL_CHOICES, max_length=200) 
    alfabit = models.CharField(choices=ALFABIT_CHOICES, max_length=200) 
    darslik_turi = models.CharField(choices=DARLIK_CHOICES, max_length=200) 
    kitobni_fondagi_soni =  models.CharField(max_length=200)
    anatatsiya = models.CharField(max_length=600)
    mundarija = models.CharField(max_length=600)
    kitob_turi = models.CharField(choices=KITOB_CHOICES, max_length=100)
    fayl = models.FileField(upload_to='kitob/', blank=True)
    sana = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.mualiflar

    def get_absolute_url(self):
        return reverse('arm_3_detail', args=[str(self.id)])
