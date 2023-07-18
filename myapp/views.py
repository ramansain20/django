from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from . import models
from .utils import util
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def upload(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        image = request.FILES["image"]
        floorimage = models.FloorImage(name=name,image=image,username=username)
        floorimage.save()
        data=util(image_path = settings.MEDIA_ROOT + "/"+str(floorimage.image))
        user=models.User(username=username,data=data)
        user.save()
        print(user)

    return JsonResponse(data,safe=False)


    