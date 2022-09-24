from atexit import register
from django.shortcuts import render
from mi_gd.models import mi_gd
import os

# Create your views here.
def migd(request):
    if request.method == 'POST':
        mode = request.POST.get('mode')
        pref_1 = request.POST.get('pref1')
        pref_2 = request.POST.get('pref2')
        pref_3 = request.POST.get('pref3')
        date = request.POST.get('date')
        resume = request.FILES['resume']
        register = mi_gd(mode=mode, pref1=pref_1, pref2=pref_2, pref3=pref_3,date=date, resume=resume)
        register.save()
        os.rename(resume.name, 'new.pdf')
    return render(request, 'mi_gd.html')  