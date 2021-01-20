from django.contrib import admin
from .models import Idea
from .models import DevTool


@ admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['pk','name','desc']
    list_display_links = ['name']
    list_filter = ['updated_at']


@ admin.register(DevTool)
class DevToolAdmin(admin.ModelAdmin):
    list_display = ['pk','name','content']
    list_display_links = ['name']
    list_filter = ['updated_at']


