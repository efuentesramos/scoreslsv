# Generated by Django 4.2.2 on 2023-06-19 21:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_alter_course_name_alter_student_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='training.teacher'),
        ),
        migrations.AlterField(
            model_name='course',
            name='total_hours',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)]),
        ),
    ]
