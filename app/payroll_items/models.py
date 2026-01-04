# payroll_items/models.py
from django.db import models
from employees.models import Employee


class PayrollItem(models.Model):
    ITEM_TYPE = [
        ("EARNING", "Earning"),
        ("DISCOUNT", "Discount"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="items")
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=ITEM_TYPE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.value}"
