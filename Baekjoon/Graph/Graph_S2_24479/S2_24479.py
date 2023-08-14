import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
# 재귀함수 호출 횟수 늘려주기
sys.setrecursionlimit(10**9)

'''
# DFS 탐색
1. 무방향 그래프
2. 시간 초과로 재귀로 풀어보기
3. 재귀 호출 횟수를 늘려야함
'''

# 정점의 수 N, 간선의 수 M, 시작 정점 R
N, M, R = map(int, input().split())

# 배열 형성
arr = [[] for _ in range(N + 1)]

# 간선 연결
# 메모리 초과를 고려해서 0 이 있는 배열이 아닌 빈 리스트에 숫자를 추가하기
for i in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

# 오름차순 정렬
for j in range(1, N + 1):
    arr[j].sort()

# 방문 리스트 형성
visited = [0] * (N + 1)

# 방문 순서 및 현재 위치
order = [0] * (N + 1)
top = 0

# dfs 함수 설정
def dfs(N, arr, R):
    global top
    # 시작점 방문
    visited[R] = 1
    top += 1
    order[R] = top
    # 인접 노드 찾기
    for k in arr[R]:
        # 방문하지 않은 곳이라면
        if visited[k] == 0:
            # 방문하기
            R = k
            dfs(N, arr, R)
    return

dfs(N, arr, R)

for l in range(1, N + 1):
    print(order[l])