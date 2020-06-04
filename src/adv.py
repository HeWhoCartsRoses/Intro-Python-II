from room import Room
# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# Setup
yes_no = ["yes", "no"]
directions = ["west", "east", "north", "south", "quit"]
response = ""
current = rooms['outside']
while response not in directions:
    print(current)
    response = input(
        "What direction do you move?\nnorth/south/east/west/quit\n")
    if response == "north":
        if hasattr(current, 'n_to') == True:
            current = current.n_to
            response = ''
        else:
            print('you cannot go that way. choose a different route')
            response = ''
    elif response == "south":
        if hasattr(current, 's.to') == True:
            current = rooms[current].s_to
            response = ''
        else:
            print('you cannot go that way. choose a different route')
            response = ''
    elif response == "east":
        if hasattr(current, 'w.to') == True:
            current = rooms[current].e_to
            response = ''
        else:
            print('you cannot go that way. choose a different route')
            response = ''
    elif response == "west":
        if hasattr(current, 'w.to') == True:
            current = rooms[current].w_to
            response = ''
        else:
            print('you cannot go that way. choose a different route')
            response = ''
    elif response == "quit":
        print('see you next time!!')
        quit()
    else:
        print("I didn't understand that.\n")
        response = ''
