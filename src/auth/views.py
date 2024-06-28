from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request,"auth/login.html",{})


#def RegisterView(request):
   # return render(request,"auth/login.html",{})


# Create your views here.
