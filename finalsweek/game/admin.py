from django.contrib import admin
from game.models import *
# Register your models here


class CardTargetEffectSetInline(admin.TabularInline):
    model = CardTargetEffectSet

class EffectM2mInline(admin.TabularInline):
    model = EffectSet.effects.through

class EffectSetAdmin(admin.ModelAdmin):
    model = EffectSet
    inlines = [
        EffectM2mInline,
    ]

class CardAdmin(admin.ModelAdmin):
    model = Card
    inlines = [
        CardTargetEffectSetInline,
    ]

admin.site.register(Card, CardAdmin)
admin.site.register(Target)
admin.site.register(Effect)
admin.site.register(EffectSet, EffectSetAdmin)
