# Description: Game class


# Import modules


from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item, Inventory
from character import Character


DEBUG = True


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
        look = Command("look", " : observer l'environnement", Actions.look, 0)
        self.commands["look"] = look
        talk = Command("talk", " <nom> : parler à un personnage", Actions.talk, 1)
        self.commands["talk"] = talk




       
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
        bus_station           = Room("Bus station","the Rainhood's bus station")
        psychiatric_hospital    = Room("Psychiatric hospital", "the Rainhood's psychiatric hospital")
        street1                 = Room("Street1", "Street in fornt of the hero's house")
        street2                 = Room("Street2", "Street2 foward the bridge")
        street3                 = Room("Street3", "Street at the left of the bridge")
         # Setup NPCs
        barman = Character("Barman", "The bar's barman", bar, ["what can I get you?", "I heard people talking about it and the only clue I can give is: the stone in the air hover the river"])
        shopkeeper = Character("Shopkeeper", "The shoes shop's shopkeeper", shoes_shop, ["Welcome to my shop!", "Okay let me check in stock if Ihave something like this","I found this model","Yeah, it seems o me that someone bought it one or two weeks ago"])
        neighbour_wife = Character("Neighbour_s_wife", "The hero's neighbour's wife", neighbour_s_house, ["I'm so sorry for the death of your wife. If you need anything, just let me know.","Yes of course! Have a sit, just give us a momet to bring you some drink"])
        neighbour_husband = Character("Neighbour_s_husband", "The hero's neighbour's husband", neighbour_s_house, ["Hello Eric", "It's a hard time for all of us."])
        forest_guard = Character("Forest_guard", "The park's forest guard", park, ["Hello mister, I remember your wife, and i think at the lost and found there is something that belongs to her.","Yes! Is this bracelet her’s?"])
        chief_inspector = Character("Chief_Inspector", "The chief inspector at the police station ", police_station, ["Hello, let me have a look. Is it your wife’s bracelet?", " Thank you for your help.","If you want it should go to archives"])
        archivist = Character("Achivist", "The archivist at the national archives", archives, ["let me check our records for you.", "Here are the documents you requested."])
        psychiatrist = Character("Psyachiatrist", "The hero's former psychiatrist", doctor_s_surgery, ["How have you been since our last session? Are you okay to let me hypnotize you again?", "So let’s begin. Follow the pendulum with your eyes forget everything…"])
        station_master = Character("Station_Master", "The bus station's station master", bus_station, ["I’m sorry I’ve never see her and I was working that day, and I’m sure she doesn’t take any bus"])
        doctor = Character("Doctor", " A doctor at the psyachiatric hospital", psychiatric_hospital, ["You need help Eric, your psychiatrist send us your exam, and now we are here to help you", " so tell us who murdered Sarah?"])




        bar.characters[barman.name ] = barman
        shoes_shop.characters[shopkeeper.name] = shopkeeper
        neighbour_s_house.characters[neighbour_wife.name] = neighbour_wife
        neighbour_s_house.characters[neighbour_husband.name] = neighbour_husband
        park.characters[forest_guard.name] = forest_guard
        police_station.characters[chief_inspector.name] = chief_inspector
        archives.characters[archivist.name] = archivist
        doctor_s_surgery.characters[psychiatrist.name] = psychiatrist
        bus_station.characters[station_master.name] = station_master
        psychiatric_hospital.characters[doctor.name] = doctor




       






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
        self.rooms.append(bus_station)
        self.rooms.append(psychiatric_hospital)
        self.rooms.append(stree1)
        self.rooms.append(Street2)
        self.rooms.append(Street3)
        """


        # Initialize inventory of rooms
        house.inventory                     = Inventory()
        library.inventory                   = Inventory()
        bar.inventory                       = Inventory()
        bridge.inventory                    = Inventory()
        shoes_shop.inventory                = Inventory()
        neighbour_s_house.inventory         = Inventory()
        park.inventory                      = Inventory()
        police_station.inventory            = Inventory()
        archives.inventory                  = Inventory()
        doctor_s_surgery.inventory          = Inventory()
        abandoned_hotel.inventory           = Inventory()
        bus_station.inventory             = Inventory()
        psychiatric_hospital                = Inventory()
        street1                             = Inventory()
        street2                             = Inventory()
        street3                 = Room("Street3", "Street at the left od the bridge")


        # Create different items
        Sarah_Journey = Item("Sarah's journey", "A personal journey of Sarah", weight=0.5, category=0)
        Sarah_Journey.text = "1/12/1999 - Eric was made, his condition has worsened since our last conversation"
        HiddenItem1 = Item("Hidden letter", "A hidden letter", weight=0.018, category=1)
        HiddenItem1.text = "This is a secret"
        TestItem = Item("Sample 0", "A sample object", weight=0, category=0, containingSecret=True)
        TestItem.text = "Draft text"
        TestItem.secretList = [HiddenItem1]
       
        # Add items to rooms inventory
        house.inventory.items[Sarah_Journey.name] = Sarah_Journey
        house.inventory.items[TestItem.name] = TestItem


        # Create PNJ
       


        # Add PNJ to rooms
        # syntax : house.characters[objPNJ.name] = objPNJ


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
            "F": bus_station,
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
            "L": bus_station,
            "R": None,
            "I": None,
            "O": None
        }


        bus_station.exits = {
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
            "L": bus_station,
            "R": None,
            "I": None,
            "O": None
        }


        # Setup player and starting room


        self.player = Player(input("\nEnter your name: "))
        self.player.current_room = house
        self.player.inventory = Inventory()


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



