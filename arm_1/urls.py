from django.urls import path
from .views import (
    Arm_1ListView,
    Arm_1UpdateView,
    Arm_1DeleteView,
    Arm_1DetailView,
    Arm_1CreateView,      
)

urlpatterns = [            
    path('<int:pk>/edit/', Arm_1UpdateView.as_view(), name='arm_1_edit'),
    path('<int:pk>/', Arm_1DetailView.as_view(), name='arm_1_detail'),
    path('<int:pk>/delete/', Arm_1DeleteView.as_view(), name='arm_1_delete'),
    path('new/', Arm_1CreateView.as_view(), name='arm_1_new'),
    path('', Arm_1ListView.as_view(), name='arm_1_list'),    
]

