def main():
    N = int(input())
    a = int(N/5)

    while a>=0:
        remain = N - 5*a
        if remain % 3 == 0:
            print(a + int(remain / 3))
            break
        a -= 1

    if a == -1:
        print(-1)
    
    
if __name__ == '__main__':
    main()