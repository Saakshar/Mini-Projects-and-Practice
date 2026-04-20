import random
base_deck=['h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13','h14',
      'd2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','d14',
      'c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14',
      's2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14']
deck=['h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13','h14',
      'd2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13','d14',
      'c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14',
      's2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14']
board={}
def control_station():
    num_of_players = int(input("How many players would you like to add? ").replace(" ",""))
    if num_of_players>10:
        raise Exception("Too Many Players")
    starting_cash=int(input("How much money would you like everyone to start with? ").replace("$",""))
    for i in range(0, num_of_players):
        add_player(starting_cash)
    players_in_bid=[]
    for player in board:
        players_in_bid.append(board[player])
    check = 0
    raise_amount = 0
    while True:
        for player in players_in_bid:
            player_turn=True
            print("\n\n\n\n\n\n\n\n\n")
            while player_turn:
                cmd=input(f'What would {player["name"]} like to do? ')
                if cmd.replace(" ","").lower()=="help":
                    print("balance - shows the money you have left\n"
                          "pot size - shows the money that is going to go to the winner\n"
                          "previous bet - shows the money required to call\n"
                          "money spent - shows the money that you have spent during this round\n"
                          "show hand - shows your hand\n"
                          "fold - avoid placing further bets and abstain for the rest of the round\n"
                          "check - continue playing in the round without increasing the bid amount\n"
                          "call - match the increased bid\n"
                          "raise - increase the bid\n"
                          "all in - increase the bid by everything you have\n")
                elif cmd.replace(" ","").lower()=="balance":
                    print(f"Balance: {player['cash']}$")
                elif cmd.replace(" ","").lower()=="potsize":
                    pot=0
                    for player in board:
                        pot+=board[player]['bid']
                    print(f"Pot Size: {pot}$")
                elif cmd.replace(" ","").lower()=="previousbet":
                    print(f"Previous Bet to Match: {raise_amount}")
                elif cmd.replace(" ","").lower()=="moneyspent":
                    print(f"You have spent {player['bid']}$ this round")
                elif cmd.replace(" ","").lower()=="showhand":
                    print(player['hand'])
                elif cmd.replace(" ","").lower()=="fold":
                    players_in_bid.remove(player)
                    player_turn=False
                elif cmd.replace(" ","").lower()=="check" and raise_amount==0:
                    check+=1
                    player_turn = False
                elif cmd.replace(" ","").lower()=="call":
                    board[player['name']]['cash']-=raise_amount
                    board[player['name']]['bid']+=raise_amount
                    check+=1
                    player_turn = False
                elif cmd.replace(" ","").lower()=="raise":
                    board[player['name']]['cash'] -= raise_amount
                    board[player['name']]['bid'] += raise_amount
                    raise_amount=int(input("How much would you like to raise by? ").replace("$",""))
                    board[player['name']]['cash'] -= raise_amount
                    board[player['name']]['bid'] += raise_amount
                    check=1
                    player_turn = False
                elif cmd.replace(" ","").lower()=="allin" and player['cash']>0:
                    board[player['name']]['cash'] -= raise_amount
                    board[player['name']]['bid'] += raise_amount
                    raise_amount=player['cash']
                    board[player['name']]['cash'] -= raise_amount
                    board[player['name']]['bid'] += raise_amount
                    check = 1
                    player_turn = False
                else:
                    print("That is not a valid command")
                if check>=len(players_in_bid):
                    check=0
                    raise_amount=0
                    print("\n\n\nBid Over")
                    winners=reveal(players_in_bid)
                    if len(deck)<len(board)*5:
                        deck=base_deck
                    players_in_bid = []
                    pot=0
                    for player in board:
                        pot+=board[player]['bid']
                        board[player]['bid']=0
                        players_in_bid.append(board[player])
                        board[player]["hand"] = []
                        board[player]["strength"] = 0
                        for i in range(0, 5):
                            card = random.choice(deck)
                            deck.remove(card)
                            board[player]["hand"].append(card)
                        board[player]['strength'] = calculate(player)
                    for winner in winners:
                        winner['cash']+=pot/len(winners)
                    print(f"Winner: {player['name']}")
def add_player(cash):
    name=input(f"What is the name of player {len(board)+1}? ").title()
    board[name]={'name':name,"hand":[],"strength":0,"high card":[],"cash":cash,"bid":0}
    for i in range(0,5):
        card=random.choice(deck)
        deck.remove(card)
        board[name]["hand"].append(card)
    board[name]['strength']=calculate(name)
def calculate(player):
        strength=0.0
        for card in board[player]["hand"]:
            board[player]['high card'].append(int(card[1:]))
        board[player]['high card'].sort()
        strength+=pair_check(board[player]['high card'])
        strength+=straight_check(board[player]['high card'])
        strength+=flush_check(board[player]["hand"])
        strength += high_check(board[player]['high card'])
        return strength
def high_check(cards):
    tie_value = "0."
    print(cards)
    for i in range(1, 6):
        decimal = str(cards[-i])
        if len(decimal) == 1:
            decimal = "0" + decimal
        tie_value += decimal
    return float(tie_value)
def pair_check(cards):
    pairing={"2":[],"3":[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'11':[],'12':[],'13':[],'14':[]}
    pairing_copy={"2":[],"3":[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'11':[],'12':[],'13':[],'14':[]}
    for card in cards:
        pairing[str(card)].append(card)
        pairing_copy[str(card)].append(card)
    for key,value in pairing_copy.items():
        if value==[]:
            pairing.pop(key)
    num=0
    full1 = False
    full2 = False
    for key, value in pairing.items():
        if len(value) == 5:
            return 8.0
        elif len(value)==4:
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
    old_value=cards[0]
    for i in range(1,5):
        new_value=cards[i]
        if old_value+1!=new_value and not(i==4 and cards[i]==14 and cards[0]==2):
            return 0.0
        old_value=new_value
    return 4.0
def flush_check(hand):
    old_suit=hand[0][0]
    for i in range(1,5):
        new_suit=hand[i][0]
        if old_suit!=new_suit:
            return 0.0
    return 5.0
def reveal(players_in_bid):
    winner=[players_in_bid[0],players_in_bid[0]['strength']]
    for data in players_in_bid:
        player=data['name']
        if player != players_in_bid[0]:
            if board[player]['strength']>winner[1]:
                winner=[board[player],board[player]['strength']]
            elif board[player]['strength']==winner[1]:
                winner.append(board[player])
                winner.append(board[player]['strength'])
    true_winners = []
    for i in range(0, len(winner)):
        if i % 2 == 0:
            true_winners.append(winner[i])
    if len(true_winners)==1:
        return true_winners
    return [player['name'] for player in true_winners]
control_station()