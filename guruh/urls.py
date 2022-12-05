from django.urls import path
from .views import (    
    GuruhListView,
    GuruhUpdateView,
    GuruhDeleteView,
    GuruhDetailView,
    GuruhCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', GuruhUpdateView.as_view(), name='guruh_edit'),
    path('<int:pk>/', GuruhDetailView.as_view(), name='guruh_detail'),
    path('<int:pk>/delete/', GuruhDeleteView.as_view(), name='guruh_delete'),
    path('new/', GuruhCreateView.as_view(), name='guruh_new'),
    path('', GuruhListView.as_view(), name='guruh_list'),
]