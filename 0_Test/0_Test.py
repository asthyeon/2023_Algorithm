import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 상어 초등학교
[출력: 학생의 만족도의 총 합 출력하기]
1. 규칙으로 정해진 순서대로 학생의 자리를 정하기
 - 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리 정하기
 - 위 사항을 만족하는 칸이 여러 개면 인접한 칸중 비어있는 칸이 가장 많은 칸으로 자리 정하기
 - 위 사항을 만족하는 칸도 여러 개면 행의 번호가 가장 작은칸으로, 그 다음 열의 번호로
2. |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r,2 c2)를 인접하다고 한다
 - 델타탐색으로 상하좌우만 인접
3. 학생의 만족도를 구하기: 그 학생과 인접한 칸에 앉은 좋아한느 학생의 수 구하기
 - 0: 0, 1: 1, 2: 10, 3: 100, 4: 1000
@ 풀이
(1) 그냥 풀어보기
"""

# 학생 수의 제곱근 N
N = int(input())
# 좌석 생성
arr = [[0] * N for _ in range(N)]
# 학생 번호에 따른 좋아하는 학생 딕셔너리
likes = {}
for _ in range(N ** 2):
    # 각 학생의 번호와 좋아하는 학생 4명 입력
    num, l1, l2, l3, l4 = map(int, input().split())
    # 좋아하는 학생 딕셔너리에 넣기
    likes[num] = (l1, l2, l3, l4)

    # 앉힐 좌석 탐색
    # 앉힐 수 있는 좌석 리스트
    seats = []
    for x in range(N):
        for y in range(N):
            # 해당 좌석이 비어있다면
            if arr[x][y] == 0:
                # 해당 좌석과 인접한 좋아하는 학생 수
                seat_like = 0
                # 해당 좌석과 인접한 비어있는 좌석 수
                seat_empty = 0
                # 델타탐색
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    # 벽 형성
                    if 0 <= nx < N and 0 <= ny < N:
                        # 빈 좌석이라면 비어있는 좌석 수 카운트
                        if arr[nx][ny] == 0:
                            seat_empty += 1
                        # 빈 좌석이 아니라면 좋아하는 학생인지 확인하고 카운트
                        else:
                            if arr[nx][ny] in likes[num]:
                                seat_like += 1
                # 앉힐 수 있는 좌석 리스트에 추가
                seats.append((seat_like, seat_empty, x, y))
    # 조건 순서대로 정렬
    seats = sorted(seats, key = lambda x: (-x[0], -x[1], x[2], x[3]))
    # 좌석에 앉히기
    arr[seats[0][2]][seats[0][3]] = num

# 만족도 조사
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
total = 0
for x in range(N):
    for y in range(N):
        # 점수 구하기
        cnt = 0
        # 델타탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < N:
                # 좋아하는 학생이 리스트에 있는지 확인 후 카운트
                if arr[nx][ny] in likes[arr[x][y]]:
                    cnt += 1
        # 만족도 점수 추가
        total += score[cnt]

print(total)