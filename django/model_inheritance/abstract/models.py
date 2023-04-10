from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Student(Human):
    score = models.IntegerField()


class Teacher(Human):
    salary = models.IntegerField()
