from django.contrib import admin

from game.models import *


class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "active", "name", "has_script", "trouble_cost", "description")
    list_display_links = ("name",)
    list_editable = ('active',)
    model = Card
    ordering = ('name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(CardAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['mutation_template'].required = False
        return form

    @staticmethod
    def has_script(obj):
        return bool(obj.script)


class OperationModifierAdmin(admin.ModelAdmin):
    list_display = ("id", "active", "has_script",)
    list_display_links = ("id",)
    list_editable = ('active',)
    model = OperationModifier
    ordering = ('id',)

    @staticmethod
    def has_script(obj):
        return bool(obj.script)


class MutationTemplateAdmin(admin.ModelAdmin):
    model = MutationTemplate


admin.site.register(Card, CardAdmin)
admin.site.register(OperationModifier, OperationModifierAdmin)
admin.site.register(StudentInfo)
admin.site.register(MutationTemplate, MutationTemplateAdmin)
admin.site.register(OperationTag)
