from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Profile, mi_gd
import numpy as np
import pandas as pd
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

def addEvents(request):

    sheetUrl = 'https://docs.google.com/spreadsheets/d/1Y5EQpyrLhIA--inNWizoZE-MJ_4kryAKJSvnvMwy3tA/edit#gid=0'
    url = sheetUrl.replace('/edit#gid=', '/export?format=csv&gid=')
    eventData = pd.read_csv(url)

    Event.objects.all().delete()

    for i in range(len(eventData)):
        Event.objects.create(
            name_ = eventData.iloc[i]["name_"],
        )

    return redirect(index)

def index(request):

    context = {
        'events': Event.objects.filter()
    }

    return render(request, "index.html", context)

def loginView(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('index')

        _name = request.POST.get('name')

        user = Profile.objects.filter(user=request.user)

        if user is None:
            context = {'message': 'Profile not found'}
            return render(request, 'login.html', context)

        if _name == user.name_ :
            login(request, user)
            context = {'name': user.name_}
            return render(request, 'login.html', context)

        return render(request, 'login.html')
        
    return render(request, 'login.html')

def registerView(request):
    if request.method == 'POST':
        
        _name = request.POST.get('name')

    return render(request, 'register.html')

def logoutView(request):
    logout(request)
    return render(request, 'index.html')

@login_required(login_url='/login/')

def profile(request):
    if request.user.is_authenticated:
        context= {}
        user = Profile.objects.filter(user=request.user).first()
        context['user'] = user    
        return render(request, "profile.html", context)
    else:
        return redirect("/login/")

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
        os.chdir('resume')
        os.rename(resume.name, 'hello.pdf')
        #gfile = drive.CreateFile({'parents': [{'id': '1TgjDODLKJ8YFTs8PBqigcwR0RsXN4o7O'}]})
        #gfile.SetContentFile('resume')
        # gfile.Upload() # Upload the file.
    return render(request, 'mi_gd.html')  