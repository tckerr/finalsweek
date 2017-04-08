from django.contrib import admin
from game.models import *
# Register your models here


class CardTargetOperationSetInline(admin.TabularInline):
    model = CardTargetOperationSet

class OperationM2mInline(admin.TabularInline):
    model = OperationSet.operations.through

class OperationSetAdmin(admin.ModelAdmin):
    model = OperationSet
    inlines = [
        OperationM2mInline,
    ]

#class OperationArgumentM2mInline(admin.TabularInline):
#    model = Operation.arguments.through


class OperationAdmin(admin.ModelAdmin):
    model = Operation
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
admin.site.register(Operation, OperationAdmin)
admin.site.register(OperationSet, OperationSetAdmin)
admin.site.register(OperationArgument)
admin.site.register(Operator)
