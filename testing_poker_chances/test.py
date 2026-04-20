from card_counter import PokerOdds
data=PokerOdds(['H8', 'H5', 'SJ'],{'tim': ['H2', 'HK'], 'kim': ['C2', 'C7'], 'jim': ['DJ', 'S9']}).test_data
deck=PokerOdds(['H8', 'H5', 'SJ'],{'tim': ['H2', 'HK'], 'kim': ['C2', 'C7'], 'jim': ['DJ', 'S9']}).deck
first_cards=[card for card in data]
print(f'data: {first_cards}\ndeck: {deck}')
for card in deck:
    if card not in first_cards:
        print(card)
# print(len(deck))