from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/page2.html')

def login(request):
    if request.home == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')  # Redirect to the home page or dashboard
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

