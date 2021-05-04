from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    groups = models.ManyToManyField('Group', related_name='teachers')

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    groups = models.ManyToManyField('Group', related_name='students')

    def __str__(self):
        return self.user.username


class Group(models.Model):
    name = models.CharField(max_length=255)

    owner = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, related_name='owned_groups', null=True)

    def __str__(self):
        return self.name
