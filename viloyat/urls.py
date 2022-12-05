from django.urls import path
from .views import (
    ViloyatListView,
    ViloyatUpdateView,
    ViloyatDeleteView,
    ViloyatDetailView,
    ViloyatCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', ViloyatUpdateView.as_view(), name='viloyat_edit'),
    path('<int:pk>/', ViloyatDetailView.as_view(), name='viloyat_detail'),
    path('<int:pk>/delete/', ViloyatDeleteView.as_view(), name='viloyat_delete'),
    path('new/', ViloyatCreateView.as_view(), name='viloyat_new'),
    path('', ViloyatListView.as_view(), name='viloyat_list'),
]