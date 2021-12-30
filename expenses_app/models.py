from django.db import models

# Create your models here.
class expenses_item(models.Model):
    expense_name = models.CharField(max_length=50)
    due_date = models.PositiveSmallIntegerField(default=1)
    expense_amount = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.expense_name