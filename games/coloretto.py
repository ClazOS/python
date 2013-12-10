'''Card Game Coloretto'''
import random
# Data structure
# Objets : the deck : a list, 9 cards per colors, 6 colors, plus 10 "+2" cards and 3 jokers, and a last turn card.
# Cards gathered by players = lists
# Slots where players put cards they draw = a list of the slots. Each slot contains between 0 and 3 cards.
# Score table = a dictionary of scores given by a number of colored cards.
# last_turn = boolean to check if the last turn card was drawn and the game should stop
# human_picked, CPU1_picked, CPU2_picked = booleans to check if players are still active in a given turn.


# TODO: deal with the turn order : last player to pick should be first to draw
# TODO: improve the text output of CPU functions
# TODO: make number of CPU and human variable, up to 5 players in total.

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
human_picked = CPU1_picked = CPU2_picked = False

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
    # reset picked status
    global human_picked
    global CPU1_picked
    global CPU2_picked
    human_picked = False
    CPU1_picked = False
    CPU2_picked = False
    #Let's empty slots just in case
    slots = []
    #Slots is a list of empty lists at the beginning of a turn. These empty lists will fill with cards, up to 3.
    for i in range(0, num_players):
        slots.append([])
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
    cards_CPU2.append('Yellow')
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
    print("CPU2 has: ", convert_dict(cards_CPU2))
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
        return deck, slots, last_turn
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
            choice = input("Select a slot to put your card " +"(" + card + ")" + ": ")
        choice = int(choice) - 1
        slots[choice].append(card)
        #debug
        print(slots)
        return deck, slots, last_turn

def human_pick_slot(slots, cards_player, human_picked):
    '''Lets human player pick a slot of cards, and add these cards to its cards. Updates slots'''
    choice = ''
    choices = []
    # populates choices list with valid choices as strings
    for i in range(0,len(slots)):
        if slots[i] != []:
            choices.append(str(i + 1))
    # print the slots for convenience
    for i in range(0,len(slots)):
        print("Slot ",str(i + 1), " contains:","\n")
        for card in slots[i]:
            print(card, "\n")
 
    # checks if inputed choice is a member of the list of valid choices
    while choice not in choices:
        print("You have these cards:")
        print(convert_dict(cards_player))
        choice = input("Choose the slot you want to pick: ")
    choice = int(choice) - 1
    cards_player += slots[choice]
    print("You now have: ", convert_dict(cards_player))
    del slots[choice]
    human_picked = True
    return slots, cards_player, human_picked

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
        print("I draw.")
        print()
        return "I draw."
    if all_slots_full:
        print("I pick.")
        print()
        return "I pick."
    # Let's use a threshold value to decide to pick. If a slot contains cards that would add threshold or more to my score, then decide to pick.
    threshold = 6
    for slot in slots:
        if compute_score(cards + slot) - compute_score(cards) >= threshold:
            print("I pick.")
            print()
            return "I pick."
    print("I draw.")
    print()
    return "I draw."

def ia_pick_slot(slots, cards, CPU_picked):
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
    CPU_picked = True
    print()
    return slots, cards, CPU_picked

def ia_draw_card(deck, slots, last_turn, cards):
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
    print()
    slots[choice].append(card)
    return deck, slots, last_turn

def human_pick_or_draw(slots):
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
        return "I pick."
    # No forced move, let's prompt the player
    print_board(slots, deck, cards_player, cards_CPU1, cards_CPU2)
    choice = ''
    while choice not in ['d','p']:
        choice = input("Do you want to [p]ick a slot or [d]raw a card? ")
    if choice == 'd':
        return "I draw."
    else:
        return "I pick."

def declare_winner(cards_player, cards_CPU1, cards_CPU2):
    '''Computes the scores of all players and declares the winner'''
    print("Player score: ", compute_score(cards_player), "\n", "CPU1's score: ", compute_score(cards_CPU1),"\n", "CPU2's score: ", compute_score(cards_CPU2))
    scores = [compute_score(cards_player), compute_score(cards_CPU1), compute_score(cards_CPU2)]
    if scores.index(max(scores)) == 0:
        print("A winner is you!")
    elif scores.index(max(scores)) == 1:
        print("CPU1 wins!!")
    elif scores.index(max(scores)) == 2:
        print("CPU2 wins!!")

# Game start
deck, cards_player, cards_CPU1, cards_CPU2 = game_start(deck, cards_player, cards_CPU1, cards_CPU2)
while not last_turn:
    slots = new_turn(num_players, slots)
    print()
    while slots != []:
        if human_picked == False:
            if human_pick_or_draw(slots) == "I draw.":
                deck, slots, last_turn = human_draw_card(deck, slots, last_turn)
            #elif human_pick_or_draw(slots) == "I pick.":
            else:
                slots, cards_player, human_picked = human_pick_slot(slots, cards_player, human_picked)
        #CPU 1's turn
        if CPU1_picked == False:
            if ia_pick_or_draw(slots, cards_CPU1) == "I draw.":
                deck, slots, last_turn = ia_draw_card(deck, slots, last_turn, cards_CPU1)
            else:
                slots, cards_CPU1, CPU1_picked = ia_pick_slot(slots, cards_CPU1, CPU1_picked)
        #CPU 2's turn
        if CPU2_picked == False:
            if ia_pick_or_draw(slots, cards_CPU2) == "I draw.":
                deck, slots, last_turn = ia_draw_card(deck, slots, last_turn, cards_CPU2)
            else:
                slots, cards_CPU2, CPU2_picked = ia_pick_slot(slots, cards_CPU2, CPU2_picked)
declare_winner(cards_player, cards_CPU1, cards_CPU2)
