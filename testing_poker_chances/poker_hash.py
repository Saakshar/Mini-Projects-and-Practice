class HandHasher:
    def __init__(self,hashed_hand):
        if isinstance(hashed_hand,list):
            self.hashed_hand=''
            for card in hashed_hand:
                self.hashed_hand+=card
        elif isinstance(hashed_hand,str):
            self.hashed_hand=hashed_hand
        else:
            raise Exception(f'{type(hashed_hand)} is an invalid datatype')
    def unhash(self):
        cards = {'a': [], 'k': [], 'q': [], 'j': [], 't': [], '9': [], '8': [], '7': [], '6': [], '5': [], '4': [],
                 '3': [], '2': []}
        flush_draw = {'h': [], 'd': [], 'c': [], 's': []}
        for i in range(0, len(self.hashed_hand)):
            char = self.hashed_hand.lower()[i]
            if i % 2 == 1:
                cards[char] += char
            else:
                flush_draw[char] += char
        flush = 0
        for suit in flush_draw:
            if len(flush_draw[suit]) > flush:
                flush = len(flush_draw[suit])
        if flush < 5:
            flush = False
        else:
            flush = True
        value_check = self.value_check(cards).split('\n')
        # print(f'value - {value_check[0]}')
        # print(f'straight - {value_check[1]}')
        # print(f'flush - {flush}')
        # print('\n')
        value = 0
        value += int(value_check[0])
        if value_check[1] == 'True':
            value += 4
        if flush:
            value += 5
        decimal='.'
        for card in cards:
            if cards[card]!=[]:
                for i in range(0,len(cards[card])):
                    try:
                        int(cards[card][i])
                    except ValueError:
                        if cards[card][i]=='a':
                            num='14'
                        elif cards[card][i]=='k':
                            num='13'
                        elif cards[card][i]=='q':
                            num='12'
                        elif cards[card][i]=='j':
                            num='11'
                        elif cards[card][i]=='t':
                            num='10'
                    else:
                        num=f'0{cards[card][i]}'
                    finally:
                        decimal+=num
        value=float(value)+float(decimal)
        # print('\n')
        return value
    def value_check(self,cards):
        multiple_check='0'
        straight=0
        start_check=False
        for card in cards:
            if len(cards[card])>0:
                if straight=='False':
                    straight=0
                start_check=True
            if start_check and straight!='True':
                if len(cards[card])>0:
                    straight+=1
                    if straight==5:
                        straight='True'
                    elif card=='2' and straight!='True':
                        if straight==4 and len(cards['2'])>0:
                            straight='True'
                        else:
                            straight='False'
                elif straight!='True':
                    straight='False'
            if len(cards[card])>4:
                return f'8\n{straight}'
            elif len(cards[card])==4:
                return f'7\n{straight}'
            elif len(cards[card])==3:
                if multiple_check =='1':
                    return f'6\n{straight}'
                else:
                    multiple_check='3'
            elif len(cards[card])==2:
                if multiple_check=='3':
                    return f'6\n{straight}'
                elif multiple_check=='1':
                    return f'2\n{straight}'
                else:
                    multiple_check='1'
        return f'{multiple_check}\n{straight}'
