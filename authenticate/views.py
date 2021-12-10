from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
class IndexView(View):
    def get(self, request):      
        return HttpResponse('hello')
                

class RegisterView(View):
    def get(self, request):
        if request.resolver_match.url_name == 'register_url':
            return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'username already taken'})

        elif User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'email already taken'})

        elif len(password1) < 4:
            return render(request, 'register.html', {'error': 'Your password is too short'})

        elif password1 != password2:
            return render(request, 'register.html', {'error': 'Your password is not match'})
        
        else:
            user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)        
            user.save()
            return redirect('authenticate:login_url')

class LoginView(View):
    def get(self, request):
        if request.resolver_match.url_name == 'login_url':            
            if request.user.is_authenticated:
                return redirect('authenticate:index_url')
            else:
                return render(request, 'login.html')

    
    def post(self, request):
        if request.resolver_match.url_name == 'login_url':

            username = request.POST['username'].strip()
            password = request.POST['password'].strip()

            try:
                user_obj = User.objects.get(username=username)

            except Exception as e:
                return render(request, 'login.html', {'error': 'Your username is invalid. please correct your username'})                
            
            if user_obj.check_password(password):                
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('authenticate:index_url')                   
            else:
                return render(request, 'login.html', {'error': 'Your password is invalid. please correct your password'})                



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('authenticate:login_url')
