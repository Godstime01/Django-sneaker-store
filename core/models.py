from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='product_image')
    slug = models.SlugField(null = True)
    in_stock = models.BooleanField(default=True)
    brand = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse('product', kwargs={
            'slug': self.slug
        })



class Order(models.Model):
    """user create order when user proceed with checkout"""

    STATUS = (
        ('pending', 'pending'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered')
    )

    user = None
    status = models.CharField(max_length=30, choices = STATUS)
    order_date = models.DateTimeField(auto_now_add = True)
    
class OrderItem(models.Model):
    
    order_id = models.ForeignKey(Order, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()

