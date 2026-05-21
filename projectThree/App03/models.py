from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    mobile = models.IntegerField()
    dob = models.DateField()
    STATUS_CHOICES = [
        ('f', 'female'),
        ('m', 'male'),
    ]
    Gender = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
    )
    def __str__(self):
        return self.name

class employee2(models.Model):
    name = models.CharField(max_length=100,)
    age = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    dob = models.DateField()
    STATUS_CHOICES = [
        ('f', 'female'),
        ('m', 'male'),
    ]
    Gender = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,)

    def __str__(self):
        return self.name