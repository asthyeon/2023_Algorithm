import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 바이러스에 걸린 컴퓨터의 수 출력
1. 양방향
'''


# bfs 함수 생성
def bfs(adj_l, S, N):
    # 방문 리스트 생성
    visited = [0] * (N + 1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(S)
    # 시작점 방문 기록
    visited[S] = 1
    # 감염된 컴퓨터 수
    cnt = 0
    # 큐가 빌 때까지
    while q:
        # 디큐
        t = q.pop(0)
        # 인접한 w 가 방문한 곳이 아니라면
        for w in adj_l[t]:
            if visited[w] == 0:
                # 인큐
                q.append(w)
                # 방문 기록
                visited[w] = 1
                # 감염된 컴퓨터 수 세기
                cnt += 1
    return cnt



# 컴퓨터의 수
N = int(input())
# 간선의 수
E = int(input())
# 인접리스트 생성
adj_l = [[] for _ in range(N + 1)]
# 간선 연결
for _ in range(E):
    v1, v2 = map(int, input().split())

    # 양방향
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

# 시작점
S = 1

print(bfs(adj_l, S, N))