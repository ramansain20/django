from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from . import models
from .utils import util
import json
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def upload(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES["image"]
        floorimage = models.FloorImage(name=name,image=image)
        floorimage.save()
        coordinates=util(image_path = settings.MEDIA_ROOT + "/"+str(floorimage.image) )
    return JsonResponse(coordinates,safe=False)


    