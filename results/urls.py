# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('class-result/', views.result_class_list, name='result_class_list'),
    path('class-result/<int:class_id>/passed-students/', views.class_passed_students, name='class_passed_students'),
]
