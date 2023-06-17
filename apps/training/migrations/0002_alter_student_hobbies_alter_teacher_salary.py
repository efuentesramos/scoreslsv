# Generated by Django 4.2.2 on 2023-06-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hobbies',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
