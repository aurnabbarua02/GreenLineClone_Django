from django.db import models
from datetime import datetime
# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email

class Service(models.Model):
    start = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    def __str__(self):
        return self.start
    
class CompanyProfile(models.Model):
    profile = models.TextField()
class CompanyMission(models.Model):
    mission = models.TextField()
class CompanyVision(models.Model):
    vision = models.TextField()
class CompanyFounder(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
class CompanyManagement(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)


class CallcenterMob(models.Model):
    mob = models.CharField(max_length=15)
    def __str__(self):
        return self.mob
class CallcenterTel(models.Model):
    tel = models.CharField(max_length=15)
    def __str__(self):
        return self.tel
    
class Section2(models.Model):
    icon = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    link = models.CharField(max_length=20)
    def __str__(self):
        return self.title
class GreenLine(models.Model):
    description = models.TextField() 

class HeadOfficeInfo(models.Model):
    address = models.CharField(max_length=200)  
    area = models.CharField(max_length=100)  
    tel = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    email = models.EmailField()

class Counter(models.Model):
    district = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    detail_area = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=15)
    phone2 = models.CharField(max_length=15, null=True, blank=True)
    phone3 = models.CharField(max_length=15, null=True, blank=True)
    def __str__(self):
        return self.district + '-' + self.area

class BusDetails(models.Model):
    bus_id = models.AutoField(primary_key=True) 
    bus_name = models.CharField(max_length=20)
    bus_type = models.CharField(max_length=50)
    bus_details = models.CharField(max_length=100)
    sit_capacity = models.IntegerField()

    def __str__(self):
        return self.bus_name+'-'+self.bus_details

class TravelDetails(models.Model):
    travel_id = models.AutoField(primary_key=True)  
    bus = models.ForeignKey(BusDetails, on_delete=models.CASCADE) 
    leaving_from = models.CharField(max_length=50)
    going_to = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    day = models.CharField(max_length=20, editable=False)  
    fare = models.IntegerField()
    booked_seat = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.date:
            self.day = self.date.strftime("%A") 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.bus.bus_name} - {self.leaving_from} to {self.going_to}"

class Passenger(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    number_of_ticket = models.IntegerField()
    transaction_id = models.CharField(max_length=50)
    travel = models.ForeignKey(TravelDetails, on_delete=models.CASCADE)