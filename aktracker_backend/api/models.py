from django.db import models

# Create your models here.
# , blank=True, null=True

# class Contact(models.Model):
#     pass

class Client(models.Model):
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    moveFrom = models.CharField(max_length=100)
    moveTo = models.CharField(max_length=100)


class Partner(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='details')
    city = models.CharField(max_length=100)
    rantal = models.CharField(max_length=100)
    seeUs = models.CharField(max_length=100)