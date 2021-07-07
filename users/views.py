from users.models import Teacher, Group, Student
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from users.serializers import GroupSerializer

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account Created for {username} Successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# create group
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def create_group(request):
    user = request.user
    teacher = get_object_or_404(Teacher, user=user)
    group_serializer = GroupSerializer(data=request.data)
    group_serializer.is_valid(raise_exception=True)
    group_serializer.save(owner=teacher)
    return Response(group_serializer.data, 201)


# join student to group
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@csrf_exempt
def student_join_group(request):
    user = request.user
    student = get_object_or_404(Student, user=user)
    group_id = request.data.get('group_id')
    group = get_object_or_404(Group, id=int(group_id))
    student.groups.add(group)
    student.save()
    return Response({'success': 'student added to group successfully'}, 200)