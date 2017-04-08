from django.contrib import admin
from game.models import *
# Register your models here


class CardTargetOperationSetInline(admin.TabularInline):
    model = CardTargetOperationSet

class OperationM2mInline(admin.TabularInline):
    model = OperationSet.instructions.through

class OperationSetAdmin(admin.ModelAdmin):
    model = OperationSet
    inlines = [
        OperationM2mInline,
    ]

#class OperationArgumentM2mInline(admin.TabularInline):
#    model = Operation.arguments.through


class InstructionAdmin(admin.ModelAdmin):
    model = Instruction
    #inlines = [
        #OperationArgumentM2mInline,
    #]

class CardAdmin(admin.ModelAdmin):
    model = Card
    inlines = [
        CardTargetOperationSetInline,
    ]

admin.site.register(Card, CardAdmin)
admin.site.register(Target)
admin.site.register(Instruction, InstructionAdmin)
admin.site.register(OperationSet, OperationSetAdmin)
admin.site.register(Argument)
admin.site.register(Operator)
admin.site.register(CardType)
