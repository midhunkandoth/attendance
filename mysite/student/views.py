from django.shortcuts import render
from django.http import HttpResponse

from .models import Course


def index(request):
    return HttpResponse("Hello, world. You're at the student index.")

def courses(request):
    courses_list = Course.objects.all().order_by('-number_of_years')

    context = {'courses_list': courses_list}

    return render(request, 'student/courses.html', context)
