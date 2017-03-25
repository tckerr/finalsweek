from rest_framework import serializers
from sim.models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'created',)
        read_only_fields = ('id', 'created',)