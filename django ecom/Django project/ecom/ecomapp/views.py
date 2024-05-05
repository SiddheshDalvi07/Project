from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Cart
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    products = Product.objects.filter(is_active=True)
    context = {}
    context['products']=products
    return render(request,'index.html',context)

def productdetail(request,pid):
    product = Product.objects.get(id=pid)
    context = {}
    context['product']=product
    return render(request, 'product_detail.html',context)

def catfilter(request,cid):
    context={}
    q1 = Q(is_active=True)
    q2 = Q(category=cid)
    products=Product.objects.filter(q1&q2)
    context['products']=products
    return render(request,'index.html',context)

def sortbyprice(request,s):
    context={}
    if s=='0':
        products=Product.objects.filter(is_active=True).order_by('-price')
        context['products']=products
        return render(request,'index.html',context)
    else:
        products=Product.objects.filter(is_active=True).order_by('price')
        context['products']=products
        return render(request,'index.html',context)

def pricerange(request):
    context={}
    if(request.method=='GET'):
        return render(request,'index.html',context)
    else:
        min=request.POST['min']
        max=request.POST['max']
        products=Product.objects.filter(is_active=True,price__gte=min,price__lte=max)
        context['products']=products
        return render(request,'index.html',context)
    
def addtocart(request,pid):
    if request.user.is_authenticated:
        uid = request.user.id
        u = User.objects.get(id=uid)
        p = Product.objects.get(id=pid)
        c = Cart.objects.create(uid=u,pid=p)
        c.save()
        return redirect("/")
    else:
        return redirect("/login")





# def productdetail(request,pid):
#     product = Product.objects.get(id=pid)
#     context = {}
#     context['product']=product
#     return render(request, 'product_detail.html',context)













    
#user accounts

def register(request):
    context={}
    if request.method=='GET':
        return render(request,'registration.html',context)
    else:
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        fname=request.POST['fname']
        lname=request.POST['lname']
        if(uname=='' or upass=='' or ucpass=='' or fname=='' or lname=='' ):
            context['error']="Please fill all the fields"
        elif(upass!=ucpass):
            context['error']="Passwords do not match"
        elif uname in [user.username for user in User.objects.all()]:
            context['error']="Username already exists"
            user=None
        else:
            user_info = User.objects.create(username=uname,password=upass,email=uname,first_name=fname,last_name=lname)
            user_info.set_password(upass)
            user_info.save()
        return render(request,'registration.html',context)
    
def user_login(request):
    context = {}
    if(request.method=="GET"):
        return render(request,"login.html")
    else:
        uname = request.POST['uname']
        upass = request.POST['upass']
        if uname=='' or upass=='':
            context['error'] = "Please fill all the fields"
        else:
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                context['success'] = "Login successful"
                return redirect('/')
            else:
                context['error'] = "Invalid Credential"
            print(user)
        return render(request,'login.html',context)

def user_logout(request):
    logout(request)
    return redirect('/')


