from django.shortcuts import render
from app1.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
           c= form1.save()
           return render(request,'app1/index.html',{'param1':c.id1})
    else:
        form1=inputform() 
    return render(request,'app1/index2.html',{'form':form1})
