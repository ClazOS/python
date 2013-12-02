'''Card Game Coloretto'''
import random
# Structure des données
# Objets : le deck : une liste ? 9 cards par colors, 6 colors
# Les cards récupérées par les joueurs : listes ?
# les slots sur lesquels il y a des cards : listes ?
# La table : une liste des listes qui représentent les slots
num_players = 3
deck = []
cards_player = []
cards_CPU1 = []
cards_CPU2 = []
slots = []
color1 = "Red"
color2 = "Green"
color3 = "Yellow"
color4 = "Blue"
color5 = "Gray"
color6 = "Black"
# Fonctions nécessaires
# Dessiner le plateau
# Jouer un tour
# Prendre un paquet
# Piocher une carte
# IA
# Compter les scores

def deck_regen(deck):
    '''Takes a deck and restores it to the initial state to begin a new game. Returns the new deck.'''
    deck = []
    for i in range(0, 9):
        deck.append(color1)
        deck.append(color2)
        deck.append(color3)
        deck.append(color4)
        deck.append(color5)
        deck.append(color6)
    for i in range(0,3):
        deck.append("Joker")
    for i in range(0,10):
        deck.append("+2")
    random.shuffle(deck)
    deck.insert(-15,"Last turn")
    return deck

def new_turn(num_players, slots):
    '''Prepares slots according to number of players. Returns slots, the content of the table'''
    #Let's empty slots just in case
    slots = []
    for i in range(0, num_players):
        slots.append([])
    #Slots is a list of empty lists at the beginning of a turn. These empty lists will fill with cards, up to 3.
    return slots

def game_start(deck, cards_player, cards_CPU1, cards_CPU2):
    '''Regens the deck, and gives each player their first card. Returns the deck, cards for the human player, and cards for CPU1 and CPU2'''
    deck = deck_regen(deck)
    # Now, give each player a card of a different color, from the deck
    deck.remove('Red')
    cards_player.append('Red')
    deck.remove('Green')
    cards_CPU1.append('Green')
    deck.remove('Yellow')
    cards_CPU1.append('Yellow')
    return deck, cards_player, cards_CPU1, cards_CPU2

def print_board(slots, deck):
    '''Prints the state of the game: slots with cards in them, and the number of remaining cards'''
    print("Remaining cards in deck: ",str(len(deck)))
    for i in range(0,len(slots)):
        print("Slot ",str(i + 1), " contains:","\n")
        for card in slots[i]:
            print(card, "\n")

def draw_card(deck, slots):
    '''Lets human player draw a card, look at it, and select a slot to put it'''
    # First, check if remaining slots are not full (3 cards). If so, draw_card returns the deck and slots unchanged.
    test = 0
    for slot in slots:
        if len(slot) == 3:
            test += 1
    if test == len(slots):
        print()
        print("All slots are full, you can't draw a card!")
        print()
        return deck, slots
    # Now that we now we are good
    else:
        card = deck.pop(0)
        print("The card you drew is ",card)
        print("Where do you want to put it?")
        print_board(slots, deck)
        choice = ''
        choices = []
        # populates choices list with valid choices as strings
        for i in range(0, len(slots)):
            if len(slots[i]) < 3:
                choices.append(str(i + 1))
        # checks if inputed choice is a member of the list of valid choices
        while choice not in choices:
            choice = input("Choose a slot to put your card: ")
        choice = int(choice) - 1
        slots[choice].append(card)
        return deck, slots

def pick_slot(slots, cards_player):
    '''Lets human player pick a slot of cards, and add these cards to its cards. Updates slots'''
    choice = ''
    choices = []
    # populates choices list with valid choices as strings
    for i in range(0,len(slots)):
        if slots[i] != []:
            choices.append(str(i + 1))
    # checks if inputed choice is a member of the list of valid choices
    while choice not in choices:
        print("You have these cards:")
        print(cards_player)
        choice = input("Choose the slot you want to draw: ")
    choice = int(choice) - 1
    cards_player += slots[choice]
    print("You now have: ", cards_player)
    del slots[choice]
    return slots, cards_player

def convert_dict(cards):
    '''Takes in a list of cards and converts it in a dictionary with key = "type of card" and value = number of cards of that type. Returns the dictionary created. Will be used to display player's cards and compute the score(maybe).'''
    d = {}
    d[color1] = cards.count(color1)
    d[color2] = cards.count(color2)
    d[color3] = cards.count(color3)
    d[color4] = cards.count(color4)
    d[color5] = cards.count(color5)
    d[color6] = cards.count(color6)
    d["Jocker"] = cards.count("Joker")
    d["+2"] = cards.count("+2")
    return d


# Debug zone
deck, cards_player, cards_CPU1, cards_CPU2 = game_start(deck, cards_player, cards_CPU1, cards_CPU2)
print(deck)
slots = new_turn(num_players, slots)
print_board(slots,deck)
deck, slots = draw_card(deck, slots)
print(slots)
slots, cards_player = pick_slot(slots,cards_player)
cards_player_dict = convert_dict(cards_player)
print (cards_player_dict)
