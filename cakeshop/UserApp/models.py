from django.db import models
from AdminApp.models import UserInfo,Product
# Create your models here.
class MyCart(models.Model):
    user=models.ForeignKey(to='AdminApp.UserInfo', on_delete=models.CASCADE)
    cake=models.ForeignKey(to='AdminApp.Product',on_delete=models.CASCADE)
    qty=models.IntegerField()

    class Meta:
        db_table= "MyCart"
