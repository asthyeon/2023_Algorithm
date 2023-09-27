import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# -1, 0, 1 각 숫자로만 채워진 종이의 개수를 순서대로 출력하기
1. 행렬을 자르는 규칙
 [1] 종이가 모두 같은 수라면 그대로 사용
 [2] [1]이 아닌 경우 종이를 9 개로 자르고 과정 반복
2. 종이는 각 칸에 -1, 0, 1 저장
"""


# 분할 함수
def divide(sx, sy, N, arr):
    global minus
    global zero
    global one
    start = 2
    stop = 0
    for x in range(sx, sx + N):
        for y in range(sy, sy + N):
            # 첫 항에 따라 종류 정하기
            if x == sx and y == sy:
                if arr[x][y] == -1:
                    start = -1
                elif arr[x][y] == 0:
                    start = 0
                else:
                    start = 1
            # 그 후로 다른 종류를 만나면 중지
            else:
                if start == -1:
                    if arr[x][y] != -1:
                        stop = 1
                        break
                elif start == 0:
                    if arr[x][y] != 0:
                        stop = 1
                        break
                else:
                    if arr[x][y] != 1:
                        stop = 1
                        break
        # 중지 신호라면 반복 종료
        if stop == 1:
            break
    # 중지 신호라면 재분할
    if stop == 1:
        # 1/9
        divide(sx, sy, N // 3, arr)
        # 2/9
        divide(sx, sy + (N // 3), N // 3, arr)
        # 3/9
        divide(sx, sy + ((N // 3) * 2), N // 3, arr)
        # 4/9
        divide(sx + (N // 3), sy, N // 3, arr)
        # 5/9
        divide(sx + (N // 3), sy + (N // 3), N // 3, arr)
        # 6/9
        divide(sx + (N // 3), sy + ((N // 3) * 2), N // 3, arr)
        # 7/9
        divide(sx + ((N // 3) * 2), sy, N // 3, arr)
        # 8/9
        divide(sx + ((N // 3) * 2), sy + (N // 3), N // 3, arr)
        # 9/9
        divide(sx + ((N // 3) * 2), sy + ((N // 3) * 2), N // 3, arr)
    # 중지 신호가 아니라면
    else:
        if start == -1:
            minus += 1
            return
        elif start == 0:
            zero += 1
            return
        else:
            one += 1
            return


# 행렬의 크기 N
N = int(input())

# 행렬
arr = [list(map(int, input().split())) for _ in range(N)]

# 각 종류에 대한 카운트
minus = 0
zero = 0
one = 0

divide(0, 0, N, arr)

print(minus)
print(zero)
print(one)