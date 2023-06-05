from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, "backend/login_register.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if username == "":
            messages.info(request, "Please fill in a username")
            return redirect("member")
        elif email == "":
            messages.info(request, "Please fill in an email address")
            return redirect("member")
        elif password == "":
            messages.info(request, "Please fill in a password")
            return redirect("member")
        elif repassword == "":
            messages.info(request, "Please fill in a repassord")
            return redirect("member")    
        elif password == repassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, "User has already existed, use another name")
                return redirect("member")
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email has already existed, use another address")
                return redirect("member")
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password=password
                )
                user.save()
                messages.info(request, "Account is created successfully")
                return redirect("member")
        else:
            messages.info(request, "Cannot register please enter the same password")
            return redirect("member")   

        # if username == "" and email == "" and password == "" and repassword == "":
        #     messages.info(request, "Please fill in all infomation ")
        #     return redirect("member")
        
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    
    # check data if existed on DB
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect("panel")
    else:
        messages.info(request, "We cannot find the account")
        return redirect("member") 
    
def logout(request):
    auth.logout(request)
    return redirect('member')