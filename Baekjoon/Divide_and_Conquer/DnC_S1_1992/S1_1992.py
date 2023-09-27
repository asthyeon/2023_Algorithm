import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N x N 크기의 영상을 압축한 결과 출력
1. 쿼드 트리: 흑백 영상을 압축하여 표현하는 데이터 구조
2. 흰 점을 나타내는 0, 검은 점을 나타내는 1
3. 모두 0일 경우 압축 결과 0, 모두 1일 경우 압축 결과 1
4. 0과 1이 섞여 있으면 전체를 한 번에 나타내지 못하고 4등분(반복)
5. 4등분한 영역의 결과를 차례대로 괄호 안에 묶어서 표현
@ 풀이
(1) 분할정복 이용
"""


# 분할 함수
def divide(sx, sy, N, arr):
    global compression
    start = -1
    stop = 0
    for x in range(sx, sx + N):
        for y in range(sy, sy + N):
            # 처음 것이 무슨 색인지 확인
            if x == sx and y == sy:
                # 흰 색으로 시작할 때
                if arr[x][y] == 0:
                    start = 0
                # 검은 색으로 시작할 때
                else:
                    start = 1
            # 처음 이후
            else:
                # 흰 색으로 시작 했을 때 검은 색을 만나면 중지
                if start == 0:
                    if arr[x][y] == 1:
                        stop = 1
                        break
                # 검은 색으로 시작 했을 때 흰 색을 만나면 중지
                else:
                    if arr[x][y] == 0:
                        stop = 1
                        break
        # 중지 신호라면 반복 종료
        if stop == 1:
            break
    # 중지 신호라면 괄호를 치며 안에 넣기
    if stop == 1:
        compression += '('
        divide(sx, sy, N // 2, arr)
        divide(sx, sy + N // 2, N // 2, arr)
        divide(sx + N // 2, sy, N // 2, arr)
        divide(sx + N // 2, sy + N // 2, N // 2, arr)
        compression += ')'
        return
    # 중지 신호가 아니라면 그대로 색상 출력
    else:
        compression += str(start)


# 영상의 크기 N
N = int(input())

# 영상
arr = [list(map(int, input().rstrip())) for _ in range(N)]

# 압축 결과
compression = ''

# 함수 사용
divide(0, 0, N, arr)

print(compression)