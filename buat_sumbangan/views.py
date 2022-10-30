from django.shortcuts import render
from buat_sumbangan import *
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from buat_sumbangan.models import *
from accounts.models import *

#harus import
@login_required
def add_donasi(request, id_bank):
    # Get user & bank sampah
    user = request.user
    bank_sampah = User.objects.get(id=id_bank)

    if(bank_sampah.is_regular):
        return HttpResponse(status=403)

    context = {
        'nama': bank_sampah.name
    }
    if user.is_regular:
        if request.method == "POST":
            
            tanggal_donasi = datetime.date.today()
            jenis_sampah = request.POST.get("jenis-sampah")
            berat_sampah = request.POST.get("berat")
            poin_sampah = count_point(jenis_sampah,int(berat_sampah))
            
            # Setter poin & berat ke modul user
            user.add_weight(int(berat_sampah)) 
            user.add_score(poin_sampah)

            # Membuat object Donasi Baru
            new_donasi = Donasi(
                donatur=user,
                date=tanggal_donasi,
                jenis=jenis_sampah,
                berat=berat_sampah,
                poin=poin_sampah,
                bank_sampah = bank_sampah.name,
            )

            new_donasi.save()
            user.save()

            return HttpResponse({"Berhasil": "Sampah telah disumbang!"}, status=200)
        
        return render(request, 'form_donasi_2.html', context)
    else:
        return HttpResponse("nunggu indri")

@login_required
def show_history(request):
    return render(request, 'history.html')

def donasi_json(request):
    user = request.user
    data = Donasi.objects.filter(donatur=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def count_point(jenis, berat):
    poin = 0
    if(jenis == "karung"):
        poin = berat * 1.2
    elif(jenis == "ban"):
        poin = berat * 1.5
    elif(jenis == "ember"):
        poin = berat * 1
    elif(jenis == "plastik"):
        poin = berat * 1
    elif(jenis == "logam"):
        poin = berat * 1.8
    elif(jenis == "botol"):
        poin = berat * 1
    return poin