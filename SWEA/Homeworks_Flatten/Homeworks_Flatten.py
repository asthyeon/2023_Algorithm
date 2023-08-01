import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 덤프 횟수: T
    T = int(input())
    # 각 상자의 높이값(100개)
    arr = list(map(int, input().split()))

    # 오름차순으로 정렬(버블 정렬)
    for i in range(99, 0, -1):
        for j in range(0, 99):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # 덤프 횟수 만큼 반복
    for dump in range(1, T + 1):
        # 제일 높은 상자 -1
        arr[99] -= 1
        # 제일 낮은 상자 +1
        arr[0] += 1
        # 재정렬
        for i in range(99, 0, -1):
            for j in range(0, 99):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # 최대 값과 최소 값의 차이
    ans = arr[99] - arr[0]
    
    print(f'#{tc} {ans}')
                


