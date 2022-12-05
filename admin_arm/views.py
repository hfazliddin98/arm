from django.shortcuts import render
from .models import ArmAdmin
from .forms import Arm_adminForm

# Create your views here.
def arm_admin(request):
    admin = ArmAdmin.objects.all()
    return render(request, 'admin/arm-admin.html', {
            'admin': admin,            
    })