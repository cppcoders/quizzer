from quiz.models import Answer, Exam, Question, Group
from django.contrib import admin

admin.site.register(Group)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Answer)
