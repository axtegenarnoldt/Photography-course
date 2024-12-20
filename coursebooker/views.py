from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Course
from .forms import CommentForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm

# Create your views here.
class CourseList(ListView):

    model = Course
    queryset = Course.objects.filter(status=1).order_by('difficulty',
                                                      '-created_on')
    template_name = "index.html"
    paginate_by = 6



def course_detail(request, course_slug):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = Course.objects.get(slug=course_slug)
            comment.user = request.user
            comment.save()
        return redirect('course_detail', course_slug=course_slug)
    else:
        form = CommentForm()
    
    course = get_object_or_404(Course, slug=course_slug)
    comments = course.comments.filter(approved=True).order_by('-created_on')
    
    return render(request, 'course_detail.html', {
        'course': course,
        'comments': comments,
        'form': form,
})


    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
