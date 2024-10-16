from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

# web/views.py
from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import Donation

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_success')  # Redirige a una página de éxito
    else:
        form = DonationForm()
    
    return render(request, 'donaciones.html', {'form': form})

def donation_success(request):
    return render(request, 'donation_success.html')


from django.contrib.auth import authenticate, login



from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})  # Aquí no cambies 'login.html'




from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'dashboard.html', {'projects': projects})



from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'dashboard.html', {'projects': projects, 'form': ProjectForm()})

def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirigir al dashboard después de subir
    else:
        form = ProjectForm()
    return render(request, 'upload_project.html', {'form': form})

def manage_projects(request):
    projects = Project.objects.all()  # Obtén todos los proyectos
    return render(request, 'manage_projects.html', {'projects': projects})


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')