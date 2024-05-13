# Generated by Django 5.0.2 on 2024-03-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=35)),
                ('second_name', models.CharField(max_length=35)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]
