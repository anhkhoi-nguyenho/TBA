"""
This file containes Room class
"""
from item import Inventory
# Define the Room class.
class Room:
    """
    This class is used to define different places in the game.
    Each place is identified by its name.
    A description about the place is also given.
    This class also defines adjacently connected places.

    Attributes:
        name (str): The name of the place.
        description (str): The description about the place.
        exits (dict) : The dictionnary containing connected places informations.

    Methods:
        __init__(self, name, description) : The constructor defining attributes.
        get_exit(self, direction) : Return the exit place corresponding to the given direction
        get_exit_string(self) : Return a string describing possible exits.
        get_long_description(self) : Return a string describing current place and possible exits.
   
    Examples:

    >>> room1 = Room("Generic Room 1", "dans Generic room 1 example." )
    >>> room2 = Room("Generic Room 2", "dans Generic room 2 example." )
    >>> room1.name
    'Generic Room 1'
    >>> room1.description
    'dans Generic room 1 example.'
    >>> room1.exits = {"N" : room2, "E" : None, "S" : None, "O" : None}
    """

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = Inventory()
        self.characters = {}

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Method to obtain possible exits
        """
        # Return the room in the given direction if it exists.
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Format a string to display possible exits
        """
        exit_string = "Exits: "
        for _exit in self.exits:
            if self.exits.get(_exit) is not None:
                exit_string += _exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Format a string to display the description of the current location
        and possible exits
        """
        return f"\nYou are in {self.description}\n\n{self.get_exit_string()}"
