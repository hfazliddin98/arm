from django.urls import path
from .views import (
    FamiliyaListView,
    FamiliyaUpdateView,
    FamiliyaDeleteView,
    FamiliyaDetailView,
    FamiliyaCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', FamiliyaUpdateView.as_view(), name='familiya_edit'),
    path('<int:pk>/', FamiliyaDetailView.as_view(), name='familiya_detail'),
    path('<int:pk>/delete/', FamiliyaDeleteView.as_view(), name='familiya_delete'),
    path('new/', FamiliyaCreateView.as_view(), name='familiya_new'),
    path('', FamiliyaListView.as_view(), name='familiya_list'),
]