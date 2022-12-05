from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import FoydalanuvchiCreationForm, FoydalanuvchiChangeForm
from .models import Foydalanuvchi

# foydalanuvchi malumotlarini admin panelga bog`lash uchun 
class FoydalanuvchiAdmin(UserAdmin):
    add_from = FoydalanuvchiCreationForm
    form = FoydalanuvchiChangeForm
    model = Foydalanuvchi
# foydalanuvchiga qoshigan malumotlarni admin panelda korsatish uchun yangi madellar kiritiladi
    list_display = [
        'familiya_a', 'ism_a', 'arm_bolim', 
        'viloyat_a', 'email', 'shahar_tuman', 'kocha', 
        'uy_nomeri', 'lavozimi', 'rasm', 'tel_nomer', 'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + (        
        (None, {'fields':('familiya_a',)}),
        (None, {'fields':('ism_a',)}),
        (None, {'fields':('arm_bolim',)}),
        (None, {'fields':('viloyat_a',)}),
        (None, {'fields':('shahar_tuman',)}),
        (None, {'fields':('kocha',)}),
        (None, {'fields':('uy_nomeri',)}),
        (None, {'fields':('lavozimi',)}),
        (None, {'fields':('tel_nomer',)}),
        (None, {'fields':('rasm',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (        
        (None, {'fields':('familiya_a',)}),
        (None, {'fields':('ism_a',)}),
        (None, {'fields':('arm_bolim',)}),
        (None, {'fields':('viloyat_a',)}),
        (None, {'fields':('shahar_tuman',)}),
        (None, {'fields':('kocha',)}),
        (None, {'fields':('uy_nomeri',)}),
        (None, {'fields':('lavozimi',)}),
        (None, {'fields':('tel_nomer',)}),
        (None, {'fields':('rasm',)}),
    )

admin.site.register(Foydalanuvchi, FoydalanuvchiAdmin)


admin.site.unregister(Group)

