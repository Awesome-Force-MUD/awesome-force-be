from rest_framework import serializers, viewsets
from .models import Player, Room

class PlayerSerializer(serializers.HyperlinkedModelSerializer): # HyperlinkedModelSerializer ~> gives us nice links

    # nested class
    class Meta:
        model = Player
        fields = ('player_name', 'players_current_room')

    def create(self, validated_data):
        ### fires up debugger when creating a new object (player)
        # import pdb; pdb.set_trace() 

        user = self.context['request'].user
        # make a new player with validated player and return it
        player = Player.objects.create(user=user, **validated_data)

        return player

# connect our serializer to our Players rows
class PlayerSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.none()

    def get_queryset(self):

        user = self.request.user

        # check the user that is logged in
        if user.is_anonymous:
            return Player.objects.none()
        else:
            return Player.objects.filter(user=user)

