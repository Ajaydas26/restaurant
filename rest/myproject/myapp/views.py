from django.urls import path
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')
def food(request):
    return render(request,'food.html')
def biriyani(request):
    return render(request,'biriyani.html')
def Kuzhimandhi(request):
    return render(request,'Kuzhimandhi.html')
def noodles(request):
    return  render(request,'noodles.html')
def shakes(request):
    return render(request,'shakes.html')