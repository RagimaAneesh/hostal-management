from django.contrib.auth.models import AbstractUser
from django.db import models

class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

class Student(models.Model):
    user =models.OneToOneField(Login,on_delete=models.CASCADE,related_name='student')
    name = models.CharField(max_length=39)
    profile_picture = models.FileField(upload_to='profilepic/')
    phone_no = models.CharField(max_length=38)
    address = models.TextField(max_length=100)
    email = models.EmailField()

class Parent(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='parent')
    student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    phone_no =models.CharField(max_length=38)

class Food(models.Model):
    cat = (('dosa','dosa'),('idali','idali'),('chappathi','chappathi'))
    cat1 =(('meals','meals'),('biriyani','biriyani'))
    cat2 = (('meals', 'meals'), ('biriyani', 'biriyani'),('chappathi','chappathi'))
    breakfast = models.CharField(max_length=100,choices=cat)
    lunch = models.CharField(max_length=100,choices=cat1)
    dinner = models.CharField(max_length=200,choices=cat2)

class Fee(models.Model):
    sl_no = models.CharField(max_length=50)
    particulers = models.CharField(max_length=400)
    amount_in_rs = models.CharField(max_length=50)

class Notification(models.Model):
    date = models.DateField(auto_now=True)
    notification = models.TextField(max_length=200)

class Studentcomplaint(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    complaint = models.TextField(max_length=500)
    reply =models.TextField(max_length=500)

class Feedback(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date = models.DateField()
    feedback = models.TextField(max_length=500)

class Attendence(models.Model):
    student = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    date = models.DateField()
    attendence =models.CharField(max_length=200)
    time = models.TimeField()

class Hostal_De(models.Model):
    date = models.DateField(auto_now=True)
    Details= models.TextField(max_length=500)












