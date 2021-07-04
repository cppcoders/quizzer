from quiz.decorators import teacher_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'quiz/home.html')


def login(request):
    return render(request, 'quiz/login.html')


@login_required
def view_group(request):
    return render(request, 'quiz/view_group.html')


@login_required
def groups(request):
    return render(request, 'quiz/groups.html')


@login_required
def quizzes(request):
    return render(request, 'quiz/quizzes.html')


@login_required
def about_us(request):
    return render(request, 'quiz/about_us.html')


@login_required
def profile(request):
    return render(request, 'quiz/profile.html')


@login_required
@teacher_required
def quiz_maker(request):
    return render(request, 'quiz/quiz_maker.html')


@login_required
def quiz(request):
    return render(request, 'quiz/quiz.html')


@login_required
def attemp(request):
    return render(request, 'quiz/attemp.html')


