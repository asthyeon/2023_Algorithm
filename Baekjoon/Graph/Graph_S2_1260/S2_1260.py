import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하기
1. 방문할 수 있는 점이 여러 개인 경우 오름차순으로 방문
2. 양방향 간선
'''


# dfs 함수 생성
def dfs(adj_l, N, V):
    # 방문 리스트 생성
    visited = [0] * (N + 1)
    # 스택 형성
    stack = []
    # 시작점 방문 기록
    visited[V] = 1
    # 방문 순서 기록
    order = []
    order.append(V)
    while True:
        # 인접하고 방문하지 않은 곳이라면
        for w in adj_l[V]:
            if visited[w] == 0:
                # 방문 기록
                visited[w] = 1
                # 이전에 지나온 곳 스택에 넣기
                stack.append(V)
                # 위치 이동
                V = w
                # 방문 순서 기록
                order.append(V)
                break
        # 방문하지 않은 곳이 없다면
        else:
            # 스택이 비어있지 않다면
            if stack:
                V = stack.pop()
            # 스택이 비어있다면 탐색 종료
            else:
                break
    return order


# bfs 함수 생성
def bfs(adj_l, N, V):
    # 방문 리스트 생성
    visited = [0] * (N + 1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(V)
    # 시작점 방문 기록
    visited[V] = 1
    # 방문 순서 기록을 위한 리스트
    order = []
    # 큐가 빌 때까지
    while q:
        # 디큐
        t = q.pop(0)
        # 방문 순서 기록
        order.append(t)
        # 인접한 w 가 방문한 적이 없다면
        for w in adj_l[t]:
            if visited[w] == 0:
                # 인큐
                q.append(w)
                # 방문 기록
                visited[w] = 1
    return order


# 정점의 개수 N, 간선의 개수 M, 시작점 V
N, M, V = map(int, input().split())

# 인접리스트 생성
adj_l = [[] for _ in range(N + 1)]
# 간선 연결
for _ in range(M):
    v1, v2 = map(int, input().split())

    # 양방향
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

# 오름차순 정렬
for i in range(1, N + 1):
    adj_l[i].sort()

print(*dfs(adj_l, N, V))
print(*bfs(adj_l, N, V))