from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST) #"request.POST" enables the form to validate the entered user data
        if form.is_valid(): #if it's not valid then it will be reloaded
            login(request,form.save()) #we have to pass "request" here because it associates the current user with the current session
            return redirect("posts:list") #after registration, we'll be directed to this page
    else:
        form=UserCreationForm() #this will be executed if our request is "GET"
    return render(request, "users/register.html", {"my_form": form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST) #to it simply: if we omit the "data" word then it won't remember the user. We don't use it in the "register_view" because when we register there's no data at all yet
        if form.is_valid(): #if it's not valid then it will be reloaded
            login(request,form.get_user()) #we have to pass "request" here because it associates the current user with the current session
            if "next" in request.POST: #it means that if there's the "next" word in our url then we'll be directed right to the word that preceded by "next". We have to add it, and because we haven't added it the "else" block will be executed
                return redirect(request.POST.get("next")) #this line of code requesting this "next" word. request.POST stores both the user data and url string!!!
            else:
                return redirect("posts:list")
    else:
        form=AuthenticationForm() #this will be executed if our request is "GET"
    return render(request, "users/login.html", {"my_form": form})

def logout_view(request):
    if request.method=="POST": #it means that a user clicks a button
        logout(request) #the logout process
        return redirect("posts:list")