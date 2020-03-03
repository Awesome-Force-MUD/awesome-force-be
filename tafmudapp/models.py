from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

## Room Model
class Room(models.Model):               # inherits the models modules from our sql db connected to django
    title = models.CharField(max_length=50, default="This is a default title")
    description = models.CharField(max_length=500, default="This is a default description")

    # add directions in order to move from our rooms
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)

    # define a function that will connect our rooms together
    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id      # this var will hold the room we are connected to
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist.")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print(" You entered an invalid direction. Please choose: 'n', 's', 'e', or 'w'. ")
                return
            # Save the current instance
            self.save()
    
    # create a method that creates a player name that will use djangos User module from django.contrib.auth.models
    def playerName(self, currentPlayerName):
        return [p.user.username for p in Player.objects.filter(currentRoom = self.id) if p.id != int(currentPlayerName)]

    # create a player uuid (uuid4 for a random ID) from the uuid module
    def playerID(self, currentPlayerID):
        return [p.uuid4 for p in Player.objects.filter(currenRoom=self.id) if p.id != int(currentPlayerID)]

###### Current End of Room Class

# Create a Player Class Model that inherits the models.Model module
class Player(models.Model):
    # create a radnom uuid for our players
    player_id = models.UUIDField(default=uuid4, unique=True) 
    # this creates a user in the adamin site of our django back end/server
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # will be updated with players current room. begin at zero until told otherwise
    players_current_room = models.IntegerField(default=0)

    # create a Player Method that initializes their current room
    def initialize(self):
        if self.players_current_room == 0:
            self.players_current_room = Room.objects.first().id
            self.save()

    # create a Player method that returns the players current room
    def room(self):
        try:
            return Room.objects.get(id=self.players_current_room)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()