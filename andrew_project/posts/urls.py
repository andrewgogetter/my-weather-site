from django.urls import path
from . import views

app_name="posts" #setting up the name helps us to easily orient ourselves in our project. Eg referencing like "posts: lists" instead just "lists" so we have a clear understanding what's going on

urlpatterns = [
    path("", views.posts_list, name="lists"), #we use the name variable for better orientation in the code, readability and template usage. If we change the url name here then there's no need to update it in the other parts of our code because we use the name variable
    path("new-post/", views.post_new, name="new-post"),
    path("<slug:slug>", views.post_page, name="page"), #the second slug is the name variable
]