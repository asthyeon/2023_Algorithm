import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 직각삼각형
1. 2차원 평면에 N개의 점이 주어져 있음
2. 이 중에서 세 점을 골랐을 때 직각삼각형이 몇 개나 있는지 구하기
* 입력
- N: 점의 개수(3 <= N <= 1,500)
- 둘째 줄부터 N개의 줄에 걸쳐 각 점의 x좌표와 y좌표가 빈 칸을 사이에 두고 주어짐
  (주어지는 모든 점의 좌표는 다름)
[출력: 첫째 줄에 직각삼각형의 개수를 출력하기]
"""

"""
@ 풀이
(1) 조합으로 세 점을 찾는 경우의 수 구하기
(2) 세 점으로 직각 삼각형이 되는 조건 확인 => 메모리 초과
 - a^2 + b^2 = c^2
(3) 삼중포문으로 되는 조건 확인
"""


# 직각삼각형 찾는 함수
def find(locations, a, b, c):
    # 각 점의 위치 입력
    x1, y1 = locations[a][0], locations[a][1]
    x2, y2 = locations[b][0], locations[b][1]
    x3, y3 = locations[c][0], locations[c][1]

    # 각 선분 길이 구하기
    a_square = (x1 - x2) ** 2 + (y1 - y2) ** 2
    b_square = (x2 - x3) ** 2 + (y2 - y3) ** 2
    c_square = (x3 - x1) ** 2 + (y3 - y1) ** 2

    # 직각삼각형 확인 후 맞으면 개수 추가
    if a_square + b_square == c_square:
        return 1
    elif b_square + c_square == a_square:
        return 1
    elif c_square + a_square == b_square:
        return 1
    # 직각삼각형이 아니라면 추가 X
    else:
        return 0


# 점의 개수 N
N = int(input())
# 각 점의 좌표들
locations = []
for _ in range(N):
    x, y = map(int, input().split())
    locations.append((x, y))

# 각 세점마다 직각삼각형 확인
answer = 0
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            answer += find(locations, a, b, c)

print(answer)