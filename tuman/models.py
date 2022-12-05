from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Tuman(models.Model):
    tuman = models.CharField(max_length=200)    
    sana = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.tuman

    def get_absolute_url(self):
        return reverse('tuman_detail', args=[str(self.id)])
