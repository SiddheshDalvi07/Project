from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def offers(request):
    return render(request,'offers.html')


def freepass(request):
    return render(request,"1dayfreeguestpass.html")

def accrecovery(request):
    return render(request,"accrecovery.html")

def abcoffee(request):
    return render(request,"abcoffee.html")

def starttoday(request):
    return render(request,"starttoday.html")

def rapidmuscle(request):
    return render(request,"rapidmuscle.html")

def referafriend(request):
    return render(request,"referafriend.html")

def membership(request):
    return render(request,"membership.html")