import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


"""
# 트리의 루트를 1이라고 할 때, 각 노드의 부모를 구하는 프로그램 작성
@ 풀이
(1) 일단 정점을 연결
(2) DFS 사용
"""
sys.setrecursionlimit(10**9)


# dfs 함수
def dfs(n, adj, visited):
    for i in adj[n]:
        if visited[i] == 0:
            visited[i] = n
            dfs(i, adj, visited)


# 노드의 개수 N
N = int(input())

# 인접 리스트
adj = [[] for _ in range(N + 1)]

# 정점 연결하기
for _ in range(N - 1):
    n1, n2 = map(int, input().split())

    adj[n1].append(n2)
    adj[n2].append(n1)

# 방문 리스트
visited = [0] * (N + 1)

# 함수 사용
dfs(1, adj, visited)

# 2번 노드부터 부모 노드 번호 출력
for j in range(2, N + 1):
    print(visited[j])
