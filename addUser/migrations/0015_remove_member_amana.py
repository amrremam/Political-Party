# Generated by Django 4.2.5 on 2024-01-20 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addUser', '0014_rename_detail_member_partyde'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='amana',
        ),
    ]
