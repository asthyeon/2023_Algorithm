import sys
sys.stdin = open('input.txt')

'''
# 델타 탐색을 이용해 파리 잡기
'''

# 테스트 케이스 개수
T = int(input())
# 각 테스트 케이스
for tc in range(1, T + 1):
    # 파리 영역: N, 파리채: M
    N, M = map(int, input().split())
    # 파리 영역 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 최대 파리가 죽은 수
    max_dead = 0

    # 0, 0 에서부터 파리 영역 생성
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # 델타 탐색 상방향 이동은 필요 없음
            for di, dj in [[0, 1], [1, 0], [0, -1]]:
                dead = 0
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    for k in range(i, M + i):
                        for l in range(j, M + j):
                            dead += arr[k][l]
                if max_dead < dead:
                    max_dead = dead

    print(f'#{tc} {max_dead}')