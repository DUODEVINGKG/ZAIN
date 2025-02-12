from django.urls import path
from apps.base.views import index, contact, project_details, error

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('project_details/<int:id>/', project_details, name='project_details'),
    path('error/', error, name="error")
]