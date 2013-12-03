'''Card Game Coloretto'''
import random
# Data structure
# Objets : the deck : a list, 9 cards per colors, 6 colors, plus 10 "+2" cards and 3~jokers, and a last turn card.
# Cards gathered by players = lists
# Slots where players put cards they draw = a list of the slots. Each slot contains between 0 and 3 cards.
# Score table = a dictionary of scores given by a number of colored cards.

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
score_table = {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21}
last_turn = False

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

def convert_dict(cards):
    '''Takes in a list of cards and converts it in a dictionary with key = "type of card" and value = number of cards of that type. Returns the dictionary created. Will be used to display player's cards.'''
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

def print_board(slots, deck, cards_player, cards_CPU1, cards_CPU2):
    '''Prints the state of the game: slots with cards in them, cards the players have gathered and the number of remaining cards'''
    print("Remaining cards in deck: ",str(len(deck)))
    print("You have: ", convert_dict(cards_player))
    print("CPU1 has: ", convert_dict(cards_CPU1))
    print("CPU1 has: ", convert_dict(cards_CPU2))
    for i in range(0,len(slots)):
        print("Slot ",str(i + 1), " contains:","\n")
        for card in slots[i]:
            print(card, "\n")


def human_draw_card(deck, slots, last_turn):
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
        if card == "Last turn":
            print("OMG, this is the last turn!")
            last_turn = True
            card = deck.pop(0)
        print("The card you drew is ",card)
        print("Where do you want to put it?")
        print_board(slots, deck, cards_player, cards_CPU1, cards_CPU2)
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
        return deck, slots, last_turn

def human_pick_slot(slots, cards_player):
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

def compute_score(cards):
    '''Takes a list of cards as argument. Computes the score for these cards. Assigns Jocker cards to a color in order to maximize score, and add the value of the +2 cards.
    Returns score as an integer.'''
    score = 0
    #count_list will be a list of the number of colored cards hold. The three biggest numbers will add to the score, the other numbers will reduce the score according to the same table.
    count_list = []
    count_list.append(cards.count(color1))
    count_list.append(cards.count(color2))
    count_list.append(cards.count(color3))
    count_list.append(cards.count(color4))
    count_list.append(cards.count(color5))
    count_list.append(cards.count(color6))
    #order list by decreasing order
    count_list.sort(reverse=True)
    #jokers will hold the number of jokers to assign to a color. Having more than 6 cards of a color is not beneficial, so we check if there is a 5 in count_list, and if there is, add 1 to it and remove a joker. Else, we look for a 4, and so on. Fortunately, the count_list is already sorted as needed, so we only need to check its items starting from the first one.
    jokers = cards.count("Joker")
    while jokers > 0:
        for i in range(0, len(count_list)):
            if count_list[i] < 6:
                count_list[i] += 1
                jokers -= 1
                break
    # Now that the jokers are assigned to the best color possible, let's compute score from colored cards.
    for num in count_list[:3]:
        if num > 6:
            score += 21
        else:
            score += score_table[num]
    for num in count_list[3:]:
        if num > 6:
            score -= 21
        else:
            score -= score_table[num]

    # Add the value of all the "+2" cards.
    score += cards.count("+2") * 2
    return score

def ia_pick_or_draw(slots,cards):
    '''Used to chose picking a slot of cards, or drawing, for CPU. Returns "I pick." or "I draw.".'''
    # First check if all slots are either full or empty, and return the only legal move.
    all_slots_empty = True
    all_slots_full = True
    for i in range(0,len(slots)):
        if slots[i] != []:
            all_slots_empty = False
        if len(slots[i]) < 3:
            all_slots_full = False
    if all_slots_empty:
        return "I draw."
    if all_slots_full:
        return "I pick."
    # Let's use a threshold value to decide to pick. If a slot contains cards that would add threshold or more to my score, then decide to pick.
    threshold = 6
    for slot in slots:
        if compute_score(cards + slot) - compute_score(cards) >= threshold:
            return "I pick."
    return "I draw."

def ia_pick(slots, cards):
    '''Used to let ia pick the best slot, given his current cards. Computes the would-be score for each slot added to its current cards, and returns its cards and the new state of the slots.'''
    choices = []
    # todo: what if an empty slot gives the best score? Can't pick it by the rules! For now, assign a very low negative value to this case. Maybe find something more elegant later.
    for slot in slots:
        if slot == []:
            choices.append(-999)
        else:
            choices.append(compute_score(slot + cards))
    # choice is the index of the slot that gives the highest score with current cards hold.
    choice = choices.index(max(choices))
    print("I pick slot #",choice + 1)
    cards += slots[choice]
    slots.pop(choice)
    return slots, cards

def ia_draw(slots, deck, cards, last_turn):
    '''Used to let ia draw a card, and add it to a legal non full slot in slots. IA will chose a slot that would net him the best score if taken later, that's why I pass a list of cards hold at this point to compute score on them'''
    card = deck.pop(0)
    if card == "Last turn":
        print("OMG, this is the last turn!")
        last_turn = True
        card = deck.pop(0)
    print(" ".join(["The card is", card]))
    choices = []
    for slot in slots:
        if len(slot) >= 3:
            choices.append(-999)
        else:
            choices.append(compute_score(slot + cards))
    # choice is the index of the slot that gives the highest score with current cards hold.
    choice = choices.index(max(choices))
    # let's add the card to this slot
    print("I put it on slot #", choice + 1)
    slots[choice].append(card)
    return slots, deck, last_turn

def human_pick_or_draw(slots, deck):
    '''Prompts player to pick a slot of draw a card'''
    # First check if all slots are either full or empty, and return the only legal move.
    all_slots_empty = True
    all_slots_full = True
    for i in range(0,len(slots)):
        if slots[i] != []:
            all_slots_empty = False
        if len(slots[i]) < 3:
            all_slots_full = False
    if all_slots_empty:
        return "I draw."
    if all_slots_full:
        return "I pick."
    choice = ''
    while choice not in ['p','d']:
        choice = input("Do you want to [p]ick a slot or [d]raw a card? ")
    if choice == 'd':
        return "I draw."
    else:
        return "I pick."


    
# Debug zone
deck, cards_player, cards_CPU1, cards_CPU2 = game_start(deck, cards_player, cards_CPU1, cards_CPU2)
#print(deck)
slots = new_turn(num_players, slots)
print_board(slots, deck, cards_player, cards_CPU1, cards_CPU2)
deck, slots, last_turn = human_draw_card(deck, slots, last_turn)
#print(slots)
#slots, cards_player = pick_slot(slots,cards_player)
#print(compute_score(cards_player))
#print(compute_score(["Green","Green","Red","Red","Red","Red","Red","Red","Red","Green","Green","Green","Green","Joker","+2"]))
#print(ia_pick_or_draw([[1,2,3],["Green","Green","Red"],[1,2,3]],["Green"]))
#print(ia_pick([[],["Green","Jocker","+2"],["Green","Green","Red"]],["Green"]))
#print(ia_draw([[],["Green","+2"],["Green","Green"]],deck,["Green"]))
print(human_pick_or_draw(slots, deck))
