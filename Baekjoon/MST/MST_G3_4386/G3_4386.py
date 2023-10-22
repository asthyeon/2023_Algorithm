import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용
1. 별자리를 이루는 선은 다른 두 별을 일직선으로 이은 형태
2. 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있음
@ 풀이
(1) prim 알고리즘 이용
"""
import heapq


# prim 함수
def prim(distance):
    # 우선순위큐
    pq = []
    # 방문 리스트
    MST = [0] * n
    # 시작점 가중치 및 별번호
    heapq.heappush(pq, (0, 0))
    # 최소 비용 합
    total = 0
    while pq:
        weight, number = heapq.heappop(pq)
        
        # 이미 방문했다면 넘기기
        if MST[number] == 1:
            continue
            
        # 방문 체크
        MST[number] = 1
        # 최소 비용에 더하기
        total += weight
            
        for new_dist, new_num in distance[number]:
            # 방문한 곳이라면 넘기기
            if MST[new_num] == 1:
                continue
            # 방문하지 않았다면 인큐
            heapq.heappush(pq, (new_dist, new_num))

    return total


# 별의 개수
n = int(input())

# 각 별의 x, y 좌표
stars = []
for i in range(n):
    x, y = map(float, input().split())
    
    stars.append((x, y))

# 거리 리스트
distance = [[] for _ in range(n)]
# 각 별들간의 거리 계산
for i in range(n - 1):
    for j in range(i, n):
        # 자기 자신일 때 넘기기
        if i == j:
            continue
        # 소수 둘째 자리까지 계산
        d = round((((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** 0.5), 2)
        
        # 거리 및 별 번호 저장
        distance[i].append((d, j))
        distance[j].append((d, i))

print(prim(distance))