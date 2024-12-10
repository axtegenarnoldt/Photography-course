from django.shortcuts import render
from django.views import generic, view
from .models import Course

# Create your views here.
class CourseList(generic.ListView):

    model = Course
    queryset = Course.objects.filter(status=1).order_by('difficulty',
                                                      '-created_on')
    template_name = "index.html"
    paginate_by = 6