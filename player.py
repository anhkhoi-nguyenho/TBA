from item import Inventory
# Define the Player class.
class Player():
    """
    This class is used to create a player,
    In a first time it memorizes the player name,
    Next, it indicates it doesn't have room yet
    After it defines the way the player move and looks for the next room it will go
    If there's no exit -> send an error message("Aucune porte dans cette direction !") and return False
    In the other case it changes the player room and print the new room's description


    Attributes:
        Name (str): The name of the player
        Current_room(Room): The  room where the player is 
    
    Method:
        __init__(self, name): The constructor
        move(self, direction): Return False if there is no room into this direction and return if there is a room

    Examples:
    >>> player1 = "Anh Khoi"

    Curent_room 
    >>> Curent_room = None
    """
    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = Inventory()
        self.max_weight = 10
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Save current room into history before moving.
        if self.current_room is not None:
            self.history.append(self.current_room)

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        """Return a string representing the history of visited rooms.

        The history contains previously visited rooms in chronological order
        and includes the current room as the last entry when available.
        """
        if self.history == []:
            return "\nNo history available.\n"

        s = "\nYou have visited the following rooms:\n"
        for room in self.history:
            s += "\n\t- {}".format(room.description)
        return s