from tkinter import *
root=Tk()
root.title('Budget Chess')
data={0:['BR','BH','BB','BQ','BK','BB','BH','BR'],1:['BP','BP','BP','BP','BP','BP','BP','BP'],2:['','','','','','','',''],3:['','','','','','','',''],4:['','','','','','','',''],5:['','','','','','','',''],6:['WP','WP','WP','WP','WP','WP','WP','WP'],7:['WR','WH','WB','WQ','WK','WB','WH','WR']}
board={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
turn_order='white'
selected_piece=''
def play(row,column):
    global turn_order
    global selected_piece
    if selected_piece[:2]!='':
        data[row][column]=selected_piece[:2]
        board[int(selected_piece[2])][int(selected_piece[3])].config(bg=selected_piece[4:])
        data[int(selected_piece[2])][int(selected_piece[3])]=''
        selected_piece=''
        if turn_order == 'white':
            turn_order = 'black'
        elif turn_order == 'black':
            turn_order = 'white'
    elif data[row][column]!='':
        if (turn_order=='white' and data[row][column][0]=='W') or (turn_order=='black' and data[row][column][0]=='B'):
            selected_piece=f'{data[row][column]}{row}{column}{board[row][column].cget("bg")}'
            board[row][column].config(bg='gray')
    update()
def update():
    turn_order_label.config(text=f"{turn_order.title()}'s Turn")
    for row in range(0,len(board)):
        for column in range(0,len(board[0])):
            if len(data[row][column]) > 0:
                board[row][column].config(text=data[row][column][1])
                if data[row][column][0] == 'B':
                    board[row][column].config(fg='red',font=("Helvetica", 8, "bold"))
                elif data[row][column][0] == 'W':
                    board[row][column].config(fg='cyan',font=("Helvetica", 8, "bold"))
            else:
                board[row][column].config(text='')
            board[row][column].config(command=lambda x=str(row)+str(column):play(int(x[0]),int(x[1])))
turn_order_label=Label(root,text="White's Turn")
turn_order_label.grid(row=0,column=0,columnspan=8)
for row in range(0, len(data)):
    for column in range(0, len(data[0])):
        if len(data[row][column])>0:
            new_btn=Button(root,width=3)
        else:
            new_btn = Button(root, width=3)
        if (row+column)%2==0:
            new_btn.config(bg='black')
        else:
            new_btn.config(bg='white')
        new_btn.grid(row=row+1, column=column)
        board[row].append(new_btn)
update()
root.mainloop()/