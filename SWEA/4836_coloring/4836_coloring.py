import sys
sys.stdin = open('sample_input.txt')

'''
값 한 번에 받기
'''
T = int(input())
for tc in range(1, T + 1):
    # 첫 줄에 칠할 영역의 개수
    N = int(input())
    # 색칠판 형성
    color = [[0] * 10 for _ in range(10)]
    
    # 색칠하기
    # 범위 및 색상 정보
    for i in range(N):
        arr = list(map(int, input().split()))
    
        # 색칠하기
        for j in range(arr[0], arr[2] + 1):
            for k in range(arr[1], arr[3] + 1):
                if arr[4] == 1:
                    if color[j][k] == 0 or color[j][k] == 2:
                        color[j][k] += arr[4]
                else:
                    if color[j][k] == 0 or color[j][k] == 1:
                        color[j][k] += arr[4]
    
    # 보라색 영역 탐색
    purple = 0
    for i in color:
        for j in i:
            if j == 3:
                purple += 1

    print(f'#{tc} {purple}')