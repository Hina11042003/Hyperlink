from django.shortcuts import render, redirect
from core.forms import Register, SignUpForm
from core.models import profile
from django.contrib.auth import login

def home(req):
    return render(req, 'student/home.html')

def about(req):
    return render(req, 'student/about.html')


def registration(request):
    if request.method == 'POST':
        fm = Register(request.POST)
        print("Submitting form")
        if fm.is_valid():
            print("form is valid")
            full_name = fm.cleaned_data['full_name']
            email     = fm.cleaned_data['email']
            password  = fm.cleaned_data['password']
            gender    = fm.cleaned_data['gender']
            skills    = ', '.join(fm.cleaned_data['skills'])  # list → string
            agree     = fm.cleaned_data['agree']
            dob       = fm.cleaned_data['dob']

            # Save data into Database 
            user=profile(full_name=full_name,  email=  email , password= password, gender= gender, skills = skills ,  agree =  agree ,dob=dob)
            user.save()
            return redirect('/success/')  
    else:
        fm = Register()
    return render(request, 'student/Registration.html', {'form': fm})

def success(request):
    return render(request,'student/success.html')

def all_profile(request):
    profiles = profile.objects.all()   
    return render(request, 'student/all_profiles.html', {'profiles': profiles})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'student/signup.html', {'form': form})