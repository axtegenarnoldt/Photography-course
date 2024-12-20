from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY = ((0, "Beginner"), (1, "Advanced"))


class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    difficulty = models.IntegerField(choices=DIFFICULTY)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='Photography_course_likes', blank=True)

    class Meta:
        ordering = ['difficulty']
   
    def __str__(self):
        return self.title

class Comment(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    text = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return f'Comment {self.message} by {self.username}'


class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                             related_name='scheduled_photography_courses')
    time = models.DateTimeField()
    location = models.CharField(max_length=200)

    class Meta:
        ordering = ['time']
        indexes = [
            models.Index(fields=['time'], name='schedule_time_idx'),
        ]

    def __str__(self):
        return f'Your photography course {self.course} is scheduled for {self.location} at {self.time}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                          related_name="bookings")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], 
            name='unique_booking_per_user_per_course')
        ]

    def __str__(self):
        return f"{self.user.username} booking for {self.course.title}"
