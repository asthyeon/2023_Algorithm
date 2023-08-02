import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 정수 입력
a, b, c, d, e, f = map(int, input().split())
# 미지수
x = 0
y = 0

# 브루트포스 방식으로 탐색
for i in range(-999, 1000):
    for j in range(-999, 1000):
        # ax + by = c 를 만족하고,
        if c == (a * i) + (b * j):
            # dx + ey = f 를 만족한다면,
            if f == (d * i) + (e * j):
                x = i
                y = j

print(x, y)