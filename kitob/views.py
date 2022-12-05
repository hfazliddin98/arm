from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Kitob
from .forms import KitobForm



def new_kitob(request):
    submitted = False
    if request.method == 'POST':
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/kitob/new_kitob/?submitted=True')
    else:
        form = KitobForm
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'kitob/new_kitob.html', {
        'form': form,
        'submitted': submitted,
    })

def kitob_3(self):
    usr = self.request.user
    print(usr)
    return self

def kitob(request):
    usd = kitob_3.usr
    ktob = Kitob.objects.filter(foy=1).all()
    return render(request, 'kitob/kitob_javob.html', {
        'ktob': ktob,
        'usd': usd,
    })
