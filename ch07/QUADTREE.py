def main():
    C = int(input())

    for tc in range(C):
        reversedTree = reverse(input())
        print(reversedTree)

def reverse(quadTree):
    if quadTree[0] == 'b' or quadTree[0] == 'w':
        return quadTree[0]
    
    else:
        idx = 1
        first = reverse(quadTree[idx:])
     
        idx += len(first)
        second = reverse(quadTree[idx:])

        idx += len(second)
        third = reverse(quadTree[idx:])

        idx += len(third)
        fourth = reverse(quadTree[idx:])

        return 'x' + third + fourth + first + second


if __name__ == '__main__':
    main()