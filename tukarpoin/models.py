from datetime import datetime
from email.policy import default
from django.db import models
from accounts.models import *
import datetime

class Voucher(models.Model):
    voucherbank = models.ForeignKey(User,on_delete=models.CASCADE, related_name="voucher_bank")
    vouchername = models.TextField(null=False, max_length=50)
    voucherbody = models.TextField(null=False, max_length=100)
    requiredpoin = models.IntegerField(default=0)
    redeemed = models.IntegerField(default=0)
    is_redeemed = models.BooleanField(default=False)
    area_required = models.TextField(default="")
    expired_date = models.DateField(default=datetime.date.today)
    available_voucher = models.IntegerField(default=0)
