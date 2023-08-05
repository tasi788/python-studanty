import os,random

def print_board(board):         # 輸出井字的樣子
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def main():
    init_board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' ' }
    begin = True
    while begin:
        curr_board = init_board.copy()  # 複製初始的空字典
        begin = False
        turn = random.choice(['x','o']) # 隨機讓兩者開始
        counter = 0
        print_board(curr_board)
        while counter < 9:
            move = input('輪到 %s ,請輸入位置: ' % turn)
            if curr_board[move] == ' ': # 判斷位置是否為' '，空則記錄現在的 turn
                counter += 1
                curr_board[move] = turn 
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            print_board(curr_board)
        choice = input('再玩一局 ? (yes | no) ')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()