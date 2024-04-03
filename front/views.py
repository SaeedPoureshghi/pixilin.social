from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from api.models import User

# Create your views here.

def index(request):
    current_user = request.user

    if current_user.is_authenticated:
        return render(request, 'home/index.html', {'user': current_user})
    else:
        return HttpResponseRedirect('/login')

class LoginView(View):

    def get(self, request):
        return render(request, 'home/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'home/login.html', {'error': 'Please provide all required fields!'})
        
        user = authenticate(request , username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'home/login.html', {'error': 'Invalid credentials!'})

class SignupView(View):
        
        def get(self, request):
            return render(request, 'home/signup.html')
        
        def post(self, request):
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
    
            if not username or not email or not password:
                return render(request, 'home/signup.html', {'error': 'Please provide all required fields!'})
            
            if User.objects.filter(username=username).exists():
                return render(request, 'home/signup.html', {'error': 'Username is already taken!'})
            
            if User.objects.filter(email=email).exists():
                return render(request, 'home/signup.html', {'error': 'Email is already taken!'})
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
    
            return render(request, 'home/signup.html', {'message': 'User created successfully!'})
                
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')