from django.urls import path
from . import views

app_name="posts" #we use this name to reference to it in our templates

urlpatterns = [
    path("", views.posts_list, name="list"), #it's useful for our sub-url structure. Also, we can refer to it using the "{ url }" structure. Which makes it easier and more readable. It's very useful when we got several apps with the same urls but for each of them we have their own unique names
    path("new-post/", views.post_new, name="new-post"),
    path("<slug:slug>", views.post_page, name="page"), #first slug is a type, the second is a variable that stored in the Post model
]