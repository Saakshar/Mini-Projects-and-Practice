from tkinter import *
import operator
import random
root=Tk()
root.title('Random Chess')
#randomizer starts
pieces=['R','H','B','Q','K','B','H','R']
data={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
for i in data:
    new_piece=random.choice(pieces)
    pieces.remove(new_piece)
    data[0].append(f'B{new_piece}')
    data[1].append('BP')
    data[2].append('')
    data[3].append('')
    data[4].append('')
    data[5].append('')
    data[6].append('WP')
    data[7].append(f'W{new_piece}')
#randomizer ends
board={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
turn_order='white'
selected_piece=''
cont=True
omnidirectional_iteration={0:[operator.add,operator.add],1:[operator.sub,operator.sub],2:[operator.add,operator.sub],3:[operator.sub,operator.add]}
color_check={'B':'red','W':'cyan'}
castle_open={'W':True,'B':True}
def defusing_passant(selected_piece):
    if len(data[int(selected_piece[2])][int(selected_piece[3])]) == 3:
        data[int(selected_piece[2])][int(selected_piece[3])] = f'{selected_piece[0]}P'
def pawn_diagonals(selected_piece,row,column):
    if data[row][column] != '':
        defusing_passant(selected_piece)
        return True
    elif data[int(selected_piece[2])][column] != '' and data[row][column] == '' and len(data[int(selected_piece[2])][column]) == 3:
        data[int(selected_piece[2])][column] = ''
        board[int(selected_piece[2])][column].config(text='')
        move_indicator.config(text='EN PASSANT')
        return True
    return False
def bishop_anti_warp(selected_piece,distance,eval1,eval2):
    for i in range(1,distance):
        if data[eval1(int(selected_piece[2]),i)][eval2(int(selected_piece[3]),i)]!='':
            return False
    return True
def move_check(selected_piece,row,column):
    if board[row][column].cget('fg')!=color_check[selected_piece[0]]:
        if selected_piece[1]== 'R' or selected_piece[1]== 'Q':
            if int(selected_piece[2])==row:
                for i in range(1,abs(int(selected_piece[3])-column)):
                    if ((int(selected_piece[3]) - column) > 0 and data[row][int(selected_piece[3])-i] != '') or ((int(selected_piece[3]) - column) < 0 and data[row][int(selected_piece[3]) + i] != ''):
                        return False
                return True
            elif int(selected_piece[3])==column:
                for i in range(1, abs(int(selected_piece[2]) - row) ):
                    if ((int(selected_piece[2]) - row)>0 and data[int(selected_piece[2])-i][column]!='') or ((int(selected_piece[2]) - row)<0 and data[int(selected_piece[2])+i][column]!=''):
                        return False
                return True
        if selected_piece[1]== 'B' or selected_piece[1]== 'Q':
            for i in range (0,7):
                if int(selected_piece[2])==row+i and int(selected_piece[3])==column+i:
                    return bishop_anti_warp(selected_piece,i,operator.sub,operator.sub)
                elif int(selected_piece[2])==row-i and int(selected_piece[3])==column-i:
                    return bishop_anti_warp(selected_piece,i,operator.add,operator.add)
                elif int(selected_piece[2])==row-i and int(selected_piece[3])==column+i:
                    return bishop_anti_warp(selected_piece,i,operator.add,operator.sub)
                elif int(selected_piece[2])==row+i and int(selected_piece[3])==column-i:
                    return bishop_anti_warp(selected_piece,i,operator.sub,operator.add)
        elif selected_piece[1]=='H':
            for direction in omnidirectional_iteration:
                if (omnidirectional_iteration[direction][0](int(selected_piece[2])==row,1) and omnidirectional_iteration[direction][1](int(selected_piece[3]) == column ,2)) or (omnidirectional_iteration[direction][0](int(selected_piece[2])==row,2) and omnidirectional_iteration[direction][1](int(selected_piece[3]) == column ,1)):
                    return True
        elif selected_piece[1]=='P':
            if selected_piece[0]== 'W':
                if int(selected_piece[2])==6 and row==4 and int(selected_piece[3])==column and data[row][column]== '' and data[row + 1][column]== '':
                    data[int(selected_piece[2])][int(selected_piece[3])]=f'{selected_piece[:2]}E'
                    return True
                elif row==int(selected_piece[2])-1 and column==int(selected_piece[3]) and data[row][column]== '':
                    defusing_passant(selected_piece)
                    return True
                elif row==int(selected_piece[2])-1 and (column == int(selected_piece[3]) + 1 or column == int(selected_piece[3]) - 1):
                    return pawn_diagonals(selected_piece,row,column)
            elif selected_piece[0]=='B':
                if int(selected_piece[2]) == 1 and row == 3 and int(selected_piece[3]) == column and data[row][column]== '' and data[row - 1][column]== '':
                    data[int(selected_piece[2])][int(selected_piece[3])]=f'{selected_piece[:2]}E'
                    return True
                elif row == int(selected_piece[2]) + 1 and column == int(selected_piece[3]) and data[row][column]== '':
                    defusing_passant(selected_piece)
                    return True
                elif row == int(selected_piece[2]) + 1 and (column == int(selected_piece[3]) + 1 or column == int(selected_piece[3]) - 1):
                    return pawn_diagonals(selected_piece,row,column)
        elif selected_piece[1]=='K':
            if (int(selected_piece[2]) + 1 >= row >= int(selected_piece[2]) - 1) and (int(selected_piece[3]) + 1 >= column >= int(selected_piece[3]) - 1):
                castle_open[selected_piece[0]]=False
                return True
            elif castle_open[selected_piece[0]] and row==int(selected_piece[2]) and column==2 and ([board[int(selected_piece[2])][i].cget('text') for i in range(0,5)]==['R','','','','K']):
                board[row][column+1].config(text='R', fg=color_check[selected_piece[0]])
                data[row][column+1] = f'{selected_piece[0]}R'
                board[row][column-2].config(text='')
                data[row][column-2] = ''
                move_indicator.config(text='CASTLE')
                return True
            elif castle_open[selected_piece[0]] and row==int(selected_piece[2]) and column==6 and ([board[int(selected_piece[2])][i+4].cget('text') for i in range(0,4)]==['K','','','R']):
                board[row][column-1].config(text='R', fg=color_check[selected_piece[0]])
                data[row][column-1] = f'{selected_piece[0]}R'
                board[row][column+1].config(text='')
                data[row][column+1] = ''
                move_indicator.config(text='CASTLE')
                return True
    return False
def play(row,column):
    global turn_order
    global selected_piece
    global cont
    if cont:
        phrase = "'s Turn"
        move_indicator.config(text='')
        if selected_piece!='':
            if int(selected_piece[2])==row and int(selected_piece[3])==column:
                board[row][column].config(bg=selected_piece[4:])
                selected_piece=''
                move_indicator.config(text='MOVE CANCELED')
            elif move_check(selected_piece,row,column):
                if board[row][column].cget('text')=='K':
                    cont=False
                    phrase=' Wins!'
                    move_indicator.config(text='GAME OVER')
                elif turn_order == 'white':
                    turn_order = 'black'
                elif turn_order == 'black':
                    turn_order = 'white'
                if selected_piece[1]=='P' and (row==0 or row==7):
                    board[row][column].config(text='Q', fg=color_check[selected_piece[0]])
                    data[row][column] = f'{selected_piece[0]}Q'
                else:
                    board[row][column].config(text=selected_piece[1], fg=color_check[selected_piece[0]])
                    data[row][column] = data[int(selected_piece[2])][int(selected_piece[3])]
                board[int(selected_piece[2])][int(selected_piece[3])].config(bg=selected_piece[4:], text='',fg='green')
                data[int(selected_piece[2])][int(selected_piece[3])] = ''
                selected_piece = ''
            else:
                move_indicator.config(text='INVALID MOVE')
        elif data[row][column]!='':
            if (turn_order=='white' and data[row][column][0]=='W') or (turn_order=='black' and data[row][column][0]=='B'):
                selected_piece=f'{data[row][column][:2]}{row}{column}{board[row][column].cget("bg")}'
                board[row][column].config(bg='gray')
            else:
                move_indicator.config(text='NOT YOUR TURN')
        else:
            move_indicator.config(text='SELECT A PIECE FIRST')
        turn_order_label.config(text=f"{turn_order.title()}{phrase}",bg=color_check[turn_order[0].upper()])
turn_order_label=Label(root,text="White's Turn",bg=color_check[turn_order[0].upper()])
turn_order_label.grid(row=0,column=0,columnspan=8)
move_indicator=Label(root,text='')
move_indicator.grid(row=9,column=0,columnspan=8)
for row in range(0, len(data)):
    for column in range(0, len(data[0])):
        new_btn = Button(root,font=("Helvetica", 8, "bold"), width=3,command=lambda x=f'{str(row)}{str(column)}':play(int(x[0]),int(x[1])))
        if len(data[row][column]) > 0:
            new_btn.config(text=data[row][column][1],fg=color_check[data[row][column][0]])
        else:
            new_btn.config(text='')
        if (row+column)%2==0:
            new_btn.config(bg='maroon')
        else:
            new_btn.config(bg='tan')
        new_btn.grid(row=row+1, column=column)
        board[row].append(new_btn)
root.mainloop()