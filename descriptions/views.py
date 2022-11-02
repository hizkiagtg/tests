from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from descriptions.models import *
from descriptions.forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def desc_json(request):
    desc = Description.objects.all()
    return JsonResponse(list(desc.values()), safe=False)

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def show_upload_form(request):
    if(request.user.is_bank):
        form = UploadDesc()

        context = {'form':form}
        return render(request, 'upload.html', context)
    else:
        return HttpResponseNotFound(status=403)

@login_required(login_url='/accounts/login/')
def upload_desc(request):
    if request.method == "POST":
        waste_bank = request.user
        title = request.POST.get("title")
        date = request.POST.get("date")
        image = request.FILES.get("image")
        description = request.POST.get("description")

        desc = Description(waste_bank=waste_bank, title=title, date=date, image=image, description=description)
        desc.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()