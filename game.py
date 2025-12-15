# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        #forest = Room("Forest", "une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        #self.rooms.append(forest)
        #tower = Room("Tower", "une immense tour en pierre qui s'élève au dessus des nuages.")
        #self.rooms.append(tower)
        #cave = Room("Cave", "une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        #self.rooms.append(cave)
        #cottage = Room("Cottage", "un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        #self.rooms.append(cottage)
        #swamp = Room("Swamp", "un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        #self.rooms.append(swamp)
        #castle = Room("Castle", "un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        #self.rooms.append(castle)
        house = Room("House", "the hero's house") 
        #self.rooms.append(house)
        library = Room("Library", "a room with boocks in the hero's house")
        #self.rooms.append(library)
        bar = Room("Bar", "the Rainhood main bar")
        #self.rooms.append(bar)
        bridge = Room("Bridge", "the bridge where they found the Sarah's lifeless body" )
        #self.rooms.append(bridge)
        shoes_shop = Room("Shoes shop", "the hugest shoes shop of Rainhood")
        #self.rooms.append(shoes_shop)
        neighbour_s_house = Room("Neighbour's house", "the house of the neighbours of the hero")
        #self.rooms.append(neighbour_s_house)
        park = Room("Park","the local park")
        #self.rooms.append(park)
        police_station = Room("Police station","police station of Rainhood")
        #self.rooms.append(police_station)
        archives = Room("Archives", "national archives")
        #self.rooms.append(archives)
        doctor_s_surgery = Room("Doctor's surgery","the surgery of the former Eric's psychiatrist ")
        #self.rooms.append(doctor_s_surgery)
        abandoned_hotel = Room("Abandoned hotel","hotel where the couple did its honeymoon")
        #self.rooms.append(abandoned_hotel)
        train_station = Room("Train station","the Rainhood's train station")
        #self.rooms.append(train_station)
        psychiatric_hospital = Room("Psychiatric hospital", "the Rainhood's psychiatric hospital")
        #self.rooms.append(psychiatric_hospital)
        street1 = Room("Street1", "Street in fornt of the hero's house")
        #self.rooms.append(stree1)
        street2 = Room("Street2", "Street2 foward the bridge")
        #self.rooms.append(Street2)
        street3 = Room("Street3", "Street at the left od the bridge")


        # Create exits for rooms

        #forest.exits = {"N" : cave, "E" : None, "S" : castle, "O" : None}
        #tower.exits = {"N" : cottage, "E" : None, "S" : None, "O" : None}
        #cave.exits = {"N" : None, "E" : cottage, "S" : forest, "O" : None}
        #cottage.exits = {"N" : None, "E" : None, "S" : tower, "O" : cave}
        #swamp.exits = {"N" : tower, "E" : None, "S" : None, "O" : castle}
        #castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}
        house.exits = {"B": None, "F": neighbour_s_house, "L": None, "R": street1,}
        neighbour_s_house = {"B": house, "F": street3, "L": None, "R": None}
        street1.exits = {"B": None, "F": bar, "L": house, "R": None}
        bar.exits = {"B": street1, "F": bridge, "L": None, "R": None}
        bridge.exits = {"B": bar, "F": street2, "L": street3, "R": abandoned_hotel}
        street2 = {"B": bridge, "F": police_station, "L": park, "R": shoes_shop}
        street3 = {"B": None, "F":park,"L": neighbour_s_house, "R": bridge}
        shoes_shop.exits = {"B": abandoned_hotel,"F": doctor_s_surgery, "L": street2, "R":None}
        park.exits = {"B": street3, "F": police_station,"L": None, "R": street2}
        police_station.exits = {"B": street2, "F": train_station, "L": park, "R": doctor_s_surgery}
        archives.exits = {"B": psychiatric_hospital, "F": None, "L": None, "R": None}
        doctor_s_surgery.exits = {"B": shoes_shop, "F": psychiatric_hospital, "L": police_station, "R": None}
        abandoned_hotel.exits = {"B": doctor_s_surgery, "F": archives, "L": train_station, "R": None}
        train_station.exits = {"B": police_station, "F": None, "L": None, "R": None}
        psychiatric_hospital.exits = {"B": doctor_s_surgery, "F": archives, "L": train_station, "R": None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = house

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # Only handle the command if it is not empty  
        if command_word != "":
            # If the command is not recognized, print an error message
            if command_word not in self.commands.keys():
                print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
