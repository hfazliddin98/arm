from django.urls import path
from .views import (
    YonalishListView,
    YonalishUpdateView,
    YonalishDeleteView,
    YonalishDetailView,
    YonalishCreateView,
       
)


urlpatterns = [    
    path('<int:pk>/edit/', YonalishUpdateView.as_view(), name='yonalish_edit'),
    path('<int:pk>/', YonalishDetailView.as_view(), name='yonalish_detail'),
    path('<int:pk>/delete/', YonalishDeleteView.as_view(), name='yonalish_delete'),
    path('new/', YonalishCreateView.as_view(), name='yonalish_new'),
    path('', YonalishListView.as_view(), name='yonalish_list'),
    
]