from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Contact, Subscription
# Create your views here.
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.full_name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()
        messages.success(request,"Thank you for your message!!!")
    return render(request,'contact.html')

def subscription(request):
    if request.method == 'POST':
        user = Subscription()
        user.email = request.POST.get('email')
        user.save()
        
    return render(request,'includes/greetings.html')