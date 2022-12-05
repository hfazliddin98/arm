from django.urls import path
from .views import (
    Arm_3ListView,
    Arm_3UpdateView,
    Arm_3DeleteView,
    Arm_3DetailView,
    Arm_3CreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', Arm_3UpdateView.as_view(), name='arm_3_edit'),
    path('<int:pk>/', Arm_3DetailView.as_view(), name='arm_3_detail'),
    path('<int:pk>/delete/', Arm_3DeleteView.as_view(), name='arm_3_delete'),
    path('new/', Arm_3CreateView.as_view(), name='arm_3_new'),
    path('', Arm_3ListView.as_view(), name='arm_3_list'),
]