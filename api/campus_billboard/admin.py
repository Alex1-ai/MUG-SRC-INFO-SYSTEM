from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import BillBoard
# Register your models here.
@admin.register(BillBoard)
class BillBoardAdmin(admin.ModelAdmin):
    list_display = ['poster_img', 'get_thumbnail',
                     'created_at', 'updated_at']
    
    def get_thumbnail(self,obj):
        if obj.poster_img:
           return format_html('<img src="{}" height="50px" />', obj.poster_img.url)
        else:
            return None
        
    get_thumbnail.short_description = 'Thumbnail'  # Sets the column header name in the admin list view