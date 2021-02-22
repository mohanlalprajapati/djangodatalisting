from django.db import models

# Create your models here.
class Category(models.Model):
    name =  models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
