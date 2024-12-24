from string import printable
from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=100 ,null=True, blank=True)
    password = models.CharField(max_length=100 ,null=True, blank=True)
    Type=models.CharField(max_length=100 ,null=True, blank=True)

class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name=models.CharField(max_length=100 ,null=True, blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=100 , null=True,blank=True)
    email=models.CharField(max_length=100, null=True,blank=True)
    address=models.CharField(max_length=100, null=True,blank=True)
    phoneno=models.CharField(max_length=250,null=True,blank=True)

class turf(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)   
    phone=models.BigIntegerField(null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True) 
    email=models.CharField(max_length=100,null=True,blank=True)
    rent=models.CharField(max_length=100,null=True,blank=True)
    image=models.FileField(upload_to='turf',null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    opentime=models.CharField(max_length=100,null=True,blank=True)
    closingtime=models.CharField(max_length=100,null=True,blank=True)
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

class Log(models.Model):
    action = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    instance_id = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

@receiver(post_save)
def log_addition(sender, instance, created, **kwargs):
    if created:
        Log.objects.create(action='Added', model=sender.__name__, instance_id=instance.id)

@receiver(post_delete)
def log_deletion(sender, instance, **kwargs):
    Log.objects.create(action='Deleted', model=sender.__name__, instance_id=instance.id)

class ComplaintTable(models.Model):
    complaint=models.CharField(max_length=100,null=True,blank=True)   
    reply=models.CharField(max_length=100,null=True,blank=True) 
    date=models.CharField(max_length=100,null=True,blank=True)
    USER=models.ForeignKey(UserTable,on_delete=models.CASCADE)

class slot(models.Model):
    turfid=models.ForeignKey(turf, on_delete=models.CASCADE,null=True,blank=True)
    timeslot=models.CharField(max_length=1000,null=True ,blank=True)
    status=models.CharField(max_length=50,default=False)
    is_active =models.BooleanField(default=True, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class bookingtable(models.Model):
    SLOT=models.ForeignKey(slot,on_delete=models.CASCADE)    
    USER=models.ForeignKey(LoginTable,on_delete=models.CASCADE)
    DATE=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)


class EquipmentTable(models.Model):
    TURF = models.ForeignKey(turf, on_delete=models.CASCADE,null=True,blank=True)
    equipment=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.FloatField(null=True,blank=True) 
    description=models.CharField(max_length=100,null=True,blank=True) 

class RequestTable(models.Model):
    USER=models.ForeignKey(LoginTable,on_delete=models.CASCADE)   
    DATE=models.DateField(null=True,blank=True)
    STATUS=models.CharField(max_length=250,default=True,null=True,blank=True)
    EQUIPMENT=models.ForeignKey(EquipmentTable,on_delete=models.CASCADE)


class RatingTable(models.Model):
    rating=models.FloatField(null=True,blank=True)
    review=models.CharField(max_length=100,null=True,blank=True)   
    USER=models.ForeignKey(LoginTable,on_delete=models.CASCADE)  
    turf=models.ForeignKey(turf,on_delete=models.CASCADE)




