# Generated by Django 5.0.2 on 2024-03-25 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0009_feedback_record_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(max_length=35),
        ),
    ]
