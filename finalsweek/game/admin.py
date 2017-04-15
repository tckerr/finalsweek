from django.contrib import admin
from django.utils.html import format_html
from game.models import *

class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "active", "linked_name", "has_script", "trouble_cost", "description")
    list_editable = ('active',)
    model = Card

    def linked_name(self, obj):
        return format_html("<a href='{id}/change'><b>{name}</b></a>".format(id=obj.id, name=obj.name))

    def has_script(self, obj):
        return bool(obj.script)


admin.site.register(Card, CardAdmin)
