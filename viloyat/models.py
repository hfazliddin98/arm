from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Viloyat(models.Model):
    viloyat = models.CharField(max_length=200)    
    sana = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.viloyat

    def get_absolute_url(self):
        return reverse('viloyat_detail', args=[str(self.id)])
