import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 한 변 N이 주어질 때 흰색과 파란색 색종이의 개수 구하기
1. 각 정사각형들은 하얀색이나 파란색으로 칠해져 있음
2. 일정한 규칙으로 잘라 다양한 크기의 정사각형 모양의 흰색 혹은 파란색 색종이를 만들려고 함
3. 종이 자르는 규칙
 - 전체 종이가 모두 같은색이 아니라면 4등분
 - 또 같은색이 아니라면 4등분
 - 모두 같은색이 되거나 하나의 정사각형이 될 때까지 반복
"""


# 분할 정복 함수
def divide(sx, sy, N, arr):
    global white
    global blue
    # 1칸일 때
    if N == 1:
        # 흰색일 때 +1
        if arr[sx][sy] == 0:
            white += 1
        # 파랑일 때 +1
        else:
            blue += 1
        return
    
    # 시작 및 정지 변수
    start = 0
    stop = 0
    for x in range(sx, sx + N):
        for y in range(sy, sy + N):
            # 처음의 색상이
            if x == sx and y == sy:
                # 흰색일 때
                if arr[x][y] == 0:
                    start = 0
                # 파랑일 때
                else:
                    start = 1
            # 처음 이후로 다른 색상을 만날 때
            else:
                # 흰색이 파랑을 만나면 반복 종료
                if start == 0:
                    if arr[x][y] == 1:
                        stop = 1
                        break
                # 파랑이 흰색을 만나면 반복 종료
                else:
                    if arr[x][y] == 0:
                        stop = 1
                        break
        # 정지일 때 반복 종료
        if stop == 1:
            break
    # 순회를 했다면(정지 X)
    else:
        # 흰색일 때 +1
        if start == 0:
            white += 1
        # 파랑일 때 +1
        else:
            blue += 1
        return
    # 정지일 때 분할
    if stop == 1:
        # 왼쪽 위
        divide(sx, sy, N // 2, arr)
        # 오른쪽 위
        divide(sx, sy + (N // 2), N // 2, arr)
        # 왼쪽 아래
        divide(sx + (N // 2), sy, N // 2, arr)
        # 오른쪽 아래
        divide(sx + (N // 2), sy + (N // 2), N // 2, arr)


# 한 변의 길이 N
N = int(input())

# 색종이 배열
arr = [list(map(int, input().split())) for _ in range(N)]
# 각 색종이 개수
white = blue = 0

# 함수 사용
divide(0, 0, N, arr)

print(white)
print(blue)