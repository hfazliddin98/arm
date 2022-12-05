from django.urls import path
from . import views


urlpatterns = [   
    path('arm-admin/', views.arm_admin, name='arm-admin'),
]
