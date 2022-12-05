from django.urls import path
from .views import (
    TumanListView,
    TumanUpdateView,
    TumanDeleteView,
    TumanDetailView,
    TumanCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', TumanUpdateView.as_view(), name='tuman_edit'),
    path('<int:pk>/', TumanDetailView.as_view(), name='tuman_detail'),
    path('<int:pk>/delete/', TumanDeleteView.as_view(), name='tuman_delete'),
    path('new/', TumanCreateView.as_view(), name='tuman_new'),
    path('', TumanListView.as_view(), name='tuman_list'),
]