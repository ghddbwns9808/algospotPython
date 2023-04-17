def main():
    n = input()
    numbers = list(map(int, input().split()))
    primNumber = erathostenes(max(numbers))
    cnt = 0

    for n in numbers:
        if primNumber[n]:
            cnt += 1

    print(cnt)
    

def erathostenes(n):
    primeNum = [True] * (n + 1)
    primeNum[1] = False
    for i in range(2, int(n/2) + 1):
        j = 2
        while i*j < n+1:
            primeNum[i*j] = False
            j += 1

    return primeNum


if __name__ == '__main__':
    main()