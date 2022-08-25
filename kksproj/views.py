from http.client import HTTPResponse
from django.shortcuts import render
from .form import ImageForm
from .models import uploadImg

# Create your views here.


def index(request):
    return render(request, "index.html")


def create(request):
    return render(request, "create.html")

def text(request):
    return render(request, "text.html") 

def textedit(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request,"textedit.html",{"obj":obj})
    else:
            form = ImageForm()
    img = uploadImg.objects.all()
    return render(request,"textedit.html",{"img":img,"form":form})
        
