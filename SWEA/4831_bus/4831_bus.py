import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 한 번 충전으로 이동 가능한 정류장 수:K,
    # 종점 번호: N,
    # 충전기가 설치된 정류장 수:M
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장 번호
    arr = list(map(int, input().split()))
    # 충전 횟수
    charging = 0
    # 현재 위치
    position = 0

    # 현재 위치에서 K만큼 갔을 때 종착점보다 커질 때까지 반복
    while position + K < N:
        # 범위를 역순으로 K만큼 이동 반복(건너 뛸 수 있기 때문)
        for i in range(K, 0, -1):
            # i 만큼 이동했을 때 충전 정류장일 경우
            if (position + i) in arr:
                # i 만큼 이동
                position += i
                # 충전 횟수 증가
                charging += 1
                # 반복 종료
                break
        # 범위 안에 충전소가 없으면 종착점 도달 불가능으로 0 출력
        else:
            charging = 0
            break

    print(f'#{tc} {charging}')