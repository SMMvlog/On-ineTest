from django.db import models

# Create your models here.

class CreateTest(models.Model):
    Question = models.CharField(max_length=50)
    a = models.CharField(max_length=30)
    b = models.CharField(max_length=30)
    c = models.CharField(max_length=30)
    d = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.Question +": "+ "option a is "+self.a+", "+ "option b is "+self.b+", "+ "option c is "+self.c+", "+ "option d is "+self.d



class StudentModel(models.Model):
    Question = models.ForeignKey(CreateTest,on_delete=models.CASCADE)
    Ans = models.CharField(max_length=30)
    