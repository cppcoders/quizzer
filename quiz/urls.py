from django.urls import path
from . import views
from . import apis

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

    ### Rest Apis END Points
    path('list_user_groups/', apis.list_groups, name='list-groups'),
    path('list_groups_quizzes/', apis.list_quizzes_per_groups, name='list-user-groups-exams'),
    path('get_group_members/<int:group_id>/', apis.get_group_members, name='get-group-memebers'),
    path('get_group_quizzes/<int:group_id>/', apis.get_group_quizzes, name='get-group-quizzes'),
    path('remove_group_user/<int:user_id>/<int:group_id>/', apis.remove_user_from_group, name='remove-group-user'),
    path('get_quiz/<int:quiz_id>/', apis.get_quizz_details, name='get-quiz'),
    path('get_quiz_questions/<int:quiz_id>/', apis.get_quizz_questions, name='get-quiz-questions'),
    path('answer_exam/', apis.student_exam_attempt, name='answer-exam'),    
    path('create_quizz/', apis.create_quizz, name='create-quizz'),
    path('create_question/', apis.create_question, name='create-question')
]
