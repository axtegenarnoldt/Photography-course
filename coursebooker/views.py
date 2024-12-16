from django.shortcuts import render
from django.views import generic, View
from .models import Course

# Create your views here.
class CourseList(generic.ListView):

    model = Course
    queryset = Course.objects.filter(status=1).order_by('difficulty',
                                                      '-created_on')
    template_name = "index.html"
    paginate_by = 6

def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    # Add any additional logic here
    return render(request, 'course_detail.html', {'course': course})