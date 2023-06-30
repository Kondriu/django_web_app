from django.contrib import admin
from django.utils.safestring import mark_safe 

from .models import CmsSlider
# Register your models here.
class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    list_display_links = ('cms_title', )
    list_editable=('cms_css', )
    fieds = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img', )


    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.cms_img.url}" wigth="80px"') 

 
admin.site.register(CmsSlider)
