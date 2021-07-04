from django.db.models.expressions import F
from users.models import Teacher, Group, Student
from django.db import models
from django.utils import timezone


class Exam(models.Model):
    owner = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='exams')
    name = models.CharField(max_length=255)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='exams')
    quiz_date = models.DateTimeField(auto_now_add=True)
    quiz_duration = models.IntegerField(default=0)


    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=100, null=False, blank=False)
    question_head = models.CharField(max_length=255, null=False, blank=False)
    question_options = models.CharField(max_length=150, null=True, blank=True)
    question_rows = models.CharField(max_length=255, null=True, blank=True)
    question_columns = models.CharField(max_length=255, null=True, blank=True)
    question_right_answer = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return self.question_head


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Attempt(models.Model):
    owner = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='attempts')
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name='attempts')
    time = models.DateTimeField(default=timezone.now)
    grade = models.FloatField()


class AttemptAnswers(models.Model):
    attempt = models.ForeignKey(
        Attempt, on_delete=models.CASCADE, related_name='answers')
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, related_name='attempts')
