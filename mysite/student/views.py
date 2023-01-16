from django.shortcuts import render
from django.http import HttpResponse

from .models import Course


def index(request):
    return HttpResponse("Hello, world. You're at the student index.")

def courses(request):

    number_of_years = request.GET.get('number_of_years', 5)

    courses_list = Course.objects.filter(number_of_years__lte=number_of_years).order_by('-number_of_years')

    context = {'courses_list': courses_list}

    return render(request, 'student/courses.html', context)
