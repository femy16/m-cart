from django.db import models

# Create your models here.

class ProductCategories(models.Model):
    categories=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.categories
        
        
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    brand = models.CharField(max_length=50, default='')
    sku = models.CharField(max_length=50, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    color = models.CharField(max_length=50, default='blue')
    productcategories=models.ForeignKey(ProductCategories,related_name="products",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
        
class ProductImage(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, related_name='images', null=False, on_delete=models.CASCADE) 
    

    


    
