from django import forms
from . import models

class CreatePost(forms.ModelForm): #we can't just pass the Meta class as our main because we can have several different forms for different classes and all they contain their own specific Meta class. And we can also create more nested classes after the Meta class
    class Meta: #this class is used to define metadata options such as "model" and "fields". It's like the right hand of our main class
        model=models.Post #it means that we assign the Post model
        fields=["title","body","slug","banner"] #it means that we grab these fields from the Post model

#this file defines the form for our website