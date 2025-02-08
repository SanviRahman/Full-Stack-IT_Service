from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Services(models.Model):
    image= models.ImageField(upload_to='image/',blank=True,null=True)
    title= models.CharField(max_length=200,blank=True,null=True)
    sub_title=models.CharField(max_length=200,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',blank=True,null=True)


    def __str__(self):
        return self.title
    
