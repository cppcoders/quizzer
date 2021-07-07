
from quiz.views import quiz
from quiz.models import *
from users.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = ['id','group_name',]

    def get_group_name(self, obj):
        return obj.name


class QuizSerializer(serializers.ModelSerializer):
    quiz_id = serializers.SerializerMethodField()
    quiz_title = serializers.SerializerMethodField()
    quiz_group = serializers.SerializerMethodField()
    class Meta:
        model = Exam
        fields = ['quiz_id','quiz_title', 'quiz_group', 'quiz_date', 'quiz_duration']

    def get_quiz_id(self, obj):
        return obj.id
    
    def get_quiz_title(self, obj):
        return obj.name
    
    def get_quiz_group(self, obj):
        return obj.group.name
    

class GroupMemebrsSerializer(serializers.ModelSerializer):
    memeber_id = serializers.SerializerMethodField()
    member_name = serializers.SerializerMethodField()
    memeber_email = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['memeber_id', 'member_name', 'memeber_email']

    def get_memeber_id(self, obj):
        return obj.user.id
    
    def get_member_name(self, obj):
        return obj.user.get_full_name()
    
    def get_memeber_email(self, obj):
        return obj.user.email

class QuestionsSerializer(serializers.ModelSerializer):
    question_id = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ['question_id', 'question_type', 'question_head', 'question_options', 'question_rows', 'question_columns', 'question_right_answer']

    def get_question_id(self, obj):
        return obj.id


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = '__all__'
        read_only_fields = ['owner']
    

class CreateQuizzSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = '__all__'
        read_only_fields = ['owner']


class CreateQuestionSerializer(serializers.ModelSerializer):
    question_options = serializers.CharField(required=False)
    question_rows = serializers.CharField(required=False)
    question_columns = serializers.CharField(required=False)
    question_right_answer = serializers.CharField(required=False)
    class Meta:
        model = Question
        fields = '__all__'
        
