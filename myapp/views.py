from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from . import models
from .utils import util
import pymongo
import os

client = pymongo.MongoClient('mongodb+srv://ramansain65:6zWguNNFWwDnczap@cluster0.hqv1bnv.mongodb.net/')
dbname = client['srib']
collection = dbname['floorplan']
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
        img_path=settings.MEDIA_ROOT + "/"+str(floorimage.image)
        data=util(image_path =img_path)
        if os.path.isfile(img_path):
            os.remove( img_path)
        floorplan={
            "username":str(username),
            "data":str(data),
            "name":str(name)
        }
        collection.insert_one(floorplan)

    return JsonResponse(data,safe=False)


    