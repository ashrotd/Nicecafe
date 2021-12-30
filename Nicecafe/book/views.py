from django.shortcuts import render
from .models import Booking
from django.contrib import messages
# Create your views here.
def book(request):
    if request.method == 'POST':
        book = Booking()
        book.dateTime = request.POST.get('dateTime')
        book.name = request.POST.get('name')
        book.number = request.POST.get('number')
        book.save()
        messages.success(request,"Thank You for Booking !!!")
    return render(request,'book.html')