from django.contrib import admin
from game.models import *
# Register your models here
class CardTargetOperationSetInline(admin.TabularInline):
    model = CardTargetOperationSet


class CardAdmin(admin.ModelAdmin):
    model = Card
    inlines = [
        CardTargetOperationSetInline,
    ]


class OperationInline(admin.TabularInline):
    model = Operation


class OperationSetAdmin(admin.ModelAdmin):
    inlines = [OperationInline,]
'''



#class OperationArgumentM2mInline(admin.TabularInline):
#    model = Operation.arguments.through


class InstructionAdmin(admin.ModelAdmin):
    model = Instruction
    #inlines = [
        #OperationArgumentM2mInline,
    #]


'''
admin.site.register(Card, CardAdmin)
admin.site.register(Target)
admin.site.register(Instruction)
admin.site.register(OperationSet, OperationSetAdmin)
admin.site.register(Operation)
admin.site.register(Argument)
admin.site.register(Operator)
#admin.site.register(CardType)
