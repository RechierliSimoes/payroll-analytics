from django.contrib import admin
from .models import Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ("company", "reference_month", "reference_year", "status", "created_at")
    list_filter = ("status", "reference_year")
    search_fields = ("company__name",)
