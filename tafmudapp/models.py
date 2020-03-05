# from django.conf import settings
# settings.configure()
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
##### Create a World Model to represent a container for our rooms
class World(models.Model):

    # our world needs borders to prevent leaking
    world_grid = models.IntegerField(default=None)
    # Let our height and width start at 0 until we add room
    # adding rooms should increase the default by 1 each time
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)


    # create a method to generate rooms automatically
    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        ## initialize the grid borders
        self.world_grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.world_grid)):
            self.world_grid[i] = [None] * size_x


        ## Begin in lower left corner aka (0, 0)
        x = -1
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1 # 1: east, -1: west


        # While there are rooms to be created...
        previous_room = None

        while room_count < num_rooms:

            # calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else: 
                #if we hit our world border walls turn NORTH and reverse the direction
                room_direction = "n"
                y += 1
                direction *= -1

            # Create a room in the given direction
            room = Room(room_count, Room.title, Room.description, x, y)

                        
            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            self.world_grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room:
                previous_room.connectRooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_count += 1


## Room Model
class Room(models.Model):               # inherits the models modules from our sql db connected to django
    # def __init__(self):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.n_to = None
    #     self.s_to = None
    #     self.e_to = None
    #     self.w_to = None
    #     self.x = x
    #     self.y = y
    loc_x = models.IntegerField(default=0)
    loc_y = models.IntegerField(default=0)
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
            # print("That room does not exist.")
            return
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
        return [p.user.username for p in Player.objects.filter(players_current_room = self.id) if p.id != int(currentPlayerName)]

    # create a player uuid (uuid4 for a random ID) from the uuid module
    def playerID(self, currentPlayerID):
        return [p.uuid4 for p in Player.objects.filter(players_current_room=self.id) if p.id != int(currentPlayerID)]

###### Current End of Room Class

# Create a Player Class Model that inherits the models.Model module
class Player(models.Model):
    # create a radnom uuid for our players
    player_id = models.UUIDField(default=uuid4, unique=True)
    #player name that is unrelatd to player_id
    player_name = models.CharField(max_length=25, default="Default Name")
    # this creates a user in the adamin site of our django back end/server
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # will be updated with players current room. begin at zero until told otherwise
    players_current_room = models.IntegerField(default=0)
    # add created at and modified at sections for our players



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




w = World()
num_rooms = 150
width = 8
height = 20
w.generate_rooms(width, height, num_rooms)
# w.print_rooms()


# print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")


















####################### Look Into receivers

# @receiver(post_save, sender=User)
# def create_user_player(sender, instance, created, **kwargs):
#     if created:
#         Player.objects.create(user=instance)
#         Token.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_player(sender, instance, **kwargs):
#     instance.player.save()