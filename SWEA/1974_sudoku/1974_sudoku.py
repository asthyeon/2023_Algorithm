import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 정답 값
    ans = 1

    # 가로 중복 확인
    for i in range(9):
        # 중복을 제거할 빈 세트 만들기
        set_arr = set()
        for j in range(9):
            # 빈 세트에 가로 값 붙이기
            set_arr.add(arr[i][j])
        # 만약 세트의 길이가 9가 안된다면
        if len(set_arr) < 9:
            # 정답 값을 0 으로 바꿔 오답으로 만들기
            ans = 0
    
    # 세로 중복 확인
    for j in range(9):
        set_arr = set()
        for i in range(9):
            set_arr.add(arr[i][j])
        if len(set_arr) < 9:
            ans = 0

    # 3x3 중복 확인
    # 3칸씩 건너뛰기
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            set_arr = set()
            # 가로로 3칸까지만 가고, 세로로 3줄까지만 가기
            for i3 in range(0 + i, 3 + i):
                for j3 in range(0 + j, 3 + j):
                    set_arr.add(arr[i3][j3])
            if len(set_arr) < 9:
                ans = 0

    print(f'#{tc} {ans}')