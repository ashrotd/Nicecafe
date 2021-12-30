from django.shortcuts import render
from .models import Career
# Create your views here.
def career(request):
    data = Career.objects.all()
    context = {'data': data}
    
    return render(request,'career.html', context)