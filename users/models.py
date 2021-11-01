from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

from django.db.models.deletion import SET_NULL
# Create your models here.

class Candidate(models.Model):
    user     = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    name     =  models.CharField(max_length=200)
    position =  models.CharField(max_length=200,null=True,blank=True)
    office   =  models.CharField(max_length=200,null=True,blank=True)
    age      =  models.IntegerField(null=True,blank=True)
    salary   =  models.IntegerField(null=True,blank=True)
    created  =  models.DateTimeField(auto_now_add=True)
    id       =  models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):

        return self.name

