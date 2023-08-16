import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 병합 정렬
1. 배열 A 에 K 번째 저장되는 수를 출력하기
2. 저장 횟수가 K 보다 작으면 -1 출력
'''

# 배열 A 의 크기 N, 저장 횟수 K
N, K = map(int, input().split())

# 서로 다른 배열 A의 원소
A = list(map(int, input().split()))

# 시작점과 끝점
start = 0
end = N - 1

# 저장 횟수
count = 0
# 저장되는 수
result = -1


# 분할 정복 함수
def merge_sort(arr, start, end):
    if start < end:
        middle = (start + end) // 2 # 중간점
        merge_sort(arr, start, middle) # 전반부 정렬
        merge_sort(arr, middle + 1, end) # 후반부 정렬
        merge(arr, start, middle, end) # 병합


# 병합 함수
def merge(arr, start, middle, end):
    # 전역 변수 지정
    global count
    global result
    i = start
    j = middle + 1
    t = 0
    # 기존 배열의 복사본
    tmp = arr[::]
    # 시작점이 중간점보다 작거나 같고 중간점이 끝점보다 작거나 같을 때
    while i <= middle and j <= end:
        # 시작점의 원소가 더 작다면
        if arr[i] <= arr[j]:
            # 위치 그대로
            tmp[t] = arr[i]
            t += 1
            i += 1
        # 시작점의 원소가 더 크다면
        else:
            # 위치 변경
            tmp[t] = arr[j]
            t += 1
            j += 1
    # 왼쪽 배열 부분만 남은 경우 재반복
    while i <= middle:
        tmp[t] = arr[i]
        t += 1
        i += 1
    # 오른쪽 배열 부분만 남은 경우 재반복
    while j <= end:
        tmp[t] = arr[j]
        t += 1
        j += 1
    # 초기화
    i = start
    t = 0
    # 시작점부터 끝점까지 저장횟수 저장
    while i <= end:
        arr[i] = tmp[t]
        count += 1
        if count == K:
            result = A[i]
            break
        i += 1
        t += 1

merge_sort(A, start, end)
print(result)