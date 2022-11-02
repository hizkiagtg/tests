from django.forms import ModelForm
from tukarpoin.models import Voucher

class VoucherForm(ModelForm):
    class Meta:
        model = Voucher
        fields = ['vouchername','requiredpoin', 'available_voucher', 'voucherbody','area_required','expired_date']