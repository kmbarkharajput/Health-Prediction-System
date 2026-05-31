from django import forms 
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name', 'dob', 'email', 'glucose', 'haemoglobin', 'cholesterol']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Name'
                }
           ),
           'dob': forms.DateInput(attrs={
               'class': 'form-control',
               'type': 'date'
           }),
           'email': forms.EmailInput(attrs={
               'class': 'form-control',
               'type': 'Enter Email'
           }),
           'glucose': forms.NumberInput(attrs={
               'class': 'form-control',
               'type': 'Enter Glucose'
           }),
           'haemoglobin': forms.NumberInput(attrs={
               'class': 'form-control',
               'type': 'Enter Haemoglobin'
           }),
           'cholesterol': forms.NumberInput(attrs={
               'class': 'form-control',
               'type': 'Enter Cholesterol'
           }),

        }


    def clean_glucose(self):
        glucose = self.cleaned_data['glucose']

        if glucose < 0:
            raise forms.ValidationError(
                "Glucose cannot be negative."
            ) 
        return glucose
    def clean_haemoglobin(self):
        haemoglobin = self.cleaned_data['haemoglobin']

        if haemoglobin < 0:
            raise forms.ValidationError(
                "Haemoglobin cannot be negative."
            ) 
        return haemoglobin
    def clean_cholesterol(self):
        cholesterol = self.cleaned_data['cholesterol']

        if cholesterol < 0:
            raise forms.ValidationError(
                "Cholesterol cannot be negative."
            ) 
        return cholesterol
       