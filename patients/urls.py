from rest_framework.routers import DefaultRouter
from django.urls import path, include
from patients import views
from .views import PatientViewSet

router = DefaultRouter()

router.register(r'patients', PatientViewSet, basename='patient-api')

urlpatterns = router.urls


urlpatterns = [
    path('', views.patient_list, name="patient_list"),
    path('create/', views.patient_create, name="patient_create"),
    path('update/<int:id>/', views.patient_update, name="patient_update"),
    path('delete/<int:id>/', views.patient_delete, name="patient_delete"),
    path('api/', include(router.urls)),


    path('', views.patient_list, name='patient_list'),
    path('create/', views.patient_create, name='patient_create'),
    path('update/<int:id>/', views.patient_update, name='patient_update'),
    path('delete/<int:id>/', views.patient_delete, name='patient_delete'),
]
