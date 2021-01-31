from django.shortcuts import render, HttpResponse
from .models import Everegis,Participants
from woc.settings import EMAIL_HOST_USER
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from twilio.rest import Client
import datetime
import pytz
from django.utils import timezone


# Create your views here.
class Abc():

    def hp(request):
        return render(request, "homepage.html")

    def everegis(request):
        if request.method == "POST":
            eventname = request.POST['eventname']
            description = request.POST['description']
            location = request.POST['location']
            fromdate = request.POST['fromdate']
            todatee = request.POST['todatee']
            deadline = request.POST['deadline']
            hostmail = request.POST['hostmail']
            hostPassword = request.POST['hostPassword']
            ins = Everegis(eventname=eventname, description=description, location=location, fromdate=fromdate, todatee=todatee,deadline=deadline,
                           hostmail=hostmail, hostPassword=hostPassword)
            utc=pytz.UTC
            now = datetime.datetime.now()
            if fromdate > todatee :
                messages.success(request, ' From date should be less than todate ')
            elif deadline > fromdate :
                messages.success(request, 'Registration deadline should be less than fromdate!')
            else:
                ins.save()
                messages.success(request, 'Your form has been submitted')
                subject = ' Event registration is successful  '
                message = f'Your event is registererd successfully \n\n Event is : {eventname}  \n\n Event ID is {ins.id} \n\n Thanks'
                recipient = [ins.hostmail]
                send_mail(subject, message, EMAIL_HOST_USER, recipient, fail_silently=False)
        return render(request, 'everegis.html')

    def eventlist(request):
        b=[]
        utc=pytz.UTC
        now = datetime.datetime.now()
        eventregis = Everegis.objects.all()
        for event in eventregis:
            deadline= event.deadline
            if deadline.replace(tzinfo=utc) > now.replace(tzinfo=utc):
                b.append(event)
        if request.method=="POST":
            name=  request.POST['name']
            phone= request.POST['phone']
            email=  request.POST['email']
            eventype = request.POST['eventType']
            regtype= request.POST['registration']
            if regtype == "group":
                people=  request.POST['people']
                participant = Participants(name=name,phone=phone, email = email, eventype= eventype, regtype= regtype, people=people)
            else:
                 participant = Participants(name=name,phone=phone, email = email, eventype= eventype, regtype= regtype)
            check = True
            participants = Participants.objects.all()
            for p in participants:
                check = True
                if  (participant.phone == p.phone or participant.name == p.name) and int(participant.eventype) == p.eventype and participant.regtype == p.regtype :  
                    check= False
                    break
            if check==True:
                participant.save()
                messages.error(request, 'Form is submitted')
                for eve in eventregis:
                    if eve.id == int(participant.eventype):
                        evedate = eve.fromdate
                        endate= eve.todatee
                        loc = eve.location
                        eventname = eve.eventname
                        temp = str(evedate).split(' ')
                        sdate = temp[0]
                        stime = temp[1].split('+')[0]

                        temp = str(endate).split(' ')
                        edate = temp[0]
                        etime = temp[1].split('+')[0]

                message_to_broadcast = f"Thank you {participant.name} for registration \n\n Your participant id is : {participant.id} \n\n Event is : {eventname} \n\n Date of event is : {sdate} - {edate} \n\n Time is :{stime} - {etime} \n\n Participation type is: {participant.regtype} "
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                message = client.messages.create(to='+91' + str(participant.phone),from_=settings.TWILIO_NUMBER,body= message_to_broadcast)           
            else:
                messages.error(request, 'Already submitted the form !!!')
        return render(request, 'eventlist.html', {'eventregis': b})


    def eventdash(request):
        if request.method=="POST":
            eveid= request.POST['eventid']
            password= request.POST['paswrd']
            participants = Participants.objects.all()
            eventregis = Everegis.objects.all()
            flag= 0
            
            partici=[]
            for e in eventregis:
                if e.id == int(eveid):
                    if e.hostPassword == password:
                        flag =1
                        for p in participants:
                            if p.eventype==int(eveid):
                                partici.append(p)  
                        content={
                            'participants' : partici
                        }
                        break
                    else:
                        flag = 2
            if flag == 1:
                if not partici:
                    messages.error(request, 'No participants exists')
                    return render(request,'eventdash.html')
                else:
                    return render(request,'eventdash.html',content)   
            elif flag == 0:
                messages.error(request, 'Event id does not exists')
                return render(request,'eventdash.html')
            elif flag == 2:
                messages.error(request, 'Incorrect Password')
                return render(request,'eventdash.html')
            else:
                messages.error(request, 'Incorrect')
                return render(request,'eventdash.html')
        else:
            return render(request,'eventdash.html')



    


