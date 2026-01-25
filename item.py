class Item:

    def __init__(self, name, description, weight, category, containingSecret= False):

        # Defining generic attributes

        self.name                       = name
        self.description                = description
        self.weight                     = weight
        self.containingSecret           = containingSecret      # True or False

        # Defining specific attributes without using subclass, initialized as empty

        if category == 0 or category == 1:      # Book or Letter
            
            self.text                   = ""

            if containingSecret:
                self.secretList = []
            
            self.movable                = True


        # Shoes or glass or footprint or fingerprint
        elif category == 2 or category == 3 or category == 4 or category == 5:    

            self.biometricstUID         = None

            if category == 2 or category == 3:
                self.movable            = True
            else:
                self.movable            = False

                def checkMatching(self, parentObject):
                    return self.biometricsUID == parentObject.biometricsUID

        elif category == 6:                     # Folder

            self.content                = []
            self.movable                = True

        elif category == 7 or category == 8 :   # Drawer or bookcase

            self.content                = []
            self.movable                = False

            if containingSecret:
                self.secretList = [] 

        else :
            print("Error - Attempt to create unknown item of category {}".format(category))
            print("Error - Please remove unknown item from game setup")
            print("Error - The game will now exit")
            exit(-1)


    def __str__(self):
        return "{} : {} ({} kg)".format(self.name, self.description, self.weight)


    def search(self):
        
        if self.containingSecret:
            return self.secretList

        return None

class Inventory:

    def __init__(self):
        self.items = {}
    
    def get_inventory(self, parentCategory):      # parentCategory : 0 = room, 1 = player
        if self.items:
            if parentCategory :
                s = "You have the following items:"
            else:
                s = "The room contains:"
            
            for key in self.items:
                s += "\n- {}".format(self.items[key])

            return s
        
        return "Your bag is empty" if parentCategory else "Nothing here"