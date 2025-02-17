from django.contrib import admin
from courses.models import Category, Course, Tag, Lesson, Comment, Bookmark

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Bookmark)
