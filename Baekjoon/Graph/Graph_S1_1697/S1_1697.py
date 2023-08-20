import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
1. 수빈이가 걷는다면 1초 후에 X -> X-1 or X+1
2. 수빈이가 순간이동 1초 후에 X -> 2*X
3. bfs로 그 시점에서 갈 수 있는 모든 부분 조사하기
'''


# bfs 함수 생성
def bfs(N, K):
    # 방문 리스트 생성
    visited = [0] * 100001
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(N)
    # 시작점 방문 기록
    visited[N] = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        t = q.pop(0)
        # -1 일 때 0 보다 크거나 같고, 방문하지 않았을 때
        if t - 1 >= 0:
            if visited[t - 1] == 0:
                q.append(t - 1)
                visited[t - 1] = visited[t] + 1
                if t - 1 == K:
                    break
        # +1 일 때 100001 보다 작고, 방문하지 않았을 때
        if t + 1 < 100001:
            if visited[t + 1] == 0:
                q.append(t + 1)
                visited[t + 1] = visited[t] + 1
                if t + 1 == K:
                    break
        # 2배 일 때 100001 보다 작고, 방문하지 않았을 때
        if 2 * t < 100001:
            if visited[2 * t] == 0:
                q.append(2 * t)
                visited[2 * t] = visited[t] + 1
                if 2 * t == K:
                    break
    return visited[K] - 1


# 수빈이 위치 N, 동생 위치 K
N, K = map(int, input().split())

print(bfs(N, K))