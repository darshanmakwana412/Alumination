from tkinter import messagebox
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, migd, EventsAttending, Event_url, speedMentoring, groupm, shadowPrograme
from django.contrib.auth.models import User
import random
import datetime
from twilio.rest import Client
import pandas as pd
import numpy as np

eventsData = {
    "beyond_the_horizon": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "it_software": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "consulting": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "analytics": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "quant": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "hr": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "product_management": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "standup": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "game_night": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "student_alumni_mentorship": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "coming_full_circle": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "ypo": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "tedx": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "ceo_connect": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    },
    "speed_mentoring": {
        "name": "Beyond The Horizon",
        "status": 0,
        "image": "../static/img/events/2.1.jpg",
    }
}

def createMigdExcel():

    df = pd.DataFrame(list(migd.objects.all().values()))
    df.to_csv("Alumination.csv")

def shadowProgram(request):

    context = {
        "message": ""
    }

    if request.method == 'POST':
        paymentProof = request.FILES['paymentProof']

        profile = Profile.objects.filter(user=request.user).first()
        paymentProof.name = f"{profile.rollno}_{profile.name}_{datetime.datetime.now()}_paymentProof.png"

        shadowPrograme(rollno=profile.rollno, image=paymentProof).save()

        context["message"] = "Image Uploaded Successfully"

        return render(request, 'shadowProgram.html', context)        
    else :
        return render(request, 'shadowProgram.html', context)

def profile(request):

    if request.user.is_authenticated:

        user = Profile.objects.filter(user=request.user).first()
        events = EventsAttending.objects.filter(roll_no=user.rollno).first()

        for key, value in list(events.__dict__.items())[2:]:
            eventsData[key]["status"] = value

        context = {
            "user": dict(list(user.__dict__.items())),
            "events": eventsData.values()
        }

        return render(request, 'Profile.html', context)

    else:
        return redirect(loginView)

def teamPage(request):
    return render(request, 'TeamPage.html')

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
                # if (str(otp) == str(request.session['otp'])):
                if(True) :
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

        if not email.split('@')[1]=='iitb.ac.in':
            context = {'message': 'Please register using your LDAP ID'}
            return render(request, 'register.html', context)

        check_user = User.objects.filter(username=rollno).first()
        if check_user:
            check_user.password = contact
            puser = Profile.objects.filter(rollno = rollno).first()
            puser.name = name
            puser.password = contact
            puser.department = department
            puser.degree = degree
            puser.contact = contact
            puser.p_email = p_email
            puser.user = check_user
            puser.save()
            check_user.save()
            return render(request, 'register.html')
        else:         
            user = User(username=rollno, password=contact)
            profile = Profile(user=user, name=name, password=contact, rollno=rollno, department=department, degree=degree,contact=contact, p_email=p_email)
            eventuser = EventsAttending(roll_no=rollno)
            user.save()
            profile.save()
            eventuser.save()
        return redirect('login')
    return render(request, 'register.html')

def index(request):
    return render(request, "alumination.html")



def logoutView(request):
    logout(request)
    return render(request, 'index.html')

@login_required(login_url='/login/')

def mi_gd(request):
    if request.method == 'POST':
        interest = request.POST.get('interest')
        pref_1 = request.POST.get('pref1')
        pref_2 = request.POST.get('pref2')
        pref_3 = request.POST.get('pref3')
        date = request.POST.get('date')
        # coreField = request.POST.get('core_field')
        coreField = "Mech"
        resume = request.FILES['resume']

        profile = Profile.objects.filter(user=request.user).first()
        resume.name = f"{profile.rollno}_{profile.name}_{datetime.datetime.now()}.pdf"

        # migdProfile = migd.objects.filter(rollno=profile.rollno).first()

        # print(migdProfile)

        # if migdProfile:
        #     migdProfile.resume.delete()
        # else :
        migd(rollno=profile.rollno, interest=interest, pref1=pref_1, pref2=pref_2, pref3=pref_3, dateAvailable=date, coreField=coreField , resume=resume).save()
        createMigdExcel()
    return render(request, 'mi_gd.html')

# Events + questions
def event_url(request):
    if request.method=="POST":
        roll_no=request.POST.get("rollno")
        question=request.POST.get("question")
        url=request.get_host+request.path
        url_string=url.toString()
        index = url_string.rfind('/')
        event=url_string[index+1:] 
        data= Event_url(roll_no=roll_no,event=event, question=question)
        data.save() 
    return  render(request, "qna.html")

def bth(request):
    userevent = EventsAttending.objects.filter(roll_no = request.user.username).first()
    context = {'eventstate' : userevent.beyond_the_horizon }
    return render(request, 'bth.html', context )

def speedMentoring(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        pref_1 = request.POST.get('pref1')
        pref_2 = request.POST.get('pref2')
        data = speedMentoring(date=date, pref1=pref_1, pref2=pref_2)
        data.save()
    return render(request, 'speedMentoring.html')

def group_mentoring(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        pref_1 = request.POST.get('pref1')
        pref_2 = request.POST.get('pref2')
        data = groupm(date=date, pref1=pref_1, pref2=pref_2)
        data.save()
    return render(request, 'group_mentoring.html')

def ceoConnect(request):
    userevent = EventsAttending.objects.filter(roll_no = request.user.username).first()
    context = {
        'eventstate' : userevent.ceo_connect
    }
    return render(request, 'ceoConnect.html', context)

def cfc(request):
    userevent = EventsAttending.objects.filter(roll_no = request.user.username).first()
    context = {'eventstate' : userevent.coming_full_circle }
    return render(request, 'cfc.html')

def game_night(request):
    userevent = EventsAttending.objects.filter(roll_no = request.user.username).first()
    context = {'eventstate' : userevent.game_night }
    return render(request, 'game_night.html')

def eventState(request, event, state):
    rollno = request.user.username
    userevent = EventsAttending.objects.filter(roll_no = rollno).first()
    setattr(userevent, event, state)
    userevent.save()