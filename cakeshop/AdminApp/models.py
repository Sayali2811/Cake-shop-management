from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    pname = models.CharField(max_length=20)
    price = models.FloatField(default=200)
    description = models.CharField(max_length=50)
    size = models.FloatField(default=1)
    quantity = models.IntegerField()
    image = models.ImageField(default='abc.jpg', upload_to='Images')
    cat = models.ForeignKey(to='Category', on_delete=models.CASCADE)

    class Meta:
        db_table = "Product"


class UserInfo(models.Model):
    uname = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length = 100)

    class Meta:
        db_table = 'UserInfo'
