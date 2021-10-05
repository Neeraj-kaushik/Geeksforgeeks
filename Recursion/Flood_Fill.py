def floodfill(li, row, col, ans, visited):
    if row < 0 or col < 0 or row == len(li) or col == len(li[0]) or li[row][col] == 1 or visited[row][col] == True:
        return
    if row == len(li)-1 and col == len(li[0])-1:
        print(ans, end=" ")
        return
    visited[row][col] = True
    floodfill(li, row-1, col, ans+"t", visited)
    floodfill(li, row, col-1, ans+"l", visited)
    floodfill(li, row+1, col, ans+"d", visited)
    floodfill(li, row, col+1, ans+"r", visited)
    visited[row][col] = False


n = int(input())
m = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
visited = [[False for j in range(m)] for i in range(n)]
floodfill(li, 0, 0, "", visited)
