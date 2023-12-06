import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 주사위 굴리기
[출력: 이동할 때마다 주사위의 윗 면에 쓰여있는 수 출력, 바깥 이동시 출력 X]
1. 지도의 좌표는 (r, c)
2. 주사위는 지도 위에 윗 면이 1, 동쪽을 바라보는 방향이 3인 상태
3. 가장 처음에 주사위에는 모든 면에 0이 적혀 있음
4. 주사위를 굴린 후 바닥칸이 0이면 바닥면에 쓰여 있는 수가 칸에 복사됨
5. 바닥칸이 0이 아니라면 칸에 쓰여있는 수가 바닥면에 복사됨
6. 주사위가 이동했을 때 마다 상단에 쓰여있는 값 구하기
7. 바깥으로 이동시 명령 무시하기
8. 이동명령 - 동쪽: 1 / 서쪽: 2 / 북쪽: 3 / 남쪽: 4
9. 주사위를 놓은 칸에 쓰여있는 수는 항상 0
@ 풀이
(1) 그냥 풀어보기
"""
# 지도 세로 N, 가로 M, 주사위 좌표 x, y, 명령의 개수 K
N, M, x, y, K = map(int, input().split())
arr = []
# 지도 정보 입력
for _ in range(N):
    info = list(map(int, input().split()))
    arr.append(info)

# 주사위 정보
dice = [[0] * 3 for _ in range(4)]

# 명령 입력
commands = list(map(int, input().split()))
for command in commands:
    # print(f'명령 {command} 현재 위치 ({x}, {y})')

    # 동쪽 이동
    if command == 1:
        # 주사위 좌표 이동
        y += 1
        # 벽을 넘어갈 시 취소
        if y >= M:
            y -= 1
            continue
        # 주사위 굴리기
        # 이동한 칸 확인 후 값 교체
        if arr[x][y] == 0:
            # 지도 교체
            arr[x][y] = dice[1][2]
        else:
            # 동쪽면 교체
            dice[1][2] = arr[x][y]
            arr[x][y] = 0
        # 주사위 전개도 리셋
        dice_copy = [d[:] for d in dice]
        # 상단 = 서쪽면
        dice[1][1] = dice_copy[1][0]
        # 서쪽면 = 바닥
        dice[1][0] = dice_copy[3][1]
        # 동쪽면 = 상단
        dice[1][2] = dice_copy[1][1]
        # 바닥 = 동쪽면
        dice[3][1] = dice_copy[1][2]
        # 상단면 출력
        print(dice[1][1])
        # print(f'#동쪽 {dice}')

    # 서쪽 이동
    elif command == 2:
        # 주사위 좌표 이동
        y -= 1
        # 벽을 넘어갈 시 취소
        if y < 0:
            y += 1
            continue
        # 주사위 굴리기
        # 이동한 칸 확인 후 값 교체
        if arr[x][y] == 0:
            # 지도 교체
            arr[x][y] = dice[1][0]
        else:
            # 서쪽면 교체
            dice[1][0] = arr[x][y]
            arr[x][y] = 0
        # 주사위 전개도 리셋
        dice_copy = [d[:] for d in dice]
        # 상단 = 동쪽면
        dice[1][1] = dice_copy[1][2]
        # 서쪽면 = 상단
        dice[1][0] = dice_copy[1][1]
        # 동쪽면 = 바닥
        dice[1][2] = dice_copy[3][1]
        # 바닥 = 서쪽면
        dice[3][1] = dice_copy[1][0]
        # 상단면 출력
        print(dice[1][1])
        # print(f'#서쪽 {dice}')

    # 북쪽 이동
    elif command == 3:
        # 주사위 좌표 이동
        x -= 1
        # 벽을 넘어갈 시 취소
        if x < 0:
            x += 1
            continue
        # 주사위 굴리기
        # 이동한 칸 확인 후 값 교체
        if arr[x][y] == 0:
            # 지도 교체
            arr[x][y] = dice[0][1]
        else:
            # 북쪽면 교체
            dice[0][1] = arr[x][y]
            arr[x][y] = 0
        # 주사위 전개도 리셋
        dice_copy = [d[:] for d in dice]
        # 상단 = 남쪽면
        dice[1][1] = dice_copy[2][1]
        # 북쪽면 = 상단
        dice[0][1] = dice_copy[1][1]
        # 남쪽면 = 바닥
        dice[2][1] = dice_copy[3][1]
        # 바닥 = 북쪽면
        dice[3][1] = dice_copy[0][1]
        # 상단면 출력
        print(dice[1][1])
        # print(f'#북쪽 {dice}')

    # 남쪽 이동
    elif command == 4:
        # 주사위 좌표 이동
        x += 1
        # 벽을 넘어갈 시 취소
        if x >= N:
            x -= 1
            continue
        # 주사위 굴리기
        # 이동한 칸 확인 후 값 교체
        if arr[x][y] == 0:
            # 지도 교체
            arr[x][y] = dice[2][1]
        else:
            # 남쪽면 교체
            dice[2][1] = arr[x][y]
            arr[x][y] = 0
        # 주사위 전개도 리셋
        dice_copy = [d[:] for d in dice]
        # 상단 = 북쪽면
        dice[1][1] = dice_copy[0][1]
        # 북쪽면 = 바닥
        dice[0][1] = dice_copy[3][1]
        # 남쪽면 = 상단
        dice[2][1] = dice_copy[1][1]
        # 바닥 = 남쪽면
        dice[3][1] = dice_copy[2][1]
        # 상단면 출력
        print(dice[1][1])
        # print(f'#남쪽 {dice}')