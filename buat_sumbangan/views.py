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
#harus iimport

def add_donasi(request):
    if request.method == "POST":
        user = request.user
        tanggal_donasi = datetime.date.today()
        jenis_sampah = request.POST.get("jenis")
        berat_sampah = request.POST.get("berat")
        poin_sampah = count_point(jenis_sampah,berat_sampah)

        # Setter poin & berat ke modul user
        user.weight += berat
        user.score += poin

        # Membuat object Donasi Baru
        new_donasi = Donasi(
            #donatur=user,
            date=tanggal_donasi,
            jenis=jenis_sampah,
            berat=berat_sampah,
            poin=poin,
        )
        new_donasi.save()
        newDonasi = Donasi.objects.create()

        return JsonResponse({"instance": "Sampah telah disumbang!"}, status=200)
    
    return render(request, 'form_donasi_2.html')


def show_history(request):
    return render(request, 'history.html')

def donasi_json(request):
    user = request.user
    data = Donasi.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def count_point(jenis, berat):
    poin = 0;
    if(jenis == "karung"):
        poin = berat * 1.2
    elif(jenis == "ban"):
        poin = berat * 1.5
    elif(jenis == "ember"):
        poin = berat * 1
    elif(jenis == "plastik"):
        point = berat * 0.5
    elif(jenis == "logam"):
        poin = berat * 1.8
    elif(jenis == "botol"):
        poin = berat * 0.4
    return poin