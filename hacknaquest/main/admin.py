from django.contrib import admin

from .models import Users,Quests,Sessions,Stages,Tags


admin.site.register([Users,Quests,Sessions,Stages,Tags])