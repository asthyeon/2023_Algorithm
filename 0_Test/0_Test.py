import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 십자뒤집기
[출력: 흰 보드를 입력에 주어진 보드로 바꾸는데 필요한 최소 클릭의 횟수 구하기]
1. 클릭한 칸과 그 칸에 인접한 동서남북 색깔이 반대가 됨
2. 보드의 형태를 바꾸기
3. '*': 검은색, '.': 흰색
@ 풀이
(1) bfs로 모든 경우의 수 다 구해보기 -> 시간초과
(2) 중복을 제거하기(같은게 여러번있을 수 있음)
"""
from collections import deque


# bfs 함수
def bfs(answer):
    # 중복 확인용
    duplications = {}
    # 덱 생성 및 클릭 횟수 및 현재 상태 인큐
    q = deque([(0, [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])])
    # 시작 상태 중복 딕셔너리에 추가
    duplications['.........'] = 1

    while q:
        cnt, board = q.popleft()

        # 정답과 일치하면 종료
        if board == answer:
            return cnt

        # 모든 위치 순회
        for x in range(3):
            for y in range(3):
                # 버튼을 누를 저장할 복사본 판 만들기
                click = [b[:] for b in board]
                # 자기 자신 바꾸기
                if click[x][y] == '.':
                    click[x][y] = '*'
                else:
                    click[x][y] = '.'

                # 델타 탐색
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    # 벽 형성
                    if 0 <= nx < 3 and 0 <= ny < 3:
                        if click[nx][ny] == '.':
                            click[nx][ny] = '*'
                        else:
                            click[nx][ny] = '.'

                # 중복 확인
                duple = ''
                for i in range(3):
                    for j in range(3):
                        duple += click[i][j]
                # 중복 딕셔너리에 없다면 추가 및 인큐
                if duple not in duplications:
                    duplications[duple] = 1
                    q.append((cnt + 1, click))
                # 있다면 넘기기
                else:
                    continue


# 테스트 케이스의 숫자 P
P = int(input())
for tc in range(1, P + 1):
    # 맞춰야할 보드판 정답
    answer = [list(input().rstrip()) for _ in range(3)]

    print(bfs(answer))














