import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 큰 정사각형 구하기
@ 풀이
(1) bfs로 풀기
"""


# bfs 함수
def bfs(sx, sy):
    global area
    global x
    global y
    while True:
        for i in range(x):
            for j in range(y):
                if sx + i > n - 1 or sy + j > n - 1:
                    return
                if arr[sx + i][sy + j] != 1:
                    return
        else:
            now_area = x * y
            if area < now_area:
                area = now_area
            x += 1
            y += 1


# 세로길이 n, 가로길이 m
n, m = map(int, input().split())
# 행렬
arr = [list(map(int, input().rstrip())) for _ in range(n)]

# 최대 넓이
area = 0
x = y = 1

for sx in range(n):
    for sy in range(m):
        if arr[sx][sy] == 1:
            bfs(sx, sy)

print(area)