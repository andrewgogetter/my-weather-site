from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def posts_list(request):
    posts=Post.objects.all().order_by("-date")
    return render(request, "posts/posts_list.html", {"my_posts": posts}) #the second "posts" the same as "posts=Post.objects.all().order_by("-date")". It means that "my_posts" contains exactly this value


def post_page(request,slug):
    post = Post.objects.get(slug=slug) #slug in parentheses tells to treat this line of the code as slug
    return render(request, "posts/post_page.html", {"my_post": post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method=="POST": #it means that a user already visited the site
        form=forms.CreatePost(request.POST,request.FILES) #it offers a user to create their own post based on previous experience. "request.Post" means data and "request.FILES" means files
        if form.is_valid(): #if not it will reload the current page
            newpost=form.save(commit=False) #we set it false because we need to apply our user to our author uet
            newpost.author=request.user #we assign our user to the author
            newpost.save() #finally we fully save it
            return redirect("posts:list") #now we're on the page with the posts list
    else:
        form=forms.CreatePost() #this form for the "GET" request which means when we first. GET request can be like for non-registered users as well as for the registered ones that fill in their very first form whereas the POST request always about registered users or non-registered users that fill in their second form on the site without existing it after the first one was filled in
    return render(request, "posts/post_new.html", {"my_form": form})