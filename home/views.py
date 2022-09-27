from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, feedback_question, mi_gd, EventsAttending
from django.contrib.auth.models import User
from django.core.mail import send_mail
import numpy as np
import pandas as pd
import random
from twilio.rest import Client
import os
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# gauth = GoogleAuth()           
# drive = GoogleDrive(gauth)


def generateOtp():
    num = random.random()*1000000
    otp = int(num)
    return otp

def sendOtp(otp, mobno, rollno):
    email = str(rollno) + "@iitb.ac.in"
    mob = "+91" + str(mobno)
    # send_mail("Thank you for Bonding with SARC", "Your OTP for Registering in SARC is "+otp, "web.sarc.iitb@gmail.com", [email, ], fail_silently=False)
    account_sid = "ACde1678c7880c7ca7b06306b36071db1f"
    auth_token = '1a5ea517ab694ce60b0010bc4a739d27'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body='Your OTP for SARC login is ' + str(otp),
    from_='+19289166866',
    to=mob
    )


def loginView(request):

    if request.user.is_authenticated:
            return redirect('index')
    if request.method == 'POST':
        if 'rollno' in request.session:
                otp = request.POST.get('otp')
                print(str(otp))
                if (str(otp) == str(request.session['otp'])):
                    user = User.objects.filter(username = request.session['rollno']).first()
                    login(request, user)
                    print("Success")
                    return render(request, 'index.html')
                else: 
                    context = {'message' : 'Wrong otp'}
                    return render(request, 'login.html', context)                 
        rollno = request.POST.get('rollno')
        user = User.objects.filter(username = rollno)
        if not user :
            context = {'message': 'Profile not found, Please Register'}
            return render(request, 'login.html', context)
        else:
            otp = generateOtp()
            print(otp)
            # sendOtp(otp=otp, mobno=user.username)
            request.session['rollno'] = rollno
            request.session['otp'] = otp
            return render(request, 'login.html')

    return render(request, 'login.html')


def otpview(request):
    if request.method.POST:
        otpin = request.POST.get('otp')
        rollno = request.session['rollno']
        mobno = request.session['mobno']
        otp = request.session['otp']
        if(otpin == otp):
            user = User.objects.filter(username = rollno)
            login(request, user)
        else:
            context = {'message' : 'Incorrect OTP' }
            return render(request, 'otpview.html', context)
    else:
        return render(request, 'otpview.html')


def registerView(request):
    
    if request.user.is_authenticated:
            return redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        department = request.POST.get('department')
        degree = request.POST.get('degree')
        contact = request.POST.get('contact')
        p_email = request.POST.get('p_email')

        check_user = Profile.objects.filter(rollno=rollno).first()
        if check_user:
            context = {'message': 'User already exists'}
            return render(request, 'register.html', context)
        if not email.split('@')[1]=='iitb.ac.in':
            context = {'message': 'Please register using your LDAP ID'}
            return render(request, 'register.html', context)

        # send_mail("Thank you for Bonding with SARC", "Your OTP for Registering in SARC is 345789", "web.sarc.iitb@gmail.com", [email, ], fail_silently=False)

        user = User(username=rollno, password=contact)
        profile = Profile(user=user, name=name, password=contact, rollno=rollno, department=department, degree=degree,contact=contact, p_email=p_email)
        eventuser = EventsAttending(roll_no=rollno)
        user.save()
        profile.save()
        eventuser.save()
        return redirect('login')
    return render(request, 'register.html')


# def addEvents(request):

#     sheetUrl = 'https://docs.google.com/spreadsheets/d/1Y5EQpyrLhIA--inNWizoZE-MJ_4kryAKJSvnvMwy3tA/edit#gid=0'
#     url = sheetUrl.replace('/edit#gid=', '/export?format=csv&gid=')
#     eventData = pd.read_csv(url)

#     Event.objects.all().delete()

#     for i in range(len(eventData)):
#         Event.objects.create(
#             name_ = eventData.iloc[i]["name_"],
#         )

#     return redirect(index)

def index(request):
    # del request.session['rollno']
    # context = {
    #     'events': Event.objects.filter()
    # }

    return render(request, "index.html")



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



# def loginView(request):

#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             return redirect('index')

#         _name = request.POST.get('name')

#         user = Profile.objects.filter(user=request.user)

#         if user is None:
#             context = {'message': 'Profile not found'}
#             return render(request, 'login.html', context)

#         if _name == user.name_ :
#             login(request, user)
#             context = {'name': user.name_}
#             return render(request, 'login.html', context)

#         return render(request, 'login.html')
        
#     return render(request, 'login.html')

# def registerView(request):
#     if request.method == 'POST':
        
#         _name = request.POST.get('name')

#     return render(request, 'register.html')


# Feed back questions Ansh
def feedback_questions(request):
    if request.method=="POST":
        data=request.POST.get('feedback_question')
        save_data=feedback_question(feedback_question=data)
        save_data.save()
        send_mail('Hello feedback from alumination', data , 'sarc.web22@gmail.com',['anshpreet022@gmail.com'] , fail_silently=False)
        return render(request ,'alumination.html')

def alumination(request):
    return render(request, "alumination.html")
