# Generated by Django 5.0.2 on 2024-02-13 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_alter_dndcharacter_alignment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dndcharacter',
            name='spells',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
