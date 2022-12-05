from django.urls import path
from .views import (
    KafedraListView,
    KafedraUpdateView,
    KafedraDeleteView,
    KafedraDetailView,
    KafedraCreateView,    
)


urlpatterns = [    
    path('<int:pk>/edit/', KafedraUpdateView.as_view(), name='kafedra_edit'),
    path('<int:pk>/', KafedraDetailView.as_view(), name='kafedra_detail'),
    path('<int:pk>/delete/', KafedraDeleteView.as_view(), name='kafedra_delete'),
    path('new/', KafedraCreateView.as_view(), name='kafedra_new'),
    path('', KafedraListView.as_view(), name='kafedra_list'),
]