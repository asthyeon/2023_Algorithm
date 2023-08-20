import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 모든 토마토가 익는데 걸리는 시간
1. 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
2. 처음부터 모든토마토가 익었으면 0 출력
3. 모두 익지못하는 상황 -1 출력
'''


# bfs 함수 생성
def bfs(sx, sy, box, ans):
    # 이번 순회에 익은게 있는지 없는지 확인하기 위함
    tomato = 0
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx, ny = sx + dx, sy + dy
        # 벽 생성 및 토마토가 익지 않았을 때
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            # # 인큐
            # q.append((nx, ny))
            # 방문 기록
            box[nx][ny] = box[sx][sy] + 1
            # 이번 순회에 익은게 있는지 없는지 확인하기 위함
            tomato += 1
    return tomato

# 상자의 가로 칸 M, 상자의 세로 칸 N
M, N = map(int, input().split())

# 상자 생성
box = [list(map(int, input().split())) for _ in range(N)]

# 모든 시작점을 찾기 위한 i
i = 0
while True:
    i += 1
    # 전체 순회를 1번 돌 때 하나도 바뀐게 없다면 출력할 조건
    ans = 0
    for sx in range(N):
        for sy in range(M):
            if box[sx][sy] == i:
                tomato = bfs(sx, sy, box, ans)
                # 토마토가 이번 순회에 하나라도 익었다면 ans += 1
                if tomato > 0:
                    ans += 1
    # 토마토가 익을게 더이상 없다면
    if ans == 0:
        break


# 아예 다 익었거나 다 익지 않았을 때
if i == 1:
    # 하나라도 안익은 토마토가 있다면
    for j in range(N):
        if 0 in box[j]:
            print(-1)
            break
    # 이미 다 익었다면
    else:
        print(0)
# 익은 것들이 있다면
else:
    # 하나라도 안익은 토마토가 있다면
    for j in range(N):
        if 0 in box[j]:
            print(-1)
            break
    # 그게 아니라면 최소 일 수 출력
    else:
        print(i - 1)