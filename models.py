from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    grade = models.IntegerField(default=1)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
