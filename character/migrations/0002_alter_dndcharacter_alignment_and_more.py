# Generated by Django 5.0.2 on 2024-02-13 01:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dndcharacter',
            name='alignment',
            field=models.CharField(choices=[('lawfulgood', 'Lawful Good'), ('lawfulneutral', 'Lawful Neutral'), ('lawfulevil', 'Lawful Evil'), ('neutralgood', 'Neutral Good'), ('trueneutral', 'True Neutral'), ('neutralevil', 'Neutral Evil'), ('chaoticgood', 'Chaotic Good'), ('chaoticneutral', 'Chaotic Neutral'), ('chaoticevil', 'Chaotic Evil')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='armor',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='charisma',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='class_name',
            field=models.CharField(choices=[('barbarian', 'Barbarian'), ('bard', 'Bard'), ('cleric', 'Cleric'), ('druid', 'Druid'), ('fighter', 'Fighter'), ('monk', 'Monk'), ('paladin', 'Paladin'), ('ranger', 'Ranger'), ('rogue', 'Rogue'), ('sorcerer', 'Sorcerer'), ('warlock', 'Warlock'), ('wizard', 'Wizard')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='constitution',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='dexterity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='initiative',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='intelligence',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='race',
            field=models.CharField(choices=[('dragonborn', 'Dragonborn'), ('dwarf', 'Dwarf'), ('elf', 'Elf'), ('gnome', 'Gnome'), ('halfelf', 'Half-Elf'), ('halfling', 'Halfling'), ('halforc', 'Half-Orc'), ('human', 'Human'), ('tiefling', 'Tiefling')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='speed',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='strength',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='dndcharacter',
            name='wisdom',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
        ),
    ]
