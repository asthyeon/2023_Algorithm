import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 감시
[출력: 사각지대의 최소크기 출력]
1. CCTV 별로 방향이 존재함
 - 1번: 오
 - 2번: 오, 왼
 - 3번: 오, 위
 - 4번: 오, 왼, 위
 - 5번: 오, 아, 왼, 위
2. CCTV는 감시할 수 있는 방향에 있는 칸 전체 감시 가능
3. CCTV는 벽을 통과할 수 없고 감시할 수 없는 영역은 사각지대
4. CCTV는 90도 방향 회전 가능, CCTV를 통과할 수 있음
5. CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기 구하기
@ 풀이
(1) 최적의 경우 X -> 모든 경우의 수 구하여 찾기
(2) CCTV 수로 백트래킹
"""
# cctv 방향
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
# cctv 번호에 따른 방향
cctv_dir = [[],
            # 1번
            [[0], [1], [2], [3]],
            # 2번
            [[0, 2], [1, 3]],
            # 3번
            [[0, 3], [1, 0], [2, 1], [3, 2]],
            # 4번
            [[0, 2, 3], [1, 3, 0], [2, 0, 1], [3, 1, 2]],
            # 5번
            [[0, 1, 2, 3]]]


# 백트래킹 함수
def back_tracking(arr, cctv_xy, cctv):
    global blind_min
    # 백트래킹 종료조건(모든 cctv의 사각지대 탐색 완료)
    if cctv == len(cctv_xy):
        blind = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    blind += 1
        # 최소값 비교
        if blind_min > blind:
            blind_min = blind
        return

    # 모든 경우를 확인하기 위한 복사본 만들기
    arr_copy = [o[:] for o in arr[:]]
    # 사각지대 탐색(cctv 번호의 방향에 따라 여러번 반복)
    for dir in cctv_dir[cctv_xy[cctv][2]]:
        # 각 방향만큼 반복
        for d in dir:
            nx,  ny = cctv_xy[cctv][0], cctv_xy[cctv][1]
            while True:
                nx, ny = nx + dx[d], ny + dy[d]
                # 벽형성
                if 0 <= nx < N and 0 <= ny < M:
                    # 벽을 만날시 중지
                    if arr_copy[nx][ny] == 6:
                        break
                    # 빈 칸일시 감시
                    elif arr_copy[nx][ny] == 0:
                        arr_copy[nx][ny] = '#'
                else:
                    break
        # 다음 cctv를 향해 재귀
        back_tracking(arr_copy, cctv_xy, cctv + 1)
        # 복사본 초기화
        arr_copy = [o[:] for o in arr[:]]


# 세로 N, 가로 M
N, M = map(int, input().split())
# 사무실 정보
office = [list(map(int, input().split())) for _ in range(N)]

# 모든 CCTV 위치 찾기
cctv_xy = []
for x in range(N):
    for y in range(M):
        if 1 <= office[x][y] <= 5:
            cctv_xy.append((x, y, office[x][y]))

# 사각지대 최소값
blind_min = 10e9

back_tracking(office, cctv_xy, 0)
print(blind_min)