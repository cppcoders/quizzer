from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Student, Teacher


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    status = forms.ChoiceField(
        choices=[("0", "Instructor"), ("1", "Student")], required=True)

    class Meta:
        model = User
        fields = ['status', 'username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        st = self.cleaned_data.get('status')
        if st == '1':
            user.is_student = True
            user.save()
            student = Student.objects.create(user=user)
        elif st == '0':
            user.is_teacher = True
            user.save()
            teacher = Teacher.objects.create(user=user)
        return user
