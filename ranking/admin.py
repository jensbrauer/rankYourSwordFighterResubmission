from django.contrib import admin
from .models import Swordfighter, Comment



@admin.register(Swordfighter)
class SwordfighterAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ('status',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('submitted_by', 'num_flags', 'status')
    ordering = ('-num_flags',)
    list_filter = ('status',)
