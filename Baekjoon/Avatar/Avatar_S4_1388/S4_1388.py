import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수 출력
'''

# 방 바닥의 세로: N, 가로: M
N, M = map(int, input().split())

# 배열 형성
adj_m = []
for i in range(N):
    adj_m.append(input().strip())

# 방문을 기록하기 위한 리스트 형성
visited = [[0] * M for _ in range(N)]
# 나무판자 개수 세기
cnt = 0
# 가로행
n = 0

# n 이 N 이 될 때 까지 반복
while n < N:
    # n 번째 행에서 w 열 반복
    for w in range(M):
        # 방문한 기록이 없을 때
        if visited[n][w] == 0:
            # 방문 기록 체크
            visited[n][w] = 1
            # 만약 가로 판자라면
            if adj_m[n][w] == '-':
                # 마지막일 때는 갯수 + 1
                if w == M - 1:
                    cnt += 1
                # 마지막이 아닐 때는
                else:
                    # 남은 가로 길이만큼 이어져있는지 확인
                    for j in range(w + 1, M):
                        # 다음 위치가 가로 판자가 아니라면 갯수 + 1
                        if adj_m[n][j] != '-':
                            cnt += 1
                            break
                        # 다음 위치가 마지막이라면 갯수 + 1
                        else:
                            visited[n][j] = 1
                            if j == M - 1:
                                cnt += 1
            # 세로 판자일 때 형식 반복
            else:
                if n == N - 1:
                    cnt += 1
                else:
                    for k in range(n + 1, N):
                        if adj_m[k][w] != '|':
                            cnt += 1
                            break
                        else:
                            visited[k][w] = 1
                            if k == N - 1:
                                cnt += 1
    # 한 개의 행이 끝나면 다음 행 반복
    n += 1

print(cnt)
