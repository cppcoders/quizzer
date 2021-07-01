# Generated by Django 3.1.7 on 2021-05-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210501_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='groups',
            field=models.ManyToManyField(related_name='students', to='users.Group'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='groups',
            field=models.ManyToManyField(related_name='teachers', to='users.Group'),
        ),
    ]