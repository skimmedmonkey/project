from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class DnDCharacter(models.Model):
    race_choices = [('dragonborn','Dragonborn'),('dwarf','Dwarf'),('elf','Elf'),('gnome','Gnome'),('halfelf','Half-Elf'),('halfling','Halfling'),('halforc','Half-Orc'),('human','Human'),('tiefling','Tiefling')]
    class_choices = [('barbarian','Barbarian'),('bard','Bard'),('cleric','Cleric'),('druid','Druid'),('fighter','Fighter'),('monk','Monk'),('paladin','Paladin'),('ranger','Ranger'),('rogue','Rogue'),('sorcerer','Sorcerer'),('warlock','Warlock'),('wizard','Wizard')]
    alignment_choices = [('lawfulgood','Lawful Good'),('lawfulneutral','Lawful Neutral'),('lawfulevil','Lawful Evil'),('neutralgood','Neutral Good'),('trueneutral','True Neutral'),('neutralevil','Neutral Evil'),('chaoticgood','Chaotic Good'),('chaoticneutral','Chaotic Neutral'),('chaoticevil','Chaotic Evil')]

    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50, choices=race_choices)
    class_name = models.CharField(max_length=50, choices=class_choices)
    alignment = models.CharField(max_length=50, choices=alignment_choices)
    strength = models.IntegerField(validators=[MaxValueValidator(20)])
    dexterity = models.IntegerField(validators=[MaxValueValidator(20)])
    constitution = models.IntegerField(validators=[MaxValueValidator(20)])
    intelligence = models.IntegerField(validators=[MaxValueValidator(20)])
    wisdom = models.IntegerField(validators=[MaxValueValidator(20)])
    charisma = models.IntegerField(validators=[MaxValueValidator(20)])
    armor = models.IntegerField(validators=[MaxValueValidator(20)])
    initiative = models.IntegerField(validators=[MaxValueValidator(20)])
    speed = models.IntegerField(validators=[MaxValueValidator(30)])
    equipment = models.CharField(max_length=50)
    attacks = models.CharField(max_length=50)
    spells = models.CharField(max_length=300, blank=True, null=True)
