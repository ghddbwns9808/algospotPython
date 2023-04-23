buttons = [[0, 1, 2],
       [3, 7, 9, 11],
       [4, 10, 14, 15],
       [0, 4, 5, 6 , 7],
       [6, 7, 8, 10, 12],
       [0, 2, 14, 15],
       [3, 14, 15],
       [4, 5, 7, 14, 15],
       [1, 2, 3, 4, 5],
       [3, 4, 5, 9, 13]]

def main():
    C = int(input())
    for tc in range(C):
        global curMin
        curMin = 1000000000
        clocks = list(map(int,input().split()))
        for i in range(16):
            clocks[i] = (int(clocks[i] / 3)) % 4

        if clocks[8] != clocks[12]:
            print(-1)
            continue

        mustCount = mustPressed(clocks)
        if clocks[9] != 0:
            print(-1)
            continue

        bruteForce(clocks, mustCount)
        if curMin == 1000000000:
            print(-1)
            continue
        
        print(curMin)
        

def mustPressed(curClock):
    cnt = 0
    #11번 clock align
    cnt += (4 - curClock[11]) % 4
    for _ in range((4 - curClock[11]) % 4):
        pressBtn(1, curClock)

    #8번 12번 clock align
    cnt += (4 - curClock[8]) % 4
    for _ in range((4 - curClock[8]) % 4):
        pressBtn(4, curClock)

    #13번 clock align
    cnt += (4 - curClock[13]) % 4
    for _ in range((4 - curClock[13]) % 4):
        pressBtn(9, curClock)

    #10번 clock align
    cnt += (4 - curClock[10]) % 4
    for _ in range((4 - curClock[10]) % 4):
        pressBtn(2, curClock)

    return cnt


def bruteForce(curClocks, cnt):
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    for e in range(4):
                        for f in range(4):
                            curPress = [a, b, c, d, e, f]
                            press(curClocks, curPress)
                            if isAligned(curClocks):
                                global curMin
                                curMin =min([curMin, cnt + sum(curPress)])
                            unPress(curClocks, curPress)


def press(curClocks, curPress):
    for _ in range(curPress[0]):
        pressBtn(0, curClocks)

    for _ in range(curPress[1]):
        pressBtn(3, curClocks)

    for _ in range(curPress[2]):
        pressBtn(5, curClocks)

    for _ in range(curPress[3]):
        pressBtn(6, curClocks)
    
    for _ in range(curPress[4]):
        pressBtn(7, curClocks)

    for _ in range(curPress[5]):
        pressBtn(8, curClocks)

def unPress(curClocks, curPress):
    for _ in range(curPress[0]):
        unPressBtn(0, curClocks)

    for _ in range(curPress[1]):
        unPressBtn(3, curClocks)

    for _ in range(curPress[2]):
        unPressBtn(5, curClocks)

    for _ in range(curPress[3]):
        unPressBtn(6, curClocks)
    
    for _ in range(curPress[4]):
        unPressBtn(7, curClocks)

    for _ in range(curPress[5]):
        unPressBtn(8, curClocks)

def pressBtn(n, curClock):
    global buttons
    for btn in buttons[n]:
        curClock[btn] = (curClock[btn] + 1) % 4
    return curClock

def unPressBtn(n, curClock):
    global buttons
    for btn in buttons[n]:
        curClock[btn] = (curClock[btn] - 1) % 4

def isAligned(curClock):
    if sum(curClock) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()