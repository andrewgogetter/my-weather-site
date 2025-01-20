from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def posts_list(request):
    posts=Post.objects.all().order_by("-date")
    return render(request, "posts/posts_list.html", {"my_posts": posts}) #we need to use the "{"my_posts": posts}" expression to be able to pass the dynamic data in our templates. If we change the first "my_posts" then we have to change it in our templates too, because it's just a name. The second "posts" is "posts=Post.objects.all().order_by("-date")"


def post_page(request,slug):
    post = Post.objects.get(slug=slug) #it implies that the object that we're searching in the Post model has to be slug friendly field (eg contain hyphens, etc)
    return render(request, "posts/post_page.html", {"my_post": post})

@login_required(login_url="/users/login/") #it means that a user has to be logged in to make a post. If they are not logged in then they will be redirected to this url
def post_new(request):
    if request.method=="POST": #"POST" here is a special word that defines the request method
        form=forms.CreatePost(request.POST,request.FILES) #request.POST contains the data from previous entries and request.POST do the same only for the files
        if form.is_valid(): #if the form invalid then the page will be reloaded
            newpost=form.save(commit=False) #it means that we want to proceed
            newpost.author=request.user #this line associates the new post with the current user. Without it the form will be saved in the database with no author name
            newpost.save() #saves to the database
            return redirect("posts:lists") #after successfully creating a new post we will be redirected to the posts page
    else:
        form=forms.CreatePost() #when a user first enters a site and decides to fill in a form then it's considered the GET request. But if he's already registered and decides to fill in the form then it's the POST request. This line of code implies the GET req
    return render(request, "posts/post_new.html", {"my_form": form})

#the GET request can be like for non-registered users as well as for the registered ones that fill in their very first form
#whereas the POST request always about registered users or non-registered users that fill in their second form on the site without existing it after the first one was filled in