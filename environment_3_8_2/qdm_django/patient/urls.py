from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
# generate patients/id/

urlpatterns = [
    path('', include(router.urls)),
]