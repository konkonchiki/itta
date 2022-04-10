from django.contrib import admin
from .models import Tag , Post

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    search_fields           = ('title' , 'text')
    list_display            = ['title','is_public','updated_at','create_at','title_len']
    list_filter             = ['is_public','tags']
    ordering                = ('-updated_at',)
    
    def title_len(self,obj):
        return len(obj.title)
    
    title_len.short_description = 'タイトルの文字数'
    summernote_fields = ('text',)

    
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)