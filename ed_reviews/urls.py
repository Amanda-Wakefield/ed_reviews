"""ed_reviews URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from courses import views

router = routers.SimpleRouter()
router.register('courses', views.CourseViewSet)
router.register('reviews', views.ReviewViewSet)

app_name = 'courses'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('api/v1/courses/', include(('courses.urls', app_name),
                                    namespace='courses')),
    path('api/v2/', include((router.urls, app_name),
                            namespace='apiv2')),
]



