import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 만들어야할 최소의 통로 길이를 소수점 둘째 자리까지 반올림하여 출력
1. 이미 연결된 선들이 존재
@ 풀이
(1) kruskal 알고리즘 사용
"""


# find 함수
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


# union 함수
def union(parents, x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x


# 우주신들의 수 N, 이미 연결된 통로 수 M
N, M = map(int, input().split())
# 우주신들의 부모 리스트
parents = [i for i in range(N)]

# 우주신들의 좌표
gods = []
for _ in range(N):
    X, Y = map(int, input().split())
    gods.append((X - 1, Y - 1))
# 이미 연결된 통로 연결
for _ in range(M):
    x, y = map(int, input().split())
    union(parents, x - 1, y - 1)

# 각 우주신들의 거리
distances = []
for j in range(N - 1):
    for k in range(j + 1, N):
        dist = (((gods[j][0] - gods[k][0]) ** 2) + ((gods[j][1] - gods[k][1]) ** 2)) ** 0.5
        distances.append((dist, j, k))

# 오름차순 정렬
distances.sort()

# 현재 방문한 정점 수
cnt = 0
# 최소 통로의 길이의 합
sum_dist = 0
for dist, god1, god2 in distances:
    # 싸이클이 발생하지 않는다면
    if find(god1) != find(god2):
        cnt += 1
        sum_dist += dist
        union(parents, god1, god2)
        # MST 구성이 끝나면
        if cnt == N - M:
            break

print('{:.2f}'.format(round(sum_dist, 2)))
