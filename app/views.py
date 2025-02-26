from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from app.form import *
from .models import *
# Create your views here.
navitems = [
        ['Home','homepage'],
        ['About us','about'],
        ['Service','service'],
        ['Query','query'],
        ['Contact us','contact'],
        ['E-ticket','eticket']
    ]   
about_greenline = GreenLine.objects.values().first()
headOffice = HeadOfficeInfo.objects.values().first()
counters = ['Dhaka', 'Chattogram', 'Khulna', 'Sylhet', 'Rangpur','Coxs Bazar']
def index(request):     
    section2 = Section2.objects.all().values()
    greenline = GreenLine.objects.all().values()    
    
    context = {
        'navitems':navitems,
        'section2':section2,
        'counters':counters,
        'greenline':greenline,
        'about_greenline':about_greenline, 'headOffice':headOffice
    } 
    return render(request, "app/index.html", context)

def about(request):   
    companyProfile = CompanyProfile.objects.all().values()  
    companyMission = CompanyMission.objects.all().values() 
    companyVision = CompanyVision.objects.all().values() 
    companyFounder = CompanyFounder.objects.values().first() 
    companyManagement = CompanyManagement.objects.all().values()  
    context={
        'navitems':navitems,'companyProfile':companyProfile,'companyMission':companyMission,
        'companyVision':companyVision, 'companyFounder':companyFounder,'companyManagement':companyManagement,
        'about_greenline':about_greenline, 'headOffice':headOffice
    }
    return render(request, "app/about.html", context)

def service(request):
    services = Service.objects.all().values()
    context={
        'navitems':navitems,
        'services':services,'about_greenline':about_greenline, 'headOffice':headOffice
    }
    return render(request, "app/service.html", context)

def query(request):
    form = sendmessageform(request.POST)
    context={
        'navitems':navitems,
        'form':form,'about_greenline':about_greenline, 'headOffice':headOffice
    }
    if (request.method == 'POST'):        
        if (form.is_valid()):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            contact = Query.objects.create(name=name, email=email,subject=subject, message=message)
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('query')         
    
    return render(request, "app/query.html", context)

def contact(request):    
    callcenterMob = CallcenterMob.objects.all().values()
    callcenterTel = CallcenterTel.objects.all().values()
    context={
        'navitems':navitems, 'headOffice':headOffice,'callcenterMob':callcenterMob,'callcenterTel':callcenterTel,
        'about_greenline':about_greenline, 'headOffice':headOffice
    }
    return render(request, "app/contact.html", context)

def service_address(request):
    address = request.GET.get('value', '')
    info = Counter.objects.all().values()    
    context={
        'navitems':navitems,'address':address,
        'about_greenline':about_greenline, 'headOffice':headOffice, 'info':info
    }
    return render(request, "app/service_address.html", context)

def eticket(request):    
    # counters = TravelDetails.objects.values_list('leaving_from', flat=True).distinct()  

    form = EticketForm(request.GET)  
    form.fields['leaving_from'].choices = [('', 'Select Please')] + [(c, c) for c in counters]
    form.fields['going_to'].choices = [('', 'Select Please')] + [(c, c) for c in counters]

    travelDetails = TravelDetails.objects.all() 

    if request.method == 'GET' and form.is_valid():
        leaving_from = form.cleaned_data.get('leaving_from', '')
        going_to = form.cleaned_data.get('going_to', '')
        date = form.cleaned_data.get('date', '')

        if leaving_from:
            travelDetails = travelDetails.filter(leaving_from=leaving_from)
        if going_to:
            travelDetails = travelDetails.filter(going_to=going_to)
        if date:
            travelDetails = travelDetails.filter(date=date)
    else:
        leaving_from = going_to = date = ""

    context = {
        'navitems': navitems,
        'about_greenline': about_greenline,
        'headOffice': headOffice,
        'form': form,
        'leaving_from': leaving_from,
        'going_to': going_to,
        'date': date,
        'busDetails': BusDetails.objects.all(),
        'travelDetails': travelDetails
    }

    return render(request, "app/eticket.html", context)

def confirmTicket(request,travel_id):
    travel = get_object_or_404(TravelDetails, pk=travel_id) 
    available_ticket = travel.bus.sit_capacity - travel.booked_seat
    form = ConfirmTicketForm(request.POST)
    
    if request.method == 'POST' and form.is_valid():
        passenger_name = form.cleaned_data['passenger_name']
        passenger_email = form.cleaned_data['passenger_email']
        number_of_ticket = form.cleaned_data['number_of_ticket']
        transaction_id = form.cleaned_data['transaction_id'] 
        if number_of_ticket > available_ticket:
            messages.error(request, "Not enough available seats!")
        else:
            passenger = Passenger.objects.create(passenger_name=passenger_name,passenger_email=passenger_email,number_of_ticket=number_of_ticket,transaction_id=transaction_id,travel=travel)
            passenger.save()
            travel.booked_seat += number_of_ticket
            travel.save(update_fields=['booked_seat'])
            messages.success(request, "Your ticket has been booked successfully!")
            return redirect('confirmTicket', travel_id=travel_id)  
    context={
        'navitems':navitems,
        'about_greenline':about_greenline, 'headOffice':headOffice,'travel':travel,'form':form,'available_ticket':available_ticket,
    
    }
    return render(request, "app/confirmTicket.html", context)
    