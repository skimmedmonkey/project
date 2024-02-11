# Generated by Django 5.0.2 on 2024-02-11 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monsters', '0002_rename_monstermodel_monster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armor', models.CharField(help_text='Armor Class field. Example: 17 (Natural Armor)', max_length=100)),
            ],
            options={
                'ordering': ['-armor'],
            },
        ),
        migrations.CreateModel(
            name='Meta_Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description', models.CharField(help_text='Enter a Meta description such as Large aberration, lawful evil', max_length=100)),
            ],
            options={
                'ordering': ['-meta_description'],
            },
        ),
    ]
