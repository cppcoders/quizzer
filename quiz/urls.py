from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('view_group', views.view_group, name='quiz-view_group'),
    path('groups', views.groups, name='quiz-groups'),
    path('about_us', views.about_us, name='quiz-about_us'),
    path('profile', views.profile, name='quiz-profile'),
    path('quiz_maker', views.quiz_maker, name='quiz-quiz_maker'),
    path('quiz', views.quiz, name='quiz-quiz'),
    path('quizzes', views.quizzes, name='quiz-quizzes'),
    path('attemp', views.attemp, name='quiz-attempt'),
]
