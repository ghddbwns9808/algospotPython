def main():
    C = int(input())
    for tc in range(C):
        answer = []

        W = input()
        n = int(input())

        for _ in range(n):
            global cache
            cache = [[-1 for i in range(101)] for i in range(101)]
            S = input()

            if isMatch(W, S, 0, 0):
                answer.append(S)

        sortedAnswer = sorted(answer)
        for s in sortedAnswer:
            print(s)

def isMatch(W, S, w, s):
    global cache
    ret = cache[w][s]

    if ret != -1:
        return ret
    
    while w < len(W) and s < len(S) and (W[w] == '?' or W[w] == S[s]):
        w += 1
        s += 1

    if w == len(W):
        if s == len(S):
            cache[w][s] = 1
            return 1
        else:
            cache[w][s] = 0
            return 0
        
    if W[w] == '*':
        for i in range(s, len(S) + 1):
            if isMatch(W, S, w +1, i) == 1:
                cache[w][s] = 1
                return 1
    cache[w][s] = 0
    return 0

if __name__ == '__main__':
    main()