from quiz.models import Answer, Attempt, AttemptAnswers, Exam, Question
from django.contrib import admin

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(AttemptAnswers)
