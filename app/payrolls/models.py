# payrolls/models.py
from django.db import models
from companies.models import Company


class Payroll(models.Model):
    STATUS_CHOICES = [
        ("UPLOADED", "Uploaded"),
        ("PROCESSING", "Processing"),
        ("COMPLETED", "Completed"),
        ("ERROR", "Error"),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reference_month = models.IntegerField()
    reference_year = models.IntegerField()
    file = models.FileField(upload_to="payrolls/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="UPLOADED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.reference_month}/{self.reference_year}"
