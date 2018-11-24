from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateCourseView.as_view(),
         name='course_list'),
    path('<int:pk>/', views.RetrieveUpdateDestroyCourseView.as_view(),
         name='course_detail'),
]