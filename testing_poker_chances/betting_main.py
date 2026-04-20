from flask import Flask,render_template, redirect, request
from main import PokerOdds

app=Flask(__name__)
deck = ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'HT', 'HJ', 'HQ', 'HK', 'HA','D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK', 'DA','C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CJ', 'CT', 'CQ', 'CK', 'CA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'ST', 'SJ', 'SQ', 'SK', 'SA']
data={}
community_cards=[]
burned_cards=[]
@app.route('/')
def startup():
    return render_template('index.html',data=data,com_cards=community_cards,burned_cards=burned_cards)
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
    return render_template('done.html',data=PokerOdds(community_cards,data,burned_cards).percentages)
@app.route('/burn_card',methods=['POST'])
def burn_card():
    card = request.form.get('burned_card').upper().replace(' ', '')
    if card in deck:
        deck.remove(card)
        burned_cards.append(card)
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)