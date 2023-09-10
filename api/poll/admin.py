from django.contrib import admin
from .models import Position, Candidate, Vote
from django.utils.html import format_html
# Register your models here.
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',
                     'created_at', 'updated_at']



@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'department','get_thumbnail','votes', 'position']
    
    def get_thumbnail(self,obj):
        if obj.image:
           return format_html('<img src="{}" height="50px" />', obj.image.url)
        else:
            return None
        
    get_thumbnail.short_description = 'Thumbnail'  # Sets the column header name in the admin list view




admin.site.register(Vote)
# @admin.register(Vote)
# class  VoteAdmin(admin.ModelAdmin):
#     list_display = ['user', 'candidate',
#                      'vote_on', 'position']
