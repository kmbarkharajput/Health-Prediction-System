from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'dob', 'email', 'glucose', 'haemoglobin', 'cholesterol', 'remarks']

search_fields = (
    'full_name', 'email'
)