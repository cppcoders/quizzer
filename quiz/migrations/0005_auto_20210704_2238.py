# Generated by Django 3.2.5 on 2021-07-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210704_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_columns',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_head',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_options',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_right_answer',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_rows',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default='string', max_length=100),
            preserve_default=False,
        ),
    ]
