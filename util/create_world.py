from django.contrib.auth.models import User
from tafmudapp.models import Room, Player
# Room.objects.all().delete()
# r_outside = Room(title="Outside Cave Entrance",description="North of you, the cave mount beckons")
# r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
# passages run north and east.""")
# r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")
# # r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
# # to north. The smell of gold permeates the air.""")
# # r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
# # chamber! Sadly, it has already been completely emptied by
# # earlier adventurers. The only exit is to the south.""")
# r_outside.save()
# r_foyer.save()
# r_overlook.save()
# # r_narrow.save()
# # r_treasure.save()
# # Link rooms together
# r_outside.connectRooms(r_foyer, "n")
# r_foyer.connectRooms(r_outside, "s")
# r_foyer.connectRooms(r_overlook, "n")
# r_overlook.connectRooms(r_foyer, "s")
# r_foyer.connectRooms(r_narrow, "e")
# r_narrow.connectRooms(r_foyer, "w")
# r_narrow.connectRooms(r_treasure, "n")
# r_treasure.connectRooms(r_narrow, "s")
# players = Player.objects.all()
# for p in players:
#     p.players_current_room = r_outside.id
#     p.save()
# # create a list with random descriptions
# random_descriptions = ["Under a loose bit of cobblestone on the ground, you see what appears to be a small tunnel. If you reach inside or stick around too long, a living crawling hand jumps out of the hole and attacks. This living hand has been hoarding rings and jewelry in this tunnel.",
# "The group finds a long forgotten coin hoard. All is not as it seems, some of the coins are tiny-sized mimics (maybe individuals, maybe swarms), that adhere to and attack those that try to gather the treasure.",
# "A crumbling wall with a small tunnel bore through its base hides the resting room for a peaceful Goblin who knows the dungeon well and will give directions or hints in trade for an interesting item.",
# "A series of really, staggeringly obvious traps. There`s a tripwire thats made of thick hemp rope, a wooden pressure plate set in the middle of a cobblestone path, a dark path with a torch set right at the beginning (the torch is crudely attached to a lever on the wall).",
# "The ceiling is completely covered with horrid insects – dark, silent and unseen except for the occasional masonry dust they knock loose.",
# "Around a corner, you hear clucking. Theres a chicken in the dungeon? Youre three levels down. Shrug: maybe its just random. But every three rooms or so, theres another one, just a chicken walking around and pecking at the dirt. Then you get to a region where there arent any chickens. That’s when shit gets real. Because the chickens are a food source."]
# every time we create a new room we insert a random description
for _ in range(150):
    r_inst = Room.objects.all().order_by("?").first()
    if r_inst.n_to == 0:
        # TODO update titles and desc to random
        if r_inst.loc_y == 254:
            print(r_inst.loc_y)
            continue
        new_room = Room(title="North Title", description="North Desc")
        new_room.loc_y = r_inst.loc_y + 1
        new_room.loc_x = r_inst.loc_x
        new_room.save()
        r_inst.connectRooms(new_room, "n")
        new_room.connectRooms(r_inst, "s")
    # continue 
    elif r_inst.s_to == 0:
        # TODO update titles and desc to random
        if r_inst.loc_y == 20:
            print(r_inst.loc_y)
            continue
        new_room = Room(title="South Title", description="South Desc")
        new_room.loc_y = r_inst.loc_y - 1
        new_room.loc_x = r_inst.loc_x
        new_room.save()
        r_inst.connectRooms(new_room, "s")
        new_room.connectRooms(r_inst, "n")
    # continue
    elif r_inst.e_to == 0:
        if r_inst.loc_x == 120:
            print(r_inst.loc_x)
            continue
        # TODO update titles and desc to random
        new_room = Room(title="East Title", description="East Desc")
        new_room.loc_x = r_inst.loc_x + 1
        new_room.loc_y = r_inst.loc_y
        new_room.save()
        r_inst.connectRooms(new_room, "e")
        new_room.connectRooms(r_inst, "w")
    # continue
    elif r_inst.w_to == 0:
        # TODO update titles and desc to random
        if r_inst.loc_x == 20:
            print(r_inst.loc_x)
            continue
        new_room = Room(title="West Title", description="West Desc")
        new_room.loc_x = r_inst.loc_x - 1
        new_room.loc_y = r_inst.loc_y
        new_room.save()
        r_inst.connectRooms(new_room, "w")
        new_room.connectRooms(r_inst, "e")
    # continue
# new rooms must be adjacent to each other
# if room pulled has an available direction we create a room in that direction.
# if no directions available pick another room at random and check for available directions
# for loop 150 times untill all rooms are created