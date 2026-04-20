import random
import time
global deck
deck=['h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13','h14',
      'd2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','d14',
      'c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14',
      's2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14']
# for i in range(0,999999):
#     deck.append(random.choice(deck))
board={}
data=[]
global iteration
iteration=1
def add_player():
    global iteration
    global deck
    # name=input(f"What is the name of player {len(board)+1}? ").title()
    name=str(iteration)
    board[name]={'name':name,"hand":[],"strength":0,"high card":[]}
    for i in range(0,5):
        card=random.choice(deck)
        # card=input("What is the card: ").lower()
        deck.remove(card)
        board[name]["hand"].append(card)
    deck=['h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13','h14',
      'd2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','d14',
      'c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14',
      's2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14']
    board[name]['strength']=calculate(name)
    data.append(board[name]['strength'])
    if board[name]['strength']>8:
        print(board[name])
    iteration+=1
def calculate(player):
    strength = 0.0
    for card in board[player]["hand"]:
        board[player]['high card'].append(int(card[1:]))
    board[player]['high card'].sort()
    strength += pair_check(board[player]['high card'])
    strength += straight_check(board[player]['high card'])
    strength += flush_check(board[player]["hand"])
    strength +=high_check(board[player]['high card'])
    return strength
def high_check(cards):
    tie_value="0."
    for i in range(1,6):
        decimal=str(cards[-i])
        if len(decimal)==1:
            decimal="0"+decimal
        tie_value+=decimal
    return float(tie_value)
def pair_check(cards):
    pairing = {"2": [], "3": [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12': [],
               '13': [], '14': []}
    pairing_copy = {"2": [], "3": [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [],
                    '12': [], '13': [], '14': []}
    for card in cards:
        pairing[str(card)].append(card)
        pairing_copy[str(card)].append(card)
    for key, value in pairing_copy.items():
        if value == []:
            pairing.pop(key)
    num = 0
    full1=False
    full2=False
    for key, value in pairing.items():
        if len(value) == 5:
            return 8.0
        elif len(value) == 4:
            return 7.0
        elif len(value) == 3:
            full1 = True
            num += 3
        elif len(value) == 2:
            full2 = True
            num += 1
    if full1 and full2:
        return 6.0
    else:
        return float(num)
def straight_check(cards):
    old_value = cards[0]
    for i in range(1, 5):
        new_value = cards[i]
        if old_value + 1 != new_value and not (i == 4 and cards[i] == 14 and cards[0] == 2):
            return 0.0
        old_value = new_value
    return 4.0
def flush_check(hand):
    old_suit = hand[0][0]
    for i in range(1, 5):
        new_suit = hand[i][0]
        if old_suit != new_suit:
            return 0.0
    return 5.0
for i in range(0,999999):
    add_player()
    # time.sleep(0.001)
data.sort()
print(data)