from django.contrib import admin
from .models import Course, Comment, Schedule, Bookings
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)