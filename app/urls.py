from django.urls import path

from . import views

urlpatterns = [
    path("homepage", views.index, name="index"),
    path("about", views.about, name="about"),
    path('service',views.service, name="service"),
    path('query',views.query, name="query"),
    path('contact',views.contact, name="contact"),
    path('service_address',views.service_address, name="service_address"),
    path('eticket',views.eticket, name="eticket"),
    path('confirmTicket<int:travel_id>',views.confirmTicket,name="confirmTicket"),
]