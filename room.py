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
        get_exit_string(self) : Return a string describing possible exits. In version 1, this string contains possible exit directions.
        get_long_description(self) : Return a string describing current place including possible exits.
    
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
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
