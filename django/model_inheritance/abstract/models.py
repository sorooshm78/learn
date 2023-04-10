from django.db import models


# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Student(Human):
    score = models.IntegerField()


class Teacher(Human):
    salary = models.IntegerField()
