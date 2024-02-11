from django.contrib import admin
from .models import Monster, Item, NPC
# Register your models here.
admin.site.register(Monster)
admin.site.register(Item)
admin.site.register(NPC)