from django.db import models

class acc(models.Model):
    username=models.CharField(max_length=50)
    accountnumber=models.IntegerField(null=True)
    phone=models.IntegerField(unique=True)
    amount=models.IntegerField(null=True)


class transcation(models.Model):
    from_phone = models.IntegerField(null=True)
    to_phone = models.IntegerField(null=True)
    t_amount = models.IntegerField(null=True)
    dt = models.CharField(max_length=30)

