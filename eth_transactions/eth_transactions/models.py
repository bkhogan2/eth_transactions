from django.db import models

class Transaction(models.Model):
    txhash = models.CharField(max_length=66)
    blockno = models.IntegerField()
    unixtimestamp = models.IntegerField()
    datetime_utc = models.DateTimeField()
    from_address = models.CharField(max_length=42)
    to_address = models.CharField(max_length=42)
    contractaddress = models.CharField(max_length=42, null=True, blank=True)
    value_in_eth = models.DecimalField(max_digits=20, decimal_places=10)
    value_out_eth = models.DecimalField(max_digits=20, decimal_places=10)
    current_value_usd = models.DecimalField(max_digits=20, decimal_places=2)
    fee_eth = models.DecimalField(max_digits=20, decimal_places=10)
    txnfee_usd = models.DecimalField(max_digits=20, decimal_places=20)
    historical_sprice_eth = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=10)
    errcode = models.CharField(max_length=10, null=True, blank=True)
    method = models.CharField(max_length=20)
