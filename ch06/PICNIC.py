def main():
    C = int(input())

    for tc in range(C):
        global cnt
        cnt = 0
        n, m = map(int, input().split())
        areFriends = [[False] * n for _ in range(n)]
        friends = list(map(int, input().split()))
        visited = [False] * n

        for j in range(m):
            first = min(friends[2*j], friends[2*j + 1])
            second = max(friends[2*j], friends[2*j + 1])
            areFriends[first][second] = True
        
        mappingFriends([], visited, areFriends, n)
        print(cnt)
        


def mappingFriends(curFriends, visited, areFriends, n):
    if len(curFriends) == n:
        global cnt
        cnt += 1
        return
    
    for i in range(0, n - 1):
        if visited[i] == False:
            visited[i] = True

            for j in range(n):
                if visited[j] is False and areFriends[i][j] is True:
                    visited[j] = True
                    mappingFriends(curFriends + [i, j], visited, areFriends, n)
                    visited[j] = False
            
            visited[i] = False
            return

if __name__ == '__main__':
    main()