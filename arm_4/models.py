from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# yangi kitob kiritish uchun
class Arm_4(models.Model):
        fan = models.CharField(max_length=200)
        adabiyot = models.CharField(max_length=200)
        mualif = models.CharField(max_length=200)
        qollanma = models.CharField(max_length=200)              
        sana = models.DateTimeField(auto_now_add=True)
        author = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
        )
        def __str__(self):
            return self.fan

        def get_absolute_url(self):
            return reverse('arm_4_detail', args=[str(self.id)])