from django.contrib import admin
from .models import Src_News
from django.utils.html import format_html
# Register your models here.
@admin.register(Src_News)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title',
                    "get_thumbnail","updated_at"
                    ]
    def get_thumbnail(self,obj):
        if obj.image:
           return format_html('<img src="{}" height="50px" />', obj.image.url)
        else:
            return None
        
    get_thumbnail.short_description = 'Thumbnail'  # Sets the column header name in the admin list view