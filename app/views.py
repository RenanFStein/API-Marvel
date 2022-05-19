from django.shortcuts import redirect, render
from .forms import Cadastro
from django.contrib.auth import authenticate, login
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, 'index.html')        
      


def cadastro_view(request):
    
    if request.method == "POST":   
        email= str(request.POST['email']).lower().strip()
        try:
            if User.objects.filter(email= email).exists :
                usuario=User.objects.create_user(username= str(request.POST['email']).lower().strip(),
                                                    first_name= str(request.POST['nome']).title().strip(),
                                                    email= str(request.POST['email']).lower().strip(),
                                                    password= request.POST['senha'])                
                
                print('Usuario cadastrado')
                return redirect( 'index')            

        except IntegrityError:
            print(f'Email {email} ja cadastrado')
            return redirect( 'index') 

    else:
        print('erro request')
        return redirect( 'index') 

def login(request):

    if request.method == 'POST':  
        username = str(request.POST['email']).lower().strip()

        password = request.POST['senha']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('logado')
            return redirect( 'home')
        
        else:
            print('email/senha invalido')
            return redirect( 'index')
    else:          
        return redirect( 'index')

  
def logout_view(request):
    logout(request)
    print('Loguot realizado')
    return redirect( 'index')
