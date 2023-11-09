import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 도로의 길이의 합이 가장 작은 사이클 찾기
1. 사이클을 찾아야 함
2. 사이클을 이루는 도로의 길이의 합이 최소가 되어야 함
3. 두 마을을 왕복하는 경우도 사이클에 포함됨
4. 사이클을 찾는 것이 불가능할 경우 -1 출력
5. 단방향
@ 풀이
(1) dfs로 싸이클 확인후 다익스트라로 싸이클 거리 구하기 => 시간초과
(2) dfs로 싸이클 확인후 플로이드-워셜로 싸이클 거리 구하기 
"""
INF = 1000000000


# 플로이드-워셜 함수
def floyd_warshall(roads):
    # 경유지
    for k in range(V + 1):
        # 출발지
        for i in range(V + 1):
            # 도착지
            for j in range(V + 1):
                # 바로 가는 것과 경유지를 거치는 것중 짧은 값으로 교체
                roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])

    # for _ in range(1, V + 1):
    #     print(f'1번에서 출발하는 거리들: {roads[_]}')


# dfs 함수
def dfs(start):
    global shortest
    # 스택 생성
    stack = []
    # 방문 리스트
    visited = [0] * (V + 1)
    # print(f'방문: {start}')
    # 방문한 순서
    now = start
    while True:
        for dist, new in roads_dfs[now]:
            # 방문하지 않은 곳이라면 방문
            if visited[new] == 0:
                visited[new] = 1
                stack.append(now)
                now = new
                # print(f'방문: {now}')
                break
            # 방문했던 곳이라면 싸이클이므로 최단 거리 구하기
            else:
                # 이번 싸이클의 거리 구하기
                # 자기 자신이라면
                if now == new:
                    short = roads[now][new]
                # 자기 자신이 아니라면
                else:
                    short = roads[now][new] + roads[new][now]
                # 최단 거리 싸이클 비교
                if shortest > short:
                    shortest = short
                # print(f'싸이클 : {short}')
        else:
            if stack:
                now = stack.pop()
                # print(f'뒤돌아가기: {now}')
            else:
                break


# 마을 수 V, 도로 수 E
V, E = map(int, input().split())
# 도로 정보
roads = [[INF] * (V + 1) for _ in range(V + 1)]
# dfs용 도로 정보
roads_dfs = [[] for _ in range(V + 1)]
for _ in range(E):
    # a -> b 를 잇는 거리 c 의 도로
    a, b, c = map(int, input().split())
    # 길이 여러개 일수도 있으므로 더 짧은 거리로 교체
    roads[a][b] = min(roads[a][b], c)
    # dfs용 도로 정보 넣기
    roads_dfs[a].append((c, b))

# print(f'인접리스트: {roads}')

# 각 거리 구해놓기
floyd_warshall(roads)
# 최단 거리 사이클
shortest = INF
# dfs 실행
for i in range(1, V + 1):
    dfs(i)

# 싸이클이 없다면 -1 처리
if shortest == INF:
    shortest = -1

print(shortest)
