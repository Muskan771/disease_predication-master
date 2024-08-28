# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

# Define a view function for the home page
def home(request):
	return render(request, 'myapp/index.html')

def about(request):
	return render(request, 'myapp/about.html')

def service(request):
      return render(request, 'myapp/service.html')

def symp(request):
      return render(request, 'myapp/symptom_checker.html')

# Define a view function for the login page
def login(request):
    # Check if the HTTP request method is POST (form submission)
    print(request.POST)
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
             
        
        user_data = User.objects.filter(username=username)
        print(user_data)
        # Check if a user with the provided username exists
        if not user_data:
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            print("user not found")
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('')
        else:
            # Log in the user and redirect to the home page upon successful login
            #login(request, user)
            return redirect('/about/')

    # Render the login page template (GET request)
    return render(request, 'myapp/index.html')

# Define a view function for the registration page
def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('/register/')
	
	# Render the registration page template (GET request)
	return render(request, 'register.html')
