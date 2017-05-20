from django.contrib import admin

from configuration.models import *


def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)


def activate(modeladmin, request, queryset):
    queryset.update(active=True)


deactivate.short_description = "Deactivate"
activate.short_description = "Activate"


class CardAdmin(admin.ModelAdmin):
    list_display = ("active", "name", "card_type", "trouble_cost", "description")
    list_display_links = ("name",)
    list_editable = ('active',)
    model = Card
    ordering = ('-card_type', 'name')
    actions = [activate, deactivate]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
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

    list_display = ("name", "priority", "get_tags", "gameflow_binding")

    @staticmethod
    def get_tags(obj):
        return ", ".join(obj.tags)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['uses'].required = False
        return form


admin.site.register(Card, CardAdmin)
admin.site.register(OperationModifier, OperationModifierAdmin)
admin.site.register(StudentInfo)
admin.site.register(MutationTemplate, MutationTemplateAdmin)
admin.site.register(OperationTag)
