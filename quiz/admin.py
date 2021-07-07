from quiz.models import Attempt, Exam, Question
from django.contrib import admin

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Attempt)

