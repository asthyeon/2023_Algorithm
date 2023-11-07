import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모든 도시의 쌍(A, B)에 대해서 도시 A -> B 로가는 필요한 비용의 최솟값 구하기
1. 시작 도시와 도착 도시 같은 경우 X
2. 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음
3. 도착 못하는 경우 0 출력
@ 풀이
(1) 플로이드-워셜 사용
(2) 모든 거리를 한 번에 구하기
"""
import heapq
INF = 999999999


# 플루이드-워셜 함수
def floyd_warshall(buses):
    # 경유지
    for i in range(1, n + 1):
        # 출발지
        for j in range(1, n + 1):
            # 목적지
            for k in range(1, n + 1):
                # 시작 도시와 도착 도시가 같은 경우 = 0
                if j == k:
                    buses[j][k] = 0
                # 직접 가는 것과 경로를 거치는 것 중 최소값으로 교체
                else:
                    buses[j][k] = min(buses[j][k], buses[j][i] + buses[i][k])

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            # 도달할 수 없을 때는 0 출력
            if buses[x][y] == INF:
                print(0, end=' ')
            else:
                print(buses[x][y], end=' ')
        print()


# 도시의 개수 n
n = int(input())
# 버스의 개수 m
m = int(input())
# 각 출발지로부터 버스의 비용 정보
buses = [[INF] * (n + 1) for _ in range(n + 1)]
# 버스 연결 정보
for _ in range(m):
    # 시작 a, 도착 b, 비용 c
    a, b, c = map(int, input().split())
    # 길이 여러개일수도 있으므로 더 짧은 비용으로 교체
    buses[a][b] = min(c, buses[a][b])

floyd_warshall(buses)
