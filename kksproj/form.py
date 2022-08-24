from dataclasses import fields
from tkinter import Image
from django import forms 
from .models import uploadImg

class ImageForm(forms.ModelForm):
    class Meta:
        model = uploadImg
        fields=("caption","image")