from django.shortcuts import render,redirect
from .models import *
from .form import *


def create(request):

    if request.method=='POST':
        a=studentForm(request.POST)
        if a.is_valid():
            a.save()
        else:print('invalid Input')
    else:pass
    a=studentForm()
    b= register.objects.all()       
    return render(request,'index.html',{'frm':a, 'data':b})


def update(request,id):
    c=register.objects.get(id = id)
    d=register.objects.all()
    e= studentForm(instance=c)
    if request.method=='POST':
        a= studentForm(request.POST, instance=c)
        if a.is_valid():
            a.save()
            return redirect('create')
        else:pass
    else:pass
    return render(request,'index.html',{'frm':e, 'data':d})

def delete(request,id):
    c=register.objects.get(id=id)
    c.delete()
    return redirect('create')






# def read(request):
#     b= register.objects.all()
#     return render(request,'read.html',{'data': b})
 








# Create your views here.
