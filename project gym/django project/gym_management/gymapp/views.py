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

def personaltraining(request):
    return render(request,"personaltraining.html")

def classes(request):
    return render(request,"classes.html")

def kickboxing(request):
    return render(request,"kickboxing.html")

def indoorcycling(request):
    return render(request,"indoorcycling.html")

def zumbafitness(request):
    return render(request,"zumbafitness.html")

def poweryoga(request):
    return render(request,"poweryoga.html")

def nutrition(request):
    return render(request,"nutrition.html")

def careers(request):
    return render(request,"careers.html")

def location(request):
    return render(request,"location.html")

def aboutus(request):
    return render(request,"aboutus.html")

def termscondition(request):
    return render(request,"termscondition.html")

def policy(request):
    return render(request,"policy.html")

def login(request):
    return render(request,"LoginPage.html")

def register(request):
    return render(request,"RegisterPage.html")