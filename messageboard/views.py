from django.shortcuts import render
from messageboard.models import tubi
import datetime
# Create your views here.
def index(request):
    mes = tubi.objects.filter(name__icontains="")
    return render(request,'index.html',{'mes':mes})

def gets(request):
    names = request.GET['namea']
    contents = request.GET['contenta']
    if (names != "" and contents != ""):
        tubi.objects.create(name = names,content = contents)
    mes = tubi.objects.filter(name__icontains="")
    return render(request,'index.html',{'mes':mes})
	
def dels(request):
    tubi.objects.filter(name__icontains="").delete()
    return render(request,'index.html')