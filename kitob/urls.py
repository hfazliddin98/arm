from urllib.request import urlretrieve
from . import views
from django.urls import path


urlpatterns = [
    path('kitob/', views.kitob, name='kitob_javob'),
    path('new_kitob/', views.new_kitob, name='new_kitob'),
]
