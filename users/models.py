from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    groups = models.ManyToManyField('Group', related_name='teachers')


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    groups = models.ManyToManyField('Group', related_name='students')


class Group(models.Model):
    name = models.CharField(max_length=255)

    owner = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name
