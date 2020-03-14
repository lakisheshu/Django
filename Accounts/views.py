from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST["Fisrt_name"]
        last_name=request.POST["Last Name"]
        username=request.POST["username"]
        email=request.POST["Email"]
        password=request.POST["password"]
        cnfm_password=request.POST["confirm password"]
        if password==cnfm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exists")
                print("username is alredy exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"eamil is taken ")
                print("All ready registerd")
                return redirect("register")
            else:
                # to send the data  to database first create user
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                # to save the user details in db use the following
                user.save();
                print("user added successfully")
                return redirect("login")
        else:
            messages.info(request,"password is not matched")
            # to get back to user page
            return redirect('register')
    else:
        return render(request,'register.html')