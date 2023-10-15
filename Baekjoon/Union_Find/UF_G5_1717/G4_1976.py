import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 여행 일정이 주어졌을 때 이 여행 경로가 가능한 것인지 확인하기
1. 도시가 N 개 존재, 길이 있을 수도 없을 수도 있음
2. 중간에 다른 도시를 경유해서 여행 가능
3. 같은 도시를 여러 번 방문하는 것도 가능
4. 가능하면 YES, 불가능 NO
@ 풀이
(1) 유니온 파인드 사용
(2) dfs로 방문
"""


# find 함수
def find(x):
    if cities[x] == x:
        return x
    # 경로 압축
    cities[x] = find(cities[x])
    return cities[x]


# union 함수
def union(x, y):
    # 루트 노드 찾기
    x = find(x)
    y = find(y)
    if x > y:
        cities[x] = y
    else:
        cities[y] = x


# 도시의 수 N
N = int(input())
# 여행 계획에 속한 도시들의 수 M
M = int(input())
# 도시 리스트
cities = [k for k in range(N + 1)]
# 도시 연결 정보
for i in range(1, N + 1):
    info = [0]
    info.extend(list(map(int, input().split())))

    for j in range(1, N + 1):
        # 자기 자신은 넘기기
        if i == j:
            continue
        else:
            # 연결되어 있다면
            if info[j] == 1:
                union(i, j)
# 여행 계획
plan = list(map(int, input().split()))

# 도시 방문
start = cities[plan[0]]
for n in range(1, len(plan)):
    if cities[plan[n]] != start:
        print('NO')
        break
else:
    print('YES')