from django.shortcuts import render
from . models import *
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import json
# Create your views here.
def home(request):
    client = user_image.objects.all()
    
    # print(client.image)

    return render(request , "home.html" , {"data": client})

def save_data(request):
    print(request.POST)
    print(request.FILES)
    if request.method == "POST":
        name = request.POST.get('name')
        fname = request.POST.get('file_name')
        file = request.FILES.get('file')
        fss  = FileSystemStorage()
        # jfile=json.dumps(file)
        # print(jfile)
        print(file ,name)
        file_name = fss.save(file.name, file)
        print(file_name,'file_name')
        url = fss.url(file_name)
        # print(url)
        user_image.objects.create(image = url , user_name = name)
        # print(request.FILES)
        print(name )
            # client_data = user_image(user_name = name   )
            # client_data.save()
            # print(client_data.image)
        x = user_image.objects.values()
        client = list(x)
        return JsonResponse({"client_data": client})
    else:
        return JsonResponse({"status":0})
        
