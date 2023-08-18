import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# BFS 탐색
1. 양방향
2. 인접 정점은 오름 차순으로 방문
3. 방문 순서 출력
'''


# bfs 함수 생성
def bfs(arr, S, R):
    # 방문 리스트 생성
    visited = [0] * (S + 1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(R)
    # 시작점 방문기록
    visited[R] = 1
    # 방문 순서
    order = [0] * (S + 1)
    cnt = 0
    # 큐가 빌 때까지
    while q:
        # 디큐
        t = q.pop(0)
        cnt += 1
        # 방문 순서 기록하기
        order[t] = cnt
        # 인접한 w 가 방문하지 않은 곳이라면
        for w in adj_l[t]:
            if visited[w] == 0:
                # 인큐
                q.append(w)
                # 방문 기록(거리)
                visited[w] = visited[t] + 1
        # 방문 순서 기록하기
    # 방문 순서 반환
    return order


# 정점의 수 S, 간선의 수 M, 시작 정점 R
S, M, R = map(int, input().split())

# 인접 리스트 생성
adj_l = [[] for _ in range(S + 1)]
# 간선 연결
for _ in range(M):
    v1, v2 = map(int, input().split())

    # 양방향
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

# 오름차순 정렬
for i in range(1, S + 1):
    adj_l[i].sort()

# 함수 값 받기
order = bfs(adj_l, S, R)

# 각 정점을 몇 번째로 방문했는지 출력
for j in range(1, S + 1):
    print(order[j])


