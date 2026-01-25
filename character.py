"""
This file contains the Character class.

Code author : Edeline MONDESIR
Docstring author : Anh Khoi NGUYEN HO
Syntax improvement : Anh Khoi NGUYE HO
"""
import random
DEBUG = True


class Character:
    """
    Character is used to create NPC in the game

    Attributes:
        name(str): name of the NPC
        description(str): description about the NPC
        current_room(Room): current location of the NPC
        msgs(list): list of messages of the NPC
    
    Method:
        __init__(self, name): the constructor
        move(self, direction): dynamically change the location of the player
        __str__(self): redefine how print() interact with an instance of this class
        get_msg(self): handle the display of messages from NCP 
    """

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def move(self):
        """
        This 
        """
        if random.choice([True, False]) is False:
            if DEBUG:
                print(f"DEBUG: {self.name} reste dans la pièce {self.current_room.name}")
            return False


        adjacent_rooms = list(self.current_room.exits.values())

        if not adjacent_rooms:
            if DEBUG:
                print(f"DEBUG: {self.name} ne peut pas se déplacer", end="")
                print(f" (aucune sortie depuis {self.current_room.name})")
            return False


        new_room = random.choice(adjacent_rooms)


        if DEBUG:
            print(f"DEBUG: {self.name} se déplace de {self.current_room.name} vers {new_room.name}")


        self.current_room.characters.remove(self)


        new_room.characters.append(self)


        self.current_room = new_room

        return True


    def __str__(self):
        return f"{self.name} : {self.description}"


    def get_msg(self):
        """
        Format and display messages of NPC
        """
        if not self.msgs:
            print(f"{self.name} n’a rien à dire.")
            return


        msg = self.msgs.pop(0)


        print(f"{self.name} dit : {msg}")


        self.msgs.append(msg)
