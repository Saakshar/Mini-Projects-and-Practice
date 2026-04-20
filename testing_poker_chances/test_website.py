import random
from poker_hash import HandHasher
from flask import Flask, render_template,redirect,url_for
app=Flask(__name__)
deck=['H2','H3','H4','H5','H6','H7','H8','H9','HT','HQ','HK','HA',
       'D2','D3','D4','D5','D6','D7','D8','D9','DT','DQ','DK','DA',
       'C2','C3','C4','C5','C6','C7','C8','C9','CT','CQ','CK','CA',
       'S2','S3','S4','S5','S6','S7','S8','S9','ST','SQ','SK','SA'
]
players=['Tim','Kim','Jim','Him']
community_cards=[]
for i in range(0,5):
    card=random.choice(deck)
    deck.remove(card)
    community_cards.append(card)
display_cards=[]
for i in range(0,3):
    display_cards.append(community_cards[i])
personal_cards={}
for player in players:
    personal_cards[player]=[]
    for i in range(0,2):
        card=random.choice(deck)
        deck.remove(card)
        personal_cards[player].append(card)
used_cards=[]
@app.route('/')
def startup():
    return render_template('display_index.html',ccards=display_cards,pcards=personal_cards)
@app.route('/add/<loc>/<card>')
def add_card(loc,card):
    global display_cards
    if card=='com' and len(display_cards)!=5:
        display_cards.append(community_cards[len(display_cards)])
        return render_template('display_index.html', ccards=display_cards, pcards=personal_cards)
    used_cards.append(card)
    if loc=="com":
        display_cards.remove(card)
    if len(used_cards)==5:
        return redirect(url_for('show_hand'))
    return redirect(url_for('startup'))
@app.route('/show')
def show_hand():
    processed_cards=''
    for card in used_cards:
        processed_cards+=card
    value=HandHasher(processed_cards).unhash()
    return render_template('display_data.html',value=value)
if __name__=='__main__':
    app.run(debug=True)