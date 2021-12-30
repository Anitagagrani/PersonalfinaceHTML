from django.db import models

# Create your models here.
class debt_item(models.Model):
    debt_name = models.CharField(max_length=50)
    debt_balance = models.FloatField(default=0)
    debt_interest_rate = models.FloatField(default=0.0)
    def __str__(self):
        return self.debt_name