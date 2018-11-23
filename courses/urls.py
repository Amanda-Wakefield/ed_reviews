from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateCourseView.as_view(), name='course_list'),
]