def display(li):
    print(li)
    return


def pk(li, r, c, move):
    if r < 0 or c < 0 or r >= len(li) or c >= len(li) or li[r][c] > 0:
        return
    if move == len(li)*len(li):
        li[r][c] = move
        display(li)
        li[r][c] = 0
        return
    li[r][c] = move
    pk(li, r-2, c+1, move+1)
    pk(li, r-1, c+2, move+1)
    pk(li, r+1, c+2, move+1)
    pk(li, r+2, c+1, move+1)
    pk(li, r+2, c-1, move+1)
    pk(li, r+1, c-2, move+1)
    pk(li, r-1, c-2, move+1)
    pk(li, r-2, c-1, move+1)
    li[r][c] = 0


n = int(input())
r = int(input())
c = int(input())
li = [[0 for j in range(n)]for i in range(n)]
pk(li, r, c, 1)
