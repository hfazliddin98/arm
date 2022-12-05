from django.urls import path
from .views import (
    IsmListView,
    IsmUpdateView,
    IsmDeleteView,
    IsmDetailView,
    IsmCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', IsmUpdateView.as_view(), name='ism_edit'),
    path('<int:pk>/', IsmDetailView.as_view(), name='ism_detail'),
    path('<int:pk>/delete/', IsmDeleteView.as_view(), name='ism_delete'),
    path('new/', IsmCreateView.as_view(), name='ism_new'),
    path('', IsmListView.as_view(), name='ism_list'),
]