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

def trainerregister(request):
    return render(request,"trainerregister.html")

from django.shortcuts import render, redirect
from .models import Trainer
from django.contrib.auth.hashers import make_password

def trainerregister(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'trainerregister.html', context)
    else:
        name = request.POST['name']
        emailid = request.POST['email']
        photo = request.FILES.get('photo')
        contact = request.POST['contact']
        age = request.POST['age']
        gender = request.POST['gender']
        salary = request.POST['salary']
        experience = request.POST['experience']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not all([name, emailid, photo, contact, age, gender, salary, experience, password, confirm_password]):
            context['error'] = "Please fill all the fields"
        elif password != confirm_password:
            context['error'] = "Passwords do not match"
        elif Trainer.objects.filter(emailid=emailid).exists():
            context['error'] = "Email already exists"
        else:
            trainer = Trainer(
                name=name,
                emailid=emailid,
                photo=photo,
                contact=contact,
                age=age,
                gender=gender,
                salary=salary,
                experience=experience,
                password=password  # Store the password as is, no need to hash
            )
            trainer.save()
            context['success'] = "Trainer registered successfully"
            

        return render(request, 'trainerregister.html', context)
    


from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import check_password 

def trainerlogin(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:
            try:
                trainer = Trainer.objects.get(emailid=email)
                
                # Check if the provided password matches the stored password
                if password == trainer.password:
                    # Authentication successful, set a session variable to indicate login
                    request.session['trainer_authenticated'] = True
                    request.session['trainer_id'] = trainer.id
                    context['success'] = "Login successful"
                    return redirect('/')
                else:
                    context['error'] = "Invalid credentials"
            except Trainer.DoesNotExist:
                context['error'] = "Invalid credentials"
        else:
            context['error'] = "Please fill all the fields"
    
    return render(request, 'trainerlogin.html', context)


def trainer_logout(request):
    # Clear the session variables related to trainer authentication
    request.session.pop('trainer_authenticated', None)
    request.session.pop('trainer_id', None)
    return redirect('/')  # Redirect to home page or any desired URL after logout

