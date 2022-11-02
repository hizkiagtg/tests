from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tukarpoin.forms import VoucherForm
from tukarpoin.models import Voucher
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from accounts.models import User

@login_required
def tukarpoin(request):
    if (request.user.is_authenticated):
        vouchers = Voucher.objects.order_by('is_redeemed', 'expired_date')
        context = { 
            'last_login': request.COOKIES.get('last_login'),
            'vouchers': vouchers, 
            'num_voucher': len(vouchers),
            'user_poin': User.score,
        }
    return render(request, "tukarpoin.html", context)

@login_required
def createvoucher(request):
    if (request.user.is_authenticated):
        user = request.user
        form = VoucherForm(request.POST or None)
        if (form.is_valid()):
            vouchername = form.cleaned_data.get('vouchername')
            requiredpoin = form.cleaned_data.get('requiredpoin')
            available_voucher = form.cleaned_data.get('available_voucher')
            voucherbody = form.cleaned_data.get('voucherbody')
            area_required = form.cleaned_data.get('area_required')
            expired_date = form.cleaned_data.get('expired_date')
            voucher = Voucher.objects.create(vouchername=vouchername, requiredpoin=requiredpoin, available_voucher=available_voucher, voucherbody=voucherbody, area_required=area_required, expired_date=expired_date, user=user)
            return JsonResponse({
                'pk': voucher.pk,
                'voucherbank': user,
                'vouchername': vouchername,
                'voucherbody': voucherbody,
                'requiredpoin': requiredpoin,
                'is_redeemed': voucher.is_redeemed,
                'area_required': area_required,
                'expired_date': expired_date,
            })

@login_required
def addvoucher(request):
    context = { 'last_login': request.COOKIES.get('last_login') }
    return render(request, "addvoucher.html", context)

@login_required
def get_json():
    all_voucher = Voucher.objects.all()
    return HttpResponse(serializers.serialize('json',all_voucher), content_type='application/json')

@login_required
def myvoucher(request):
    if (request.user.is_authenticated):
        vouchers = Voucher.objects.filter(Voucher.is_redeemed==True)
        context = { 
            'last_login': request.COOKIES.get('last_login'),
            'vouchers': vouchers, 
            'num_voucher': len(vouchers),
        }
    return render(request, "myvoucher.html", context)

@login_required
def redeem(request, id):
    voucher = Voucher.objects.get(pk=id)
    if (voucher.user==request.user):
        voucher.is_redeemed = not voucher.is_redeemed
        voucher.available_voucher = voucher.available_voucher-1
        voucher.save()
        return HttpResponseRedirect(reverse('tukarpoin:tukarpoin'))