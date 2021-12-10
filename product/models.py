from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name

class Seller(models.Model):
    seller_name = models.CharField(max_length=50)    

    def __str__(self):
        return self.seller_name


class Product(models.Model):    
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product_origin = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=30)
    product_purchase_price = models.IntegerField()
    product_selling_price = models.IntegerField()

    
