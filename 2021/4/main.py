finput = open('input.txt','r').read().rstrip()
draws, *boards = finput.split('\n\n')
draws = draws.split(',')

boards = [b.split() for b in boards]
marked_boards = [ [0] * 25 for _ in boards]

def is_winner(m):
    # horizontal winner
    for i in range(0,25,5):
        if m[i:i+5] == [1,1,1,1,1]:
            return True
    # vertical winner
    for i in range(0,5):
        if m[i:25:5] == [1,1,1,1,1]:
            return True
    return False

def score(b,m):
    return sum(int(b[i]) for i,v in enumerate(m) if v == 0)

part1_ans = None
winners = [0] * len(boards)
for draw in draws:
    for i, board in enumerate(boards):
        if draw in board:
            ind = board.index(draw)
            marked_boards[i][ind] = 1

            if not winners[i] and is_winner(marked_boards[i]):
                if not part1_ans: 
                    part1_ans = score(board,marked_boards[i])*int(draw)

                winners[i] = 1 
                if sum(winners) == len(boards):
                    print(part1_ans)
                    print(score(board,marked_boards[i])*int(draw))
