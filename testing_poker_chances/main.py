from poker_hash import HandHasher
class PokerOdds():
    def __init__(self,community_cards,player_hands,burned_cards):
        self.deck = ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK', 'HA','D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK', 'DA','C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CJ', 'CT', 'CQ', 'CK', 'CA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA']
        # self.flush_draw={'H':0,'D':0,'C':0,'S':0}
        try:
            for card in burned_cards:
                self.deck.remove(card)
            for card in community_cards:
                # self.flush_draw[card[0]]+=1
                self.deck.remove(card)
            for player in player_hands:
                for card in player_hands[player]:
                    self.deck.remove(card)
            player_hands=self.card_fix(player_hands)
            self.percentages = {player: 0 for player in player_hands}
            if len(community_cards)==3:
                self.flop(community_cards,player_hands)
            elif len(community_cards)==4:
                self.turn(community_cards,player_hands)
            elif len(community_cards)==5:
                self.river(community_cards,player_hands)
            else:
                raise Exception(f'{community_cards} are an invalid set of community cards')
        except ValueError:
            raise Exception('invalid deck, the same card was used multiple times')
        # print(self.percentages)
        for player in self.percentages:
            self.percentages[player]=f'{self.percentages[player]}%'
        print(self.percentages)
    def flop(self,community_cards,player_hands):
        self.total_possible_cards = (len(self.deck)**2)-1
        # self.test_data={}
        draw_deck=list(self.deck)
        for card in self.deck:
            # self.test_data[card]=[]
            base_community_cards = list(community_cards)
            base_community_cards.append(card)
            draw_deck.remove(card)
            for card2 in draw_deck:
                # self.test_data[card].append(card2)
                base2_community_cards = list(base_community_cards)
                base2_community_cards.append(card2)
                self.iterate(base2_community_cards, player_hands)
            draw_deck.append(card)
    def turn(self,community_cards,player_hands):
        self.total_possible_cards=len(self.deck)
        for card in self.deck:
            base_community_cards = list(community_cards)
            base_community_cards.append(card)
            self.iterate(base_community_cards,player_hands)
    def river(self,community_cards,player_hands):
        self.total_possible_cards=1
        self.iterate(community_cards,player_hands)
    def iterate(self,community_cards,player_hands):
        self.values = {}
        for player in player_hands:
            if player_hands[player][0]=='#':
                pass
            elif player_hands[player][1]=='#':
                for card in self.deck:
                    pass
            else:
                self.base_iterate(community_cards,player_hands,player)
        winning_value = sorted([self.values[player] for player in self.values])[-1]
        for player in self.values:
            if self.values[player] == winning_value:
                self.percentages[player] += 100 / self.total_possible_cards
        print(self.percentages)
    def base_iterate(self,community_cards,player_hands,player):
                possible_hands = []
                for i in range(0, 36):
                    num1 = False
                    num2 = True
                    temp_community_cards = list(community_cards)
                    hashed_hand = ''
                    if i < 5:
                        hashed_hand += player_hands[player][0]
                        temp_community_cards.remove(community_cards[i])
                    elif i < 10:
                        hashed_hand += player_hands[player][1]
                        temp_community_cards.remove(community_cards[i - 5])
                    elif i == 35:
                        pass
                    else:
                        hashed_hand += player_hands[player][0]
                        hashed_hand += player_hands[player][1]
                        num1 = int(str(i / 5)[0]) - 2
                        num2 = i % 5
                        if num1 != num2:
                            temp_community_cards.remove(community_cards[num1])
                            temp_community_cards.remove(community_cards[num2])
                    if num1 != num2:
                        for card in temp_community_cards:
                            hashed_hand += card
                        possible_hands.append(HandHasher(hashed_hand).unhash())
                    # print(hashed_hand)
                # print(possible_hands)
                self.values[player] = sorted(possible_hands)[-1]
    # def player_iterate(self,community_cards,player_hands):
    #     for player in player_hands:
    #         if len(player_hands[player])==2:
    #             pass
    #         elif len(player_hands[player])==1:
    #             #
    #             pass
    #         elif player_hands[player]==[]:
    #             #
    #             pass
    #         else:
    #             raise Exception(f'{player} has an invalid hand')
    def card_fix(self,player_hands):
        for player in player_hands:
            if len(player_hands[player])>2:
                raise Exception(f'{player} has an invalid hand')
            else:
                while len(player_hands[player])!=2:
                    player_hands[player].append('#')
        return player_hands