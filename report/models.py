from django.db import models

# Create your models here.


class Report(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    time_ = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.quantity)