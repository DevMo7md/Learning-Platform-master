# Generated by Django 4.2.5 on 2024-08-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LP_app', '0005_alter_student_alsaf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='alsaf',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
