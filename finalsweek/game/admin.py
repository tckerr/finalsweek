from django.contrib import admin
from django.utils.html import format_html
from game.models import *

class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "active", "name", "has_script", "trouble_cost", "description")
    list_display_links  = ("name",)
    list_editable = ('active',)
    model = Card
    ordering = ('name',)


    def has_script(self, obj):
        return bool(obj.script)


admin.site.register(Card, CardAdmin)
admin.site.register(StudentInfo)
