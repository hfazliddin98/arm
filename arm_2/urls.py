from django.urls import path

from pages import views
from . import views
from .views import (
    Arm_2ListView,
    Arm_2UpdateView,
    Arm_2DeleteView,
    Arm_2DetailView,
    Arm_2CreateView,
    Arm_2sinov,

)


urlpatterns = [
    path('<int:pk>/edit/', Arm_2UpdateView.as_view(), name='arm_2_edit'),
    path('<int:pk>/', Arm_2DetailView.as_view(), name='arm_2_detail'),
    path('<int:pk>/delete/', Arm_2DeleteView.as_view(), name='arm_2_delete'),
    path('new/', Arm_2CreateView.as_view(), name='arm_2_new'),
    path('', Arm_2ListView.as_view(), name='arm_2_list'),
    path('sinov/', Arm_2sinov.as_view(), name='arm_2'),
    path('javob/', views.javob, name='javob'),
    path('talaba-kitob/', views.talaba_kitob, name='talaba-kitob'),
    path('talaba_javob/', views.talaba_javob, name='talaba-javob'),
    path('talaba_list/', views.talaba_list, name='talaba-list'),
    path('kitob_list/<kitob_id>', views.kitob_list, name='kitob-list'),
]
