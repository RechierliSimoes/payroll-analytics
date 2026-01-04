# employees/models.py
from django.db import models
from payrolls.models import Payroll


class Employee(models.Model):
    payroll = models.ForeignKey(Payroll, on_delete=models.CASCADE, related_name="employees")
    registration = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    cost_center = models.CharField(max_length=100)

    def __str__(self):
        return self.name
