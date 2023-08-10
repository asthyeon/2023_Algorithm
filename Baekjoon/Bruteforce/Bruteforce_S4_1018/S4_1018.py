import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# N 개의 행, M 개의 열
N, M = map(int, input().split())
# 배열 형성
arr = [input() for _ in range(N)]
# 색칠한 횟수 리스트
color_list = []

# 배열 내에서 자를 체스판 형성
# 마지막 열도 포함하기 위해서 -7 을 해주기
for i in range(N-7):
    for j in range(M-7):

        # 블랙으로 시작하는 체스판으로 가정
        # 블랙으로 시작한 칠한 횟수
        count_B = 0
        # 화이트로 시작한 칠한 횟수
        count_W = 0
        # 가로 행 형성
        for r in range(i, i + 8):
            # 세로 열 형성
            for c in range(j, j + 8):
                # 블랙으로 시작한다면
                if arr[i][j] == 'B':
                    if r % 2 == 0:
                        if c % 2 == 0:
                            if arr[r][c] != 'B':
                                count_B += 1
                        else:
                            if arr[r][c] != 'W':
                                count_B += 1
                    else:
                        if c % 2 == 0:
                            if arr[r][c] != 'W':
                                count_B += 1
                        else:
                            if arr[r][c] != 'B':
                                count_B += 1
                # 화이트로 시작한다면
                else:
                    if r % 2 == 0:
                        if c % 2 == 0:
                            if arr[r][c] != 'W':
                                count_W += 1
                        else:
                            if arr[r][c] != 'B':
                                count_W += 1
                    else:
                        if c % 2 == 0:
                            if arr[r][c] != 'B':
                                count_W += 1
                        else:
                            if arr[r][c] != 'W':
                                count_W += 1
        
        # 0 값을 제외하기 위해 비교
        if count_B > count_W:
            color_list.append(count_B)
        else:
            color_list.append(count_W)

        # 화이트판으로 시작하는 체스판으로 가정
        # 블랙으로 시작한 칠한 횟수
        count_B2 = 0
        # 화이트로 시작한 칠한 횟수
        count_W2 = 0
        # 가로 행 형성
        for r in range(i, i + 8):
            # 세로 열 형성
            for c in range(j, j + 8):
                # 블랙으로 시작한다면
                if arr[i][j] != 'B':
                    if r % 2 == 0:
                        if c % 2 == 0:
                            if arr[r][c] != 'B':
                                count_B2 += 1
                        else:
                            if arr[r][c] != 'W':
                                count_B2 += 1
                    else:
                        if c % 2 == 0:
                            if arr[r][c] != 'W':
                                count_B2 += 1
                        else:
                            if arr[r][c] != 'B':
                                count_B2 += 1
                # 화이트로 시작한다면
                else:
                    if r % 2 == 0:
                        if c % 2 == 0:
                            if arr[r][c] != 'W':
                                count_W2 += 1
                        else:
                            if arr[r][c] != 'B':
                                count_W2 += 1
                    else:
                        if c % 2 == 0:
                            if arr[r][c] != 'B':
                                count_W2 += 1
                        else:
                            if arr[r][c] != 'W':
                                count_W2 += 1
        
        # 0 값을 제외하기 위해 비교
        if count_B2 > count_W2:
            color_list.append(count_B2)
        else:
            color_list.append(count_W2)

# 최소값 출력
print(min(color_list))