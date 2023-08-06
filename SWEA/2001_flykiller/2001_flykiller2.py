import sys
sys.stdin = open('input.txt')

'''
# 그냥 탐색으로 잡기
'''

# 테스트 케이스 개수
T = int(input())
# 각 테스트 케이스
for tc in range(1, T + 1):
    # 파리 영역: N, 파리채: M
    N, M = map(int, input().split())
    # 파리 영역 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 파리 최대 죽은 수
    max_dead = 0

    # 탐색
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            dead = 0
            for k in range(i, M + i):
                for l in range(j, M + j):
                    dead += arr[k][l]
            if max_dead < dead:
                max_dead = dead
    
    print(f'#{tc} {max_dead}')