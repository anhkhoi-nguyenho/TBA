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
        # self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction (F, B, R, L, I, O)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        
        # Setup rooms

        house                   = Room("House", "the hero's house")
        library                 = Room("Library", "a room with boocks in the hero's house")
        bar                     = Room("Bar", "the Rainhood main bar")
        bridge                  = Room("Bridge", "the bridge where they found the Sarah's lifeless body" )
        shoes_shop              = Room("Shoes shop", "the hugest shoes shop of Rainhood")
        neighbour_s_house       = Room("Neighbour's house", "the house of the neighbours of the hero")
        park                    = Room("Park","the local park")
        police_station          = Room("Police station","police station of Rainhood")
        archives                = Room("Archives", "national archives")
        doctor_s_surgery        = Room("Doctor's surgery","the surgery of the former Eric's psychiatrist ")
        abandoned_hotel         = Room("Abandoned hotel","hotel where the couple did its honeymoon")
        train_station           = Room("Train station","the Rainhood's train station")
        psychiatric_hospital    = Room("Psychiatric hospital", "the Rainhood's psychiatric hospital")
        street1                 = Room("Street1", "Street in fornt of the hero's house")
        street2                 = Room("Street2", "Street2 foward the bridge")
        street3                 = Room("Street3", "Street at the left od the bridge")

        """
        Currently not needed - Append room to rooms list
        self.rooms.append(house)
        self.rooms.append(library)
        self.rooms.append(bar)
        self.rooms.append(bridge)
        self.rooms.append(shoes_shop)
        self.rooms.append(neighbour_s_house)
        self.rooms.append(park)
        self.rooms.append(police_station)
        self.rooms.append(archives)
        self.rooms.append(doctor_s_surgery)
        self.rooms.append(abandoned_hotel)
        self.rooms.append(train_station)
        self.rooms.append(psychiatric_hospital)
        self.rooms.append(stree1)
        self.rooms.append(Street2)
        self.rooms.append(Street3)
        """

        # Create exits for rooms

        house.exits = {
            "B": None, 
            "F": neighbour_s_house, 
            "L": None, 
            "R": street1,
            "I": library,
            "O": None
        }
        
        library.exits = {
            "B": None,
            "F": None,
            "L": None,
            "R": None,
            "I": None,
            "O": house
        }

        neighbour_s_house.exits = {
            "B": house, 
            "F": street3, 
            "L": None, 
            "R": None,
            "I": None,
            "O": None
        }
        
        street1.exits = {
            "B": None, 
            "F": bar, 
            "L": house, 
            "R": None,
            "I": None,
            "O": None
        }
        
        bar.exits = {
            "B": street1, 
            "F": bridge, 
            "L": None, 
            "R": None,
            "I": None,
            "O": None
        }
        
        bridge.exits = {
            "B": bar, 
            "F": street2, 
            "L": street3, 
            "R": abandoned_hotel,
            "I": None,
            "O": None
        }
        
        street2.exits = {
            "B": bridge, 
            "F": police_station, 
            "L": park, 
            "R": shoes_shop,
            "I": None,
            "O": None
        }
        
        street3.exits = {
            "B": None, 
            "F":park,
            "L": neighbour_s_house,
            "R": bridge,
            "I": None,
            "O": None
        }
        
        shoes_shop.exits = {
            "B": abandoned_hotel,
            "F": doctor_s_surgery, 
            "L": street2, 
            "R": None,
            "I": None,
            "O": None
        }

        park.exits = {
            "B": street3, 
            "F": police_station,
            "L": None, 
            "R": street2,
            "I": None,
            "O": None
        }

        police_station.exits = {
            "B": street2, 
            "F": train_station, 
            "L": park, 
            "R": doctor_s_surgery,
            "I": None,
            "O": None
        }

        archives.exits = {
            "B": psychiatric_hospital, 
            "F": None, 
            "L": None, 
            "R": None,
            "I": None,
            "O": None
        }
        
        doctor_s_surgery.exits = {
            "B": shoes_shop, 
            "F": psychiatric_hospital, 
            "L": police_station, 
            "R": None,
            "I": None,
            "O": None
        }
        
        abandoned_hotel.exits = {
            "B": doctor_s_surgery, 
            "F": archives, 
            "L": train_station, 
            "R": None,
            "I": None,
            "O": None
        }
        
        train_station.exits = {
            "B": police_station, 
            "F": None, 
            "L": None, 
            "R": None,
            "I": None,
            "O": None
        }
        
        psychiatric_hospital.exits = {
            "B": doctor_s_surgery, 
            "F": archives, 
            "L": train_station, 
            "R": None,
            "I": None,
            "O": None
        }

        # Setup player and starting room

        self.player = Player(input("\nEnter your name: "))
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
                print(f"\nUnrecognized '{command_word}' command. Type 'help' for possible commands.\n")
            # If the command is recognized, execute it
            else:
                command = self.commands[command_word]
                command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nWelcome player {self.player.name}!")
        print(f"In this world, you are Eric.")
        print(f"Let's uncover the truth about your wife's death!")
        print("\nType 'help' to for possible commands.")

        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
