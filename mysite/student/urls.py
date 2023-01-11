from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='detail'),
    path('create_course', views.CourseCreateView.as_view(), name='create_course' ),
]