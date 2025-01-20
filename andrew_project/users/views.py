from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def register_view(request): #it's all clear here to comprehend
    if request.method=="POST":
        form=UserCreationForm(request.POST) #we don't provide the "data" word in "registration" because it just doesn't exist yet. We haven't created our user yet
        if form.is_valid():
            login(request,form.save())
            return redirect("posts:lists")
    else:
        form=UserCreationForm()
    return render(request, "users/register.html", {"my_form": form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST) #if we emit the "data" word then it won't remember the user. Using "data" we ensure that the user stored in there
        if form.is_valid():
            login(request,form.get_user())
            if "next" in request.POST: #at the current moment it's not in "request.POST" so we will be redirected to "posts:lists"
                return redirect(request.POST.get("next"))
            else:
                return redirect("posts:lists")
    else:
        form=AuthenticationForm()
    return render(request, "users/login.html", {"my_form": form})

def logout_view(request): #it's all clear here to comprehend too!
    if request.method=="POST":
        logout(request)
        return redirect("posts:lists")