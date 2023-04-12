from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.price}"


class MyBook(Book):
    class Meta:
        proxy = True
        ordering = ["price"]
