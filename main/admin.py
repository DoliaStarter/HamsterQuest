from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile,Quests,Sessions,Stages,Tags


admin.site.register([UserProfile,Quests,Sessions,Stages,Tags])