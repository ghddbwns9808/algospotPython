def main():
    C = int(input())

    for tc in range(C):
        fencesLen = int(input())
        fences = list(map(int, input().split()))
        
        maxWidth = dc(fences, 0, len(fences) - 1)
        print(maxWidth)


def dc(fences, start, end):
    
    if start == end:
        return fences[start]
    
    left = (start + end) // 2
    right = left + 1

    leftMax = dc(fences, start, left)
    rightMax = dc(fences, right, end)

    fenceCnt = 2
    minHigth = min(fences[left], fences[right])
    midMax = minHigth * fenceCnt

    while start < left or right < end:
        
        if start == left:
            right += 1
            minHigth = min(minHigth, fences[right])

        elif right == end:
            left -= 1
            minHigth = min(minHigth, fences[left])

        elif fences[left - 1] >= fences[right + 1]:
            left -= 1
            minHigth = min(minHigth, fences[left])

        elif fences[left - 1] < fences[right + 1]:
            right += 1
            minHigth = min(minHigth, fences[right])

        fenceCnt += 1
        midMax = max(midMax, minHigth * fenceCnt)

    return max(leftMax, rightMax, midMax)


if __name__ == '__main__':
    main()