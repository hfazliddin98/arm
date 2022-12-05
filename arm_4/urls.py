from django.urls import path
#from .views import (
  #  Arm_4ListView,       
#)
from django.urls import path
from .views import (
    Arm_4ListView,
    Arm_4UpdateView,
    Arm_4DeleteView,
    Arm_4DetailView,
    Arm_4CreateView,
    Arm_4HListView,      
)

urlpatterns = [            
    path('<int:pk>/edit/', Arm_4UpdateView.as_view(), name='arm_4_edit'),
    path('<int:pk>/', Arm_4DetailView.as_view(), name='arm_4_detail'),
    path('<int:pk>/delete/', Arm_4DeleteView.as_view(), name='arm_4_delete'),
    path('new/', Arm_4CreateView.as_view(), name='arm_4_new'),
    path('', Arm_4ListView.as_view(), name='arm_4_list'),
    path('arm/', Arm_4HListView.as_view(), name='arm'),  
]

#urlpatterns = [    
  #  path('arm/', Arm_4ListView.as_view(), name='arm'),   
#]