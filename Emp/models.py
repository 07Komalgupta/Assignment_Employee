from django.db import models

# Create your models here.

class employees(models.Model):
    emp_id = models.IntegerField()
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField(max_length=40)


    def __str__(self):
        return self.firstname + " " + self.lastname