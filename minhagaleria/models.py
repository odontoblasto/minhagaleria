from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class CategoryModel(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    category_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.category_name


class PhotoModel(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category_name = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return str(self.category_name) + str(self.description)



class ProfileModel(models.Model):


    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    data_nascimento= models.DateField(null=True)
    foto = models.ImageField(null=True,blank=True,upload_to='images/profile')
   

    def __str__(self):
        return str(self.user_name) 

    def get_absolute_url(self):
        return reverse('home')