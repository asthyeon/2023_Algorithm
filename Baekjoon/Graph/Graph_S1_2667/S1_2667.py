import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 2차원 배열을 그래프로 표현해 DFS나 BFS로 순회하기
1. 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하기
2. 집이 잇는 곳: 1, 집이 없는 곳: 0
3. 전체 탐색을 하면서 1이 있는 곳만 방문을 하고, 방문한 곳은 다른 숫자로 바꿔주기
'''


# bfs 함수 생성
def bfs(arr, sx, sy):
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sx, sy))
    # 시작점 방문 기록
    arr[sx][sy] = 2
    # 방문한 집 수
    cnt = 0
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.pop(0)
        # 방문한 곳 집 수 세기
        cnt += 1
        # 델타탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 어레이가 1이라면
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                # 인큐
                q.append((nx, ny))
                # 방문 기록
                arr[nx][ny] = 2
                # 숫자 세기
    return cnt



# 지도의 크기 N
N = int(input())

# 단지 생성
arr = [list(map(int, input().rstrip())) for _ in range(N)]

# 방문 리스트 생성
visited = [[0] * N for _ in range(N)]

# 총 단지수
total = 0

# 각 단지내의 집 수
apart = []

# 전체 탐색
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total += 1
            apart.append(bfs(arr, i, j))

# 오름차순 정렬
apart.sort()

print(total)
for k in range(total):
    print(apart[k])