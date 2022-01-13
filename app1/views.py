from django.shortcuts import render
from . models import *
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
    client = user_image.objects.all()
    
    # print(client.image)

    return render(request , "home.html" , {"data": client})

def save_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        file = request.FILES.get('file')
        fss  = FileSystemStorage()
        print(file ,name)
        file_name = fss.save(file.name ,file )

        url = fss.url(file_name)
        user_image.objects.create(image = url , user_name = name)
        # print(request.FILES)
        print(name )
            # client_data = user_image(user_name = name   )
            # client_data.save()
            # print(client_data.image)
        x = user_image.objects.values()
        client = list(x)
        return JsonResponse({"link":url  ,  "client_data": client})
    else:
        return JsonResponse({"status":0})
        
