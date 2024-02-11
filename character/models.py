from django.db import models

# Create your models here.

class DnDCharacter(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    alignment = models.CharField(max_length=50)
    strength = models.CharField(max_length=50)
    dexterity = models.CharField(max_length=50)
    constitution = models.CharField(max_length=50)
    intelligence = models.CharField(max_length=50)
    wisdom = models.CharField(max_length=50)
    charisma = models.CharField(max_length=50)
    armor = models.CharField(max_length=50)
    initiative = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    equipment = models.CharField(max_length=50)
    attacks = models.CharField(max_length=50)
    spells = models.CharField(max_length=300)
