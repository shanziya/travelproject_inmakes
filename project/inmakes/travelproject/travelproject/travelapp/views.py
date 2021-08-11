from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    des=team.objects.all()
    return render(request,"index.html",{'result':obj,'desgnation':des})

# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse('contact page')