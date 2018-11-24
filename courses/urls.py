from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.ListCreateCourseView.as_view(),
         name='course_list'),
    path('<int:pk>/',
         views.RetrieveUpdateDestroyCourseView.as_view(),
         name='course_detail'),
    path('<int:course_pk>/reviews/',
         views.ListCreateReviewView.as_view(),
         name='review_list'),
    path('<int:course_pk>/reviews/<int:pk>/',
         views.RetrieveUpdateDestroyReviewView.as_view(),
         name='review_detail'),
]