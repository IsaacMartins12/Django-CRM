from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request) :
    
    #Check to see if logging in 
    
    if request.method == 'POST' :
        print("Entrei no post")
        username = request.POST['username']
        password = request.POST['password']
        
        #Authenticate
        
        user = authenticate(request, username=username, password=password)
      
        if user is not None :
            login(request,user)
            messages.success(request,"You Have Been Logged In !")
            return redirect('home')
        
        else :
            messages.success(request,"There Was An Error Logging In, Please try again ...")
            return redirect('home')
    
    else :
        print(messages.get_messages)
        return render(request, 'home.html', {})

def logout_user(request) :
    pass 