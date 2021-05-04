from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Teacher, Student


@receiver(post_delete, sender=Teacher)
def auto_delete_user_with_teacher(sender, instance, **kwargs):
    instance.user.delete()


@receiver(post_delete, sender=Student)
def auto_delete_user_with_teacher(sender, instance, **kwargs):
    instance.user.delete()
