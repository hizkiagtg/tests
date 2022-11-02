from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from descriptions.models import *

# Create your views here.
def desc_json(request):
    desc = Description.objects.all()
    return JsonResponse(list(desc.values()), safe=False)

def show_details(request, id):
    accessor = request.user
    info = User.objects.get(id=id)
    desc = Description.objects.filter(waste_bank_id=id)
    context = {
        'id': id,
        'accessor': accessor,
        'info': info,
        'desc': desc,
    }
    return render(request, 'details.html', context)

def upload_desc(request):
    # if request.method == "POST":
    #     waste_bank = request.user
    #     title = request.POST.get("title")
    #     date = request.POST.get("date")
    #     image = request.FILES.get("image")
    #     description = request.POST.get("description")

    #     desc = Description(waste_bank=waste_bank, title=title, date=date, image=image, description=description)
    #     desc.save()

    #     return HttpResponse(b"CREATED", status=201)
    
    # return HttpResponseNotFound()

    form = UploadDesc()

    if request.method == "POST":
        form = UploadDesc(request.POST, request.FILES)
        if form.is_valid():
            form.instance.waste_bank = request.user
            form.save()
    
    context = {'form':form}
    return render(request, 'upload.html', context)