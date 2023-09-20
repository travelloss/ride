# from django.http import HttpResponse
# from django.shortcuts import render
#
# #Create your views here.
#
#
from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Photo


def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

def dem(request):
    ob=Photo.objects.all()
    return render(request,"index.html",{'result1':ob})

