board={0:[' ',' ',' '],1:[' ',' ',' '],2:[' ',' ',' ']}
def check_win():
    cont=True
    win_conditions = {}
    for i in range(0, 3):
        win_conditions[f'c{i}'] = (f'{board[0][i]}{board[1][i]}{board[2][i]}')
        win_conditions[f'r{i}'] = (f'{board[i][0]}{board[i][1]}{board[i][2]}')
    win_conditions['d0'] = (f'{board[0][0]}{board[1][1]}{board[2][2]}')
    win_conditions['d2'] = (f'{board[0][2]}{board[1][1]}{board[2][0]}')
    empty = False
    for set in win_conditions:
        # print(f'{set}: {win_conditions[set]}')
        if win_conditions[set] == "OOO":
            print("YOU WIN!!!!")
            show_game()
            cont = False
        elif win_conditions[set] == "XXX":
            print("YOU LOSE")
            show_game()
            cont = False
        elif not empty:
            for i in range(0, 2):
                if win_conditions[set][i] == ' ':
                    empty = True
    if not empty and cont:
        print('DRAW')
        show_game()
        cont = False
    return [cont,win_conditions]
def show_game():
    print(f'     1   2   3\n\n1    {board[0][0]} | {board[0][1]} | {board[0][2]}\n    -----------\n2    {board[1][0]} | {board[1][1]} | {board[1][2]}\n    -----------\n3    {board[2][0]} | {board[2][1]} | {board[2][2]}')
def bot_turn(i):
    if set[0] == 'c':
        board[i][int(set[1])] = 'X'
    elif set[0] == 'r':
        board[int(set[1])][i] = 'X'
    elif set[0] == 'd':
        board[i][abs(int(set[1]) - i)] = 'X'
    else:
        raise Exception('Error: game failed to load')
    return True
cont=True
while cont:
    print(f'     1   2   3\n\n1    {board[0][0]} | {board[0][1]} | {board[0][2]}\n    -----------\n2    {board[1][0]} | {board[1][1]} | {board[1][2]}\n    -----------\n3    {board[2][0]} | {board[2][1]} | {board[2][2]}')
    try:
        row=int(input('What row would you like to select? '))-1
        column=int(input('What column would you like to select? '))-1
        if row>2 or row<0 or column>2 or column<0:
            raise ValueError
    except ValueError:
        print('Only enter a number between 1 and 3!!!!')
    else:
        if board[row][column] == ' ':
            board[row][column] = 'O'
            win_conditions=check_win()[1]
            if cont:
                bot_moved=False
                for set in win_conditions:
                    if not bot_moved:
                        if win_conditions[set]=='O O' or win_conditions[set]=='X X':
                            bot_moved=bot_turn(1)
                        elif win_conditions[set]==' OO' or win_conditions[set]==' XX':
                            bot_moved=bot_turn(0)
                        elif win_conditions[set]=='OO ' or win_conditions[set]=='XX ':
                            bot_moved=bot_turn(2)
                if not bot_moved:
                    if board[1][1]==' ':
                        board[1][1]='X'
                    else:
                        for row in board:
                            for column in range(0,3):
                                if board[row][column]==' ' and not bot_moved:
                                    board[row][column]='X'
                                    bot_moved=True
            cont=check_win()[0]
        else:
            print('That spot is taken, try picking a different one.')