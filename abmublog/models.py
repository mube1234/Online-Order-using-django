from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='userprofile')
    image=models.ImageField(null=True,blank=True,default="male2.png")
    address = models.CharField(null=True,blank=True, max_length=100)
    gender = models.CharField(null=True,blank=True, max_length=100,choices=(('male', 'male'), ('female', 'female')))
    phone = models.IntegerField(null=True,blank=True,)

    def __str__(self):
        return self.user.username+ "Profile "

class Product(models.Model):
    name=models.CharField(max_length=100,unique=True)
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Customer(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField(null=True)
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200, null=True,choices=STATUS,default='Pending')
    date_created=models.DateTimeField(auto_now_add=True)
class MakeOrder(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.ForeignKey(Product,on_delete=models.CASCADE,max_length=200,null=True)
    title=models.CharField(max_length=200,unique=True)
    image=models.ImageField()
    date_posted = models.DateTimeField(auto_now_add=True)
    #blog_views=models.IntegerField(default=0)
    def __str__(self):
        return self.author.username
class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' by ' + self.user.username
