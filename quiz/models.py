from users.models import Teacher, Group
from django.db import models


class Exam(models.Model):
    owner = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text
