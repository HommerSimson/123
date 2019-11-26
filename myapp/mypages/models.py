from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    discount = models.BooleanField()
    description = models.TextField(default=None)

    def str(self):
        return self.name



