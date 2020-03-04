from rest_framework import serializers, viewsets
from .models import Player, Room, World

class PlayerSerializer(serializers.HyperlinkedModelSerializer): # HyperlinkedModelSerializer ~> gives us nice links

    # nested class
    class Meta:
        model = Player
        fields = ('player_name', 'players_current_room')

    def create(self, validated_data):
        ## fires up debugger when creating a new object (player)
        # import pdb; pdb.set_trace() 

        user = self.context['request'].user
        # make a new player with validated player and return it
        player = Player.objects.create(user=user, **validated_data)

        return player

# connect our serializer to our Players rows
class PlayerSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    # def get_queryset(self):

    #     user = self.request.user

        # check the user that is logged in
        # if user.is_anonymous:
        #     return Player.objects.none()
        # else:
        #     return Player.objects.filter(user=user)

# #################################
# ROOM Serializer
class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('title', 'description')

    # Create a new room
    def create(self, validated_data):
        #import pdb; pdb.set_trace() 
        room = Room.objects.create(**validated_data)
        return room


# connect our serializer to our Room rows
class RoomSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


# #################################
# World Serializer
class WorldSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = World
        fields = ('room_id')

    # Create a new room
    def create(self, validated_data):
        #import pdb; pdb.set_trace() 
        world = World.objects.create(**validated_data)
        return world

# connect our serializer to our Room rows
class WorldSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = WorldSerializer
    queryset = World.objects.all()
