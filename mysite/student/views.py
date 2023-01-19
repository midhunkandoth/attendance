from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse


from .models import Course


def index(request):
    return HttpResponse("Hello, world. You're at the student index.")

def courses(request):
    courses_list = Course.objects.all().order_by('-number_of_years')

    context = {'courses_list': courses_list}

    return render(request, 'student/courses.html', context)


def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'student/detail.html', {'course': course})


class CourseCreateView(CreateView):
    model = Course
    fields = "__all__"
    
    def get_success_url(self):
        return reverse('detail', kwargs={'course_id': self.object.pk})


class CourseUpdateView(UpdateView):
    model = Course
    fields = "__all__"
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'course_id'
    
    def get_success_url(self):
        return reverse('detail', kwargs={'course_id': self.object.pk})
