class Character:
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = []


from game import DEBUG
import random

def move(self):
    if random.choice([True, False]) is False:
        if DEBUG:
            print(f"DEBUG: {self.name} reste dans la pièce {self.current_room.name}")
        return False

    adjacent_rooms = list(self.current_room.exits.values())
    
    if not adjacent_rooms:
        if DEBUG:
            print(f"DEBUG: {self.nam} ne peut pas se déplacer (aucune sortie depuis {self.current_room.name})")
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
    if not self.msgs:
        print(f"{self.name} n’a rien à dire.")
        return

    msg = self.msgs.pop(0)

    print(f"{self.name} dit : {msg}")

    self.msgs.append(msg)




    
    

