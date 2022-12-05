from django.urls import path
from . import views

# asosiy yonalish
#from .views import HomePageView

#urlpatterns = [
#    path('', HomePageView.as_view(), name='home'),
#]

# yangi yo`nalish
urlpatterns = [
    path('', views.home, name='home'),
]