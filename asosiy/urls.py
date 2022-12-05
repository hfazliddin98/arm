"""asosiy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from arm_2 import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('arm-1/', include('arm_1.urls')),
    path('arm-2/', include('arm_2.urls')),     
    path('arm-3/', include('arm_3.urls')),
    path('arm/', include('arm_4.urls')),
    path('kitob/', include('arm_4.urls')),
    path('fakultet/', include('fakultet.urls')),    
    path('kafedra/', include('kafedra.urls')),
    path('yonalish/', include('yonalish.urls')),
    path('guruh/', include('guruh.urls')),
    path('viloyat/', include('viloyat.urls')),
    path('familiya/', include('familiya.urls')),
    path('ism/', include('ism.urls')),
    path('sharif/', include('sharif.urls')),
    path('tuman/', include('tuman.urls')),
    #path('tyutr/', include('tyutr.urls')),
    #path('fanlar/', include('fanlar.urls')),
    path('dekanat/', include('dekanat.urls')),
    path('talaba/', include('talaba.urls')), 
    path('kitob/', include('kitob.urls')),    
    path('', include('pages.urls')),
    path('arm-admin/', include('admin_arm.urls')),
]

admin.site.index_title = 'ARM Umumiy Bazasi'
admin.site.site_header = 'QDPI Kutubxonasi'
admin.site.site_title = 'Admin Sahifasiga kirish'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
