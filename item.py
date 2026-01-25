class Item:

    def __init__(self, name, description, weight, movable= True):

        self.name                       = name
        self.description                = description
        self.weight                     = weight
        self.text                       = "Nothing to read !"   # Default value
        self.secretList                 = []
        self.movable                    = movable
        self.biometricstUID             = None
        self.child_items                = []

    def __str__(self):
        return "{} : {} ({} kg)".format(self.name, self.description, self.weight)

class Inventory:

    def __init__(self):
        self.contained_items = {}
    
    def get_inventory(self, parentCategory):      # parentCategory : 0 = room, 1 = player
        if self.contained_items:
            if parentCategory :
                s = "\nYou have the following items:"
            else:
                s = "\nThere is:"
            
            for item_name in self.contained_items:
                s += "\n- {}".format(self.contained_items[item_name])
            
            return s     
        
        return "\nYour bag is empty" if parentCategory else "There is nothing here"