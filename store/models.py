
from django.db import models
from django.contrib.auth.models import User

#Category
class Category(models.Model):
    name=models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.size

class Color(models.Model):
    color = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.color


#product

class Product(models.Model):
    title=models.CharField(max_length=30)
    tag=models.CharField(max_length=25,null=True,blank=True)
    description=models.CharField(max_length=250)
    price=models.IntegerField()
    image=models.ImageField(upload_to='image/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.ManyToManyField(Color, null=True, blank=True)
    size = models.ManyToManyField(Size, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username

    
class AddtoCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username



class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=60,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=250)
    pin=models.IntegerField(null=True,blank=True)
    dist=models.CharField(max_length=25)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.address





class Order(models.Model):

    status = (
        ("Created", "Created"),
        ("Paid", "Paid"),
        ("Pending", "Pending"),
        ("Failed", "Failed"),
        ("Delivered", "Delivered"),
        ("Shipped", "Shipped"),
    )

    payment_type = (
        ("COD", "COD"),
        ("Onlie", "Online"),
    )

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    status = models.CharField(choices=status, default='Created', max_length=55)
    payment_type = models.CharField(choices=payment_type, default='COD', max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)