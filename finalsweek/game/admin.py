from django.contrib import admin
from django.utils.html import format_html
from game.models import *

class CardTargetOperationSetInline(admin.TabularInline):
    model = CardTargetOperationSet

class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "active", "linked_name", "has_script", "trouble_cost", "description")
    list_editable = ('active',)
    model = Card
    inlines = [
        CardTargetOperationSetInline,
    ]

    def linked_name(self, obj):
        return format_html("<a href='{id}/change'><b>{name}</b></a>".format(id=obj.id, name=obj.name))

    def has_script(self, obj):
        return bool(obj.script)

class OperationInline(admin.TabularInline):
    model = Operation

class OperationSetAdmin(admin.ModelAdmin):
    inlines = [OperationInline,]

admin.site.register(Card, CardAdmin)
admin.site.register(Target)
admin.site.register(Instruction)
admin.site.register(OperationSet, OperationSetAdmin)
admin.site.register(Operation)
admin.site.register(Argument)
admin.site.register(Operator)
