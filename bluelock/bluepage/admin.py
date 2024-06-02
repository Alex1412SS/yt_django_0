from django.contrib import admin
from .models import Ai_tools


admin.site.site_header = "learn admin panel"
admin.site.site_title = "learn admin panel"


class Aiadmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'about', )
    search_fields = ('name',)
    list_editable = ('about',)
    actions = ('makezer',)
    def makezer(self, request, queryset):
        queryset.update(name='not found')

admin.site.register(Ai_tools, Aiadmin)