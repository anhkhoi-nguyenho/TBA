"""
This file contains Item class

Code Author : Anh Khoi NGUYEN HO
Docstrings Author : Anh Khoi NGUYEN HO
"""
class Item:
    """
    This class is used to create different items in the game

    Attributes:
        Name (str): name of the item
        Descirption (Str): descirption of the item
        Weight (int): weight in kg of the item
        Text (int): for items having text, writings to read
        Contained_items (list): list of contained child item; default None
        Movable (bool): boolean - whether the item can be moved; default True
        BiometricsUID (uuid.UUID): UID generated with uuid.uuid4(); default None
        Sealed_secret (list): list of child items locked with a code; default None
        Sealed_code (str): the code required to unlock sealed child items 

    Method:
        __init__(self, name, description, weight, movable) : constructor
        __str__(self) : redefine interaction with print()
    """
    def __init__(self, name, description, weight, movable= True):


        self.name                       = name
        self.description                = description
        self.weight                     = weight
        self.text                       = "Nothing to read !"   # Default value
        self.contained_items            = None
        self.movable                    = movable
        self.biometricsUID              = None
        self.sealed_secret              = None
        self.sealed_code                = None

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
class Inventory:
    """
    Define inventory instance for Player and Room class
    
    Attributes :
        Contained_items(dict) : dictionnary of contained items
    
    Method :
        __init__(self): constructor
        get_inventory(self, parentCategory): dynamically format a string to display contained items
    """
    def __init__(self):
        self.contained_items = {}

    def get_inventory(self, parent_category):
        """
        Format a string for display depending on the class of parent object
        parentCategory : 0 = room, 1 = player
        """
        if self.contained_items:
            if parent_category :
                s = "\nYou have the following items:"
            else:
                s = "\nThere is:"

            for item in self.contained_items.values():
                s += f"\n\t- {item}"

            return s

        return "\nYour bag is empty" if parent_category else "There is nothing here"
