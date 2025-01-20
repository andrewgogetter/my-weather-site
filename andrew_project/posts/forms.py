from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model=models.Post #it specifies the form will be used to create or update instances of the "Post" model
        fields=["title","body","slug","banner"] #it means that these fields from the "Post" model will be included in our form

#the actual "form" is just a field where a user can enter text, etc.