from django.urls import path
from .views import (
    FakultetListView,
    FakultetUpdateView,
    FakultetDeleteView,
    FakultetDetailView,
    FakultetCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', FakultetUpdateView.as_view(), name='fakultet_edit'),
    path('<int:pk>/', FakultetDetailView.as_view(), name='fakultet_detail'),
    path('<int:pk>/delete/', FakultetDeleteView.as_view(), name='fakultet_delete'),
    path('new/', FakultetCreateView.as_view(), name='fakultet_new'),
    path('', FakultetListView.as_view(), name='fakultet_list'),
]