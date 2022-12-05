from django.urls import path
from .views import Dekanat

urlpatterns = [    
    path('dekanat/', Dekanat.as_view(), name='dekanat'),
]

