from django.db import models
from django.urls import reverse

# Create your models here.
class Monster(models.Model):
    """monster class models"""
    monster_name = models.CharField(max_length=50, unique=True, help_text='Enter a Monster Name')

    class Meta:
        ordering = ['-monster_name']
    
    def __str__(self):
        """String for representing the MonsterModel object (in Admin site etc.)"""
        return self.monster_name

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of monster name"""
        return reverse('model-detail-view', args=[str(self.id)])

class Item(models.Model):
    """item models"""
    item = models.CharField(max_length=100, help_text='Enter a Meta description such as Large aberration, lawful evil')

    class Meta:
        ordering = ['-item']
    
    def __str__(self):
        """String for representing the MonsterModel item (in Admin site etc.)"""
        return self.item

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of monster name"""
        return reverse('model-detail-view', args=[str(self.id)])

class NPC(models.Model):
    """monster class models"""
    npc = models.CharField(max_length=100, help_text='NPC field. Example: Villager')

    class Meta:
        ordering = ['-npc']
    
    def __str__(self):
        """String for representing the MonsterModel npc (in Admin site etc.)"""
        return self.npc

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of monster name"""
        return reverse('model-detail-view', args=[str(self.id)])
