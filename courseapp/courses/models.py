from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-id']

class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='lessons/%Y/%m/', null=True)

    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='lessons')
    tags = models.ManyToManyField('Tag', related_name='lessons')
    bookmarks_users = models.ManyToManyField(User, through='Bookmark')

    def __str__(self):
        return self.subject

class Comment(BaseModel):
    content = models.CharField(max_length=255)

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Bookmark(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='bookmarks')

    def __str__(self):
        return f'{self.user.username} - {self.lesson.subject}'