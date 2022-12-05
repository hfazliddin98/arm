from django.urls import path
from . import views
from .views import (
    Talaba,
    TalabaOlgan,
    TalabaBarcha,
    TalabaBuyurtma,
    TalabaYangilik,
    TalabaListView,
    TalabaUpdateView,
    TalabaDeleteView,
    TalabaDetailView,
    TalabaCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', TalabaUpdateView.as_view(), name='talaba_edit'),
    path('<int:pk>/', TalabaDetailView.as_view(), name='talaba_detail'),
    path('<int:pk>/delete/', TalabaDeleteView.as_view(), name='talaba_delete'),
    path('new/', TalabaCreateView.as_view(), name='talaba_new'),
    path('', TalabaListView.as_view(), name='talaba_list'),
    path('talaba/', Talaba.as_view(), name='talaba'),
    path('barcha/', TalabaBarcha.as_view(), name='barcha'),
    path('yangilik/', TalabaYangilik.as_view(), name='yangilik'),
    path('buyurtma/', TalabaBuyurtma.as_view(), name='buyurtma'),
    path('olgan/', TalabaOlgan.as_view(), name='olgan_kitob'),  
    path('oldi/', views.talaba, name='olgan_kitob'), 
]
