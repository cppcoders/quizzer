from quiz.views import quiz
from quiz.models import Exam
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from users.models import Group, Student, Teacher, User
from .serializers import (
    GroupSerializer, 
    QuizSerializer,
    GroupMemebrsSerializer,
    QuestionsSerializer,
    AttemptSerializer,
    CreateQuizzSerializer,
    CreateQuestionSerializer
)
from quiz import serializers
# list groups
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def list_groups(request):
    user = request.user
    try:
        student = get_object_or_404(Student, user=user)
        groups = student.groups.all()
    except:
        teacher = get_object_or_404(Teacher, user=user)
        groups = teacher.groups.all()
    
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data, 200)


# list Quizes For Groups:
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def list_quizzes_per_groups(request):
    user = request.user
    try:
        student = get_object_or_404(Student, user=user)
        groups = student.groups.all()
    except:
        teacher = get_object_or_404(Teacher, user=user)
        groups = teacher.groups.all()
    qroup_quizzes = Exam.objects.filter(group__in=groups)
    serializer = QuizSerializer(qroup_quizzes, many=True)
    return Response(serializer.data, 200)


# get memebers details by group id
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def get_group_members(request, group_id):
    group = get_object_or_404(Group, id=int(group_id))
    members = group.students.all()
    serializer = GroupMemebrsSerializer(members, many=True)
    return Response(serializer.data, 200)


# list Quizes For Group:
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def get_group_quizzes(request, group_id):
    group = get_object_or_404(Group, id=int(group_id))
    qroup_quizzes = Exam.objects.filter(group=group)
    serializer = QuizSerializer(qroup_quizzes, many=True)
    return Response(serializer.data, 200)

# remove student from group
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def remove_user_from_group(request, user_id, group_id):
    user = get_object_or_404(User, id=user_id)
    student = get_object_or_404(Student, user=user)
    group = get_object_or_404(Group, id=int(group_id))
    try:
        student.groups.remove(group)
        student.save()
        return Response('user removed from group successfully', 200)
    except Exception as e:
        return Response({'error': f'{e}'}, 404)


# get current quizz by quiz_id
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def get_quizz_details(request, quiz_id):
    quiz = get_object_or_404(Exam, id=int(quiz_id))
    serializer = QuizSerializer(quiz)
    return Response(serializer.data, 200)

# get quizz questions by quiz id
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def get_quizz_questions(request, quiz_id):
    quiz = get_object_or_404(Exam, id=int(quiz_id))
    questions = quiz.questions.all()
    serializer = QuestionsSerializer(questions, many=True)
    return Response(serializer.data, 200)


# Post Exam Answers
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def student_exam_attempt(request):
    user = request.user
    student = get_object_or_404(Student, user=user)
    answers = AttemptSerializer(data=request.data , many=True)
    answers.is_valid(raise_exception=True)
    answers.save(owner=student)
    return Response(answers.data, 201)


# create quiz
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def create_quizz(request):
    user = request.user
    teacher = get_object_or_404(Teacher, user=user)
    quiz_serializer = CreateQuizzSerializer(data=request.data)
    quiz_serializer.is_valid(raise_exception=True)
    quiz_serializer.save(owner=teacher)
    return Response(quiz_serializer.data, 201)


# create question
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def create_question(request):
    user = request.user
    teacher = get_object_or_404(Teacher, user=user)
    question = CreateQuestionSerializer(data=request.data)
    question.is_valid(raise_exception=True)
    question.save()
    return Response(question.data, 201)
