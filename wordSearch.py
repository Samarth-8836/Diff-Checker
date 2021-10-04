def inBounds(board, i, j):
    if (i > -1) and (i<len(board)) and (j>-1) and (j<len(board[i])):
        return True
    return False

def searchStart(word, board, i, j, curr = 0, correctStep = 0):
    if curr >= (len(word) - 1):
        return True
    temp = None
    if inBounds(board, i+1,j) and word[curr+1] == board[i+1][j]:
        temp = board[i][j]
        board[i][j] = -1
        return searchStart(word,board, i+1,j,curr+1,correctStep+1)
    elif inBounds(board, i,j+1) and word[curr+1] == board[i][j+1]:
        temp = board[i][j]
        board[i][j] = -1
        return searchStart(word,board, i,j+1,curr+1,correctStep+1)
    elif inBounds(board, i-1,j) and word[curr+1] == board[i-1][j]:
        temp = board[i][j]
        board[i][j] = -1
        return searchStart(word,board, i-1,j,curr+1,correctStep+1)
    elif inBounds(board, i,j-1) and word[curr+1] == board[i][j-1]:
        temp = board[i][j]
        board[i][j] = -1
        return searchStart(word,board, i,j-1,curr+1,correctStep+1)
    if temp:
        board[i][j] = temp # wrong

def boardCopy(board):
    newBoard = []
    for x in range(0, len(board)):
        temp = []
        for y in range(0, len(board[x])):
            temp.append(board[x][y])
        newBoard.append(temp)
    return newBoard

def wordSearch(word,board):
    for i in range(0,len(board)):
        for j in range(0, len(board[i])):
            if(word[0] == board[i][j]):
                if searchStart(word, boardCopy(board), i, j):
                    return True
    return False

if __name__ == '__main__':
    board = [
        ["C","A","A"],
        ["A","A","A"],
        ["B","C","D"]
    ]
    print(wordSearch("AAB", board))
