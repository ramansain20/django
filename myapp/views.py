from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from . import models
from .utils import util
# Create your views here.
def index(request):
    
    return render(request,"index.html")

def upload(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES["image"]
        floorimage = models.FloorImage(name=name,image=image)
        floorimage.save()
        return redirect("/data")
    return render(request,"upload.html")


def data(request):
    
    coordinates=util(image_path = settings.MEDIA_ROOT + "/uploads/PNG.png" )
    return render(request,"data.html",{"coordinates":coordinates})

    