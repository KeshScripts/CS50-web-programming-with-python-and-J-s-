from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.shortcuts import render
from flights.models import *

# Create your views here.


      
def index(request): 
   return render(request, "./flights/index.html", {
      "flights":Flight.objects.all()
      
      })
   
def add(request):
   flight = Flight.objects.get(pk = 1)
   
   if request.method == "POST":
      
      jfk = Airport.objects.get(code = "JFK")
      jfk.save()
      bud = Airport.objects.get( code = "BUD")
      bud.save()
      car = Airport.objects.get(code = "CAR")
      car.save()
      origin = Flight (request.POST, instance = flight.city  )
      destination = Flight (request.POST, instance = flight.city)
      duration = request.POST["duration"]
      flight = Flight(origin = origin, destination=destination, duration = duration)
      flight.save()
      return HttpResponseRedirect(reverse ("index"))
      
      
   return render (request, "./flights/add.html",{
      "flights": Airport.objects.all()
   })
   
   
def flight(request,Flight_id):
   flight = Flight.objects.get(id = Flight_id)
   passengers = flight.passengers.all()
   return render(request, "./flights/Flight.html" , {
      
      "flight": flight,
      "passengers": passengers,
      "passengers": passengers,
      "non_passengers":Passenger.objects.exclude(Flight = flight).all(),
      "passlen" : len(passengers)
      
   })
   
def book(request, Flight_id):
   if request.method == "POST":
      flight = Flight.objects.get(pk= Flight_id)
      passengers = Passenger.objects.get(pk = int(request.POST["passengers"]))
      passengers.Flight.add(flight)
      
      return HttpResponseRedirect(reverse("Flight", args=(flight.id,)))
      
   
   
      
   