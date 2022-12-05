#from django.views.generic import TemplateView

#asosiy ishlanadigan home
#class HomePageView(TemplateView):
#    template_name = 'home.html'

#yangi home
from django.shortcuts import render
from datetime import datetime
import calendar
from calendar import HTMLCalendar

def home(request):
    # vaqt korinishi uchun
    now = datetime.now()
    yil = now.year
    oy = now.month
    kun = now.day
    vaqt = now.strftime('%I:%M %p')

    return render(request, 'home.html', {
        'yil': yil,
        'vaqt': vaqt,
        'oy': oy,
        'kun': kun,
    })




# eski yo`nalish asosiy papkaga joylashtiriladi
# from django.views.generic.base import TemplateView
# path('', TemplateView.as_view(template_name='home.html'), name='home'),
