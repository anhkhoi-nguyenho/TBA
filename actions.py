# Description: The actions module.


# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.




# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG2 = "\nLa commande '{command_word}' prend 2 paramètres.\n"


class Actions:


    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a direction defined as follow (F, B, R, L, U, D ).
        F = foward
        B = back
        R = right
        L = left
        U = upstairs
        D = downstairs


        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.


        Returns:
            bool: True if the command was executed successfully, False otherwise.


        Examples:
       
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False


        """
       
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False


        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        print(player.get_history())
        return True


    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.


        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.


        Returns:
            bool: True if the command was executed successfully, False otherwise.


        Examples:


        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False


        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
       
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nThank you, {player.name}, for playing this game. Good Bye !\n"
        print(msg)
        game.finished = True
        return True


    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
       
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.


        Returns:
            bool: True if the command was executed successfully, False otherwise.


        Examples:


        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False


        """


        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
       
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True


    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.
        """
        # Vérifier que la commande n'a pas de paramètre supplémentaire
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False


        # Afficher l'historique via la méthode du Player          
        print(game.player.get_history())
        return True


    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir à la pièce précédente.
        """
        # Vérification du nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False


        player = game.player
        # Vérifier si l'historique contient au moins une pièce
        if not player.history:
            print("\nAucune pièce précédente.\n")
            return False
       
        # Revenir à la pièce précédente
        player.current_room = player.history.pop()  # récupère la dernière pièce visitée
        print(player.current_room.get_long_description())  # description de la nouvelle pièce
       
        # Afficher l'historique mis à jour
        print(player.get_history())
        return True
   
    def look(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        current_room = game.player.current_room
        current_room_inventory = current_room.inventory
        print("\nYou are in", current_room.description)
        print(current_room_inventory.get_inventory(0))    # Reminder : 0 = room; 1 = player

        # Display of NPCs
        s = "There is no character here"

        if game.player.current_room.characters :
            s = ""
            for character in game.player.current_room.characters:
                    s += "\n\t- {}".format(character)

        print(s)

        return True


    def talk(game, list_of_words, number_of_parameters):


        """if len(list_of_words) != number_of_parameters + 1:
            print(yes)
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
        return False"""


        name = list_of_words[1].lower()
        room = game.player.current_room


        found = False
        for npc_name, npc in room.characters.items():
            if npc_name.lower() == name:
                npc.get_msg()
                found = True
                break


        if not found:
            if room.characters:
                print("Il n'y a personne de ce nom ici. PNJ présents :", ", ".join(room.characters.keys()))
            else:
                print("Il n'y a aucun personnage ici.")
            return False
        return True

    def take(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            print(l)
            print(number_of_parameters + 1)
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        player_inventory = player.inventory.contained_items
        current_room_inventory = player.current_room.inventory.contained_items

        # Get the item to take from the list of words.
        to_take = list_of_words[1]

        if to_take in current_room_inventory:

            if not current_room_inventory[to_take].movable:
                print(f"\n{to_take} can not be moved and is not added to your bag.")
                return False

            to_take_weight = current_room_inventory[to_take].weight

            if to_take_weight > player.max_weight:
                print("\nYour bag is too heavy to add {}".format(to_take))
                print("Remove {} kg to add the new item".format(to_take_weight - player.max_weight))
                return False

            player_inventory[to_take] = current_room_inventory[to_take]
            print("\n{} is added to your bag".format(to_take))
            player.max_weight -= to_take_weight
            del current_room_inventory[to_take]
            return True

        print(to_take, "is not in the current location !")
        return False

    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            print(l)
            print(number_of_parameters + 1)
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        player_inventory = player.inventory.contained_items
        current_room_inventory = player.current_room.inventory.contained_items

        # Get the item to take from the list of words.
        to_drop = list_of_words[1]

        if to_drop in player_inventory:
            current_room_inventory[to_drop] = player_inventory[to_drop]
            print("\n{} is removed from your bag".format(to_drop))
            player.max_weight += player_inventory[to_drop].weight
            del player_inventory[to_drop]
            return True

        print(to_drop, "is not in your bag !")
        return False
    
    def check(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player_inventory = game.player.inventory
        print(player_inventory.get_inventory(1))    # Reminder : 0 = room; 1 = player
        return True

    def read(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            print(l)
            print(number_of_parameters + 1)
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        to_read = list_of_words[1]

        player_inventory = game.player.inventory.contained_items
        current_room_inventory = game.player.current_room.inventory.contained_items

        if to_read in player_inventory:
            print(player_inventory[to_read].text)   # By default, obj.text = "Nothing to read !"
        elif to_read in current_room_inventory:
            print(current_room_inventory[to_read].text)
        else:
            print(f"{to_read} is neither in your back nor in the current location !")
            return False

    def inspect(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            print(l)
            print(number_of_parameters + 1)
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        to_inspect = list_of_words[1]

        player_inventory = game.player.inventory.contained_items
        current_room_inventory = game.player.current_room.inventory.contained_items

        if to_inspect in player_inventory:
            
            contained_items = player_inventory[to_inspect].contained_items

        elif to_inspect in current_room_inventory:

            contained_items = current_room_inventory[to_inspect].contained_items
            
        else:
            print(f"{to_inspect} is neither in your back nor in the current location !")
            return False
        
        s = "\nNothing found !"

        if contained_items:
            s = f"\n{to_inspect} has following items:"
            for child_item in contained_items:
                    s += f"\n\t- {child_item}"
                    current_room_inventory[child_item.name] = child_item
        
        print(s)

    def compare(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            print(l)
            print(number_of_parameters + 1)
            command_word = list_of_words[0]
            print(MSG2.format(command_word=command_word))
            return False

        state = True

        player_inventory = game.player.inventory.contained_items
        current_room_inventory = game.player.current_room.inventory.contained_items

        biometrics1 = list_of_words[1]
        biometrics2 = list_of_words[2]

        if biometrics1 in player_inventory:
            UID1 = player_inventory[biometrics1].biometricsUID
        elif biometrics1 in current_room_inventory:
            UID1 = current_room_inventory[biometrics1].biometricsUID
        else:
            print(f"\n{biometrics1} is neither in your back nor in the current location !")
            state = False

        if not UID1:    # UD1 = None
            print(f"\nThere is no biometrics data in {biometrics1}")
            state = False

        if biometrics2 in player_inventory:
            UID2 = player_inventory[biometrics2].biometricsUID
        elif biometrics2 in current_room_inventory:
            UID2 = current_room_inventory[biometrics2].biometricsUID
        else:
            print(f"\n{biometrics2} is neither in your back nor in the current location !")
            state = False
        
        if not UID2:    # UD2 = None
            print(f"\nThere is no biometrics data in {biometrics2}")
            state = False
        
        if state:
            print("\nIdentical !") if UID1 == UID2 else print("\nDifferent !")

        return state
    
    def unseal(game, list_of_words, number_of_parameters):

        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            print(l)
            print(number_of_parameters + 1)
            command_word = list_of_words[0]
            print(MSG2.format(command_word=command_word))
            return False
        
        to_unseal = list_of_words[1]
        code = list_of_words[2]

        player_inventory = game.player.inventory.contained_items
        current_room_inventory = game.player.current_room.inventory.contained_items

        secret = None
        if to_unseal in player_inventory:
            
            if player_inventory[to_unseal].sealed_code == code:
                secret = player_inventory[to_unseal].sealed_secret

        elif to_unseal in current_room_inventory:

            if current_room_inventory[to_unseal].sealed_code == code:
                secret = current_room_inventory[to_unseal].sealed_secret
            
        else:
            print(f"{to_unseal} is neither in your back nor in the current location !")
            return False
        
        s = "\nWrong code or there is no secret to reveal !"
        if secret:
            s = f"\n{to_unseal} has following secrets:"
            for child_item in secret:
                    s += f"\n\t- {child_item}"
                    current_room_inventory[child_item.name] = child_item
        
        print(s)
