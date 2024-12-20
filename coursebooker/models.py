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

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                            related_name="user_bookings", unique_for_date='course__id')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendees_count = models.PositiveIntegerField(validators=[MaxValueValidator(4)])
    confirmed = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'course'], 
            name='unique_booking_per_user_per_course')
        ]