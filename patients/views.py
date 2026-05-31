from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
from .ml_service import predict_health
from rest_framework import viewsets
from .serializers import PatientSerializer



def patient_list(request):
    patients = Patient.objects.all().order_by('-id')
    return render(request, 'patients/patient_list.html', {'patients': patients})


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)

            prediction = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            )
            patient.remarks = prediction
            patient.save()
            return redirect('patient_list')

    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form, 'title': 'Add Patient'})

def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            prediction = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            )
            patient.remarks = prediction
            patient.save()
            return redirect('patient_list')

    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form, 'title': 'Update Patient'})

def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('patient_list')





class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by("-id")
    serializer_class = PatientSerializer
    def perform_create(self, serializer):
        patient = serializer.save()

        try:
            prediction = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            )
            patient.remarks = prediction
            patient.save()
        except Exception as e:
            patient.remarks = f"Prediction Error: {str(e)}"
            patient.save()

    def perform_update(self, serializer):
        patient = serializer.save()

        try:
            prediction = predict_health(
                patient.glucose,
                patient.haemoglobin,
                patient.cholesterol
            )
            patient.remarks = prediction
            patient.save()
        except Exception as e:
            patient.remarks = f"Prediction Error: {str(e)}"
            patient.save()