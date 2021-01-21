from django.shortcuts import render, HttpResponse
from .models import Everegis
from woc.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
class Abc():
    count = 0

    def func():
        Abc.count = Abc.count +1
        return Abc.count

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
            ins.save()
            messages.success(request, 'Your form has been submitted')
            xcount = Abc.func()
            subject = ' Event registration is successful  '
            message = f'Your event is registererd successfully \n\n Event is : {eventname}  \n\n Event ID is {xcount} \n\n Thanks'
            recipient = [ins.hostmail]
            send_mail(subject, message, EMAIL_HOST_USER, recipient, fail_silently=False)
            return render(request, 'everegis.html')
        else:
            return render(request, 'everegis.html')

    def eventlist(request):   
        eventregis = Everegis.objects.all()
        return render(request, 'eventlist.html', {'eventregis': eventregis})

    def index(request):
        products = Product.objects.all()
        return render(request, 'file.html', {'home': products})


    # def inde(request):
    #     if request.method =="POST":
    #         ename = request.POST['ename']
    #         contact = request.POST['contact']
    #         ins = Disp(ename=ename, contact=contact)
    #         ins.save()
    #         return render(request, "index.html")
    #     else:
    #         return render(request, 'index.html')
    #
    #
    # def another(request):
    #     disps = Disp.objects.all()
    #     return render(request, 'another.html', {'disps': disps})


    # def dates(request):
    #     if request.method == "POST":
    #         dates = request.POST['dates']
    #         s = Newdate(dates=dates)
    #         s.save()
    #         return render(request, 'date.html')
    #     else:
    #         return render(request, 'date.html')
    #
    #
    # def new(request):
    #     newdates = Newdate.objects.all()
    #     return(request,'new.html',{'newdates': newdates })

