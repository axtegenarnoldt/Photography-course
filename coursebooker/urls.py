from . import views
from django.urls import path

urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('courses/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('register/', views.register, name='register'),
    
]