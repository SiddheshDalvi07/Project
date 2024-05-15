from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def offers(request):
    return render(request,'offers.html')


def freepass(request):
    return render(request,"1dayfreeguestpass.html")