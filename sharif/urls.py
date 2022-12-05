from django.urls import path
from .views import (
    SharifListView,
    SharifUpdateView,
    SharifDeleteView,
    SharifDetailView,
    SharifCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', SharifUpdateView.as_view(), name='sharif_edit'),
    path('<int:pk>/', SharifDetailView.as_view(), name='sharif_detail'),
    path('<int:pk>/delete/', SharifDeleteView.as_view(), name='sharif_delete'),
    path('new/', SharifCreateView.as_view(), name='sharif_new'),
    path('', SharifListView.as_view(), name='sharif_list'),
]