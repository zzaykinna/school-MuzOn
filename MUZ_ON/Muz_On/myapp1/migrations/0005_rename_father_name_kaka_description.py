# Generated by Django 5.0.2 on 2024-03-05 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0004_kaka_delete_specialties'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kaka',
            old_name='father_name',
            new_name='description',
        ),
    ]
