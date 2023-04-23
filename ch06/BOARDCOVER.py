dx = [[0, 0, 1], [0, 0, 1], [0, 1, 1], [0, 1, 1]]
dy = [[0, 1, 0], [0, 1, 1], [0, -1, 0], [0, 0, 1]]

def main():
    C = int(input())
    for tc in range(C):
        global cnt
        cnt = 0
        sharpCounter = 0

        h, w = map(int, input().split())
        coverdBoard = [[False] * w for _ in range(h)]

        for i in range(h):
            line = input()
            for j, c in enumerate(line):
                if c == '#':
                    sharpCounter += 1
                    coverdBoard[i][j] = True

        if (w*h - sharpCounter) % 3 != 0:
            print(0)
        else:
            coverBoard(coverdBoard)
            print(cnt)

def coverBoard(coveredBoard):
    if False not in sum(coveredBoard, []):
        global cnt
        cnt += 1
        return
    
        
    for i in  range(len(coveredBoard)):
        for j in range(len(coveredBoard[0])):
            if coveredBoard[i][j] == False:
                for k in range(4):
                    if canCover(coveredBoard, i, j, dx[k], dy[k]):
                        coveredBoard = cover(coveredBoard, i, j, dx[k], dy[k])
                        coverBoard(coveredBoard)
                        eraseBoard(coveredBoard, i, j, dx[k], dy[k])
                return
    return
        
def canCover(board, startX, startY, blockX, blockY):
    for i in range(3):
        movedX = startX + blockX[i]
        movedY = startY + blockY[i]
        if not(movedX in range(0, len(board))) or not(movedY in range(0, len(board[0]))):
            return False
        if board[movedX][movedY] == True:
            return False
        
    return True

def cover(coverdBoard, startX, startY, blockX, blockY):
    for i in range(3):
        movedX = startX + blockX[i]
        movedY = startY + blockY[i]
        coverdBoard[movedX][movedY] = True
        
    return coverdBoard

def eraseBoard(coverdBoard, startX, startY, blockX, blockY):
    for i in range(3):
        movedX = startX + blockX[i]
        movedY = startY + blockY[i]
        coverdBoard[movedX][movedY] = False
        
    return coverdBoard


if __name__ == '__main__':
    main()