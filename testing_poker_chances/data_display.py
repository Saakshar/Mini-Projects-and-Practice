from flask import Flask,render_template, redirect, request
from card_counter import PokerOdds

app=Flask(__name__)
deck = ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK', 'HA','D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK', 'DA','C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CJ', 'CT', 'CQ', 'CK', 'CA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA']
# num_of_players=input('How many players would like to play? ')
data={}
community_cards=[]
burned_cards=[]
# for i in range(0,int(num_of_players)):
#     # new_player=input(f'What is the name of player {i+1}? ')
#     data[new_player]=[]
#     for i in range(0,2):
#         drawn_card=random.choice(deck)
#         deck.remove(drawn_card)
#         data[new_player].append(drawn_card)
# community_cards=[]
# for i in range(0,3):
#     drawn_card = random.choice(deck)
#     deck.remove(drawn_card)
#     community_cards.append(drawn_card)
# print(f'Community Cards: {community_cards}')
# print(data)
# print(PokerOdds(community_cards,data).percentages)
@app.route('/')
def startup():
    return render_template('display_index.html',data=data,com_cards=community_cards,burned_cards=burned_cards)
@app.route('/add_com_card',methods=['POST'])
def add_com_card():
    if len(community_cards)!=5:
        card=request.form.get('community_card').upper().replace(' ', '')
        if card in deck:
            deck.remove(card)
            community_cards.append(str(card))
    return redirect('/')
@app.route('/add_player',methods=['POST'])
def add_player():
    player=request.form.get('player').upper().replace(' ','')
    if player !='':
        data[str(player)]=[]
    return redirect('/')
@app.route('/add_card/<player>',methods=['POST'])
def add_card(player):
    card=request.form.get('player_card').upper().replace(' ','')
    if card in deck and len(data[player])!=2:
        deck.remove(card)
        data[player].append(card)
    return redirect('/')
@app.route('/fold/<name>')
def fold(name):
    del data[name]
    return redirect('/')
@app.route('/calculate')
def calculate():
    return render_template('display_data.html',data=PokerOdds(community_cards,data,burned_cards).percentages)
@app.route('/burn_card',methods=['POST'])
def burn_card():
    card = request.form.get('burned_card').upper().replace(' ', '')
    if card in deck:
        deck.remove(card)
        burned_cards.append(card)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)