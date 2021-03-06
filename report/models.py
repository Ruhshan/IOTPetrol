from django.db import models

# Create your models here.


class Sale(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    sold_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quantity)