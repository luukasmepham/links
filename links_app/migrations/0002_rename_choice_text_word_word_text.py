# Generated by Django 5.0.2 on 2024-02-28 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='choice_text',
            new_name='word_text',
        ),
    ]
