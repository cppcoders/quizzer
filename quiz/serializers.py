
from quiz.models import *
from users.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    exams = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = ['name', 'owner', 'students', 'exams']


class ExamSerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Exam
        fields = ['name', 'owner', 'group', 'questions']


class QuestionsSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)
    correct = serializers.StringRelatedField()
    class Meta:
        model = Question
        fields = ['exam', 'text', 'answers', 'correct']