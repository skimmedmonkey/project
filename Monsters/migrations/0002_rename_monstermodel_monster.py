# Generated by Django 5.0.2 on 2024-02-11 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Monsters', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MonsterModel',
            new_name='Monster',
        ),
    ]