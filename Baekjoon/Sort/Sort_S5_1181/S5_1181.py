import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 단어 정렬
1. 길이가 짧은 것부터
2. 같으면 사전 순
3. 중복된 단어는 하나만 남기고 제거
'''

# 단어의 개수
N = int(input())

# 단어 입력
words = []
for _ in range(N):
    words.append(input().rstrip())

# 사전순 정렬
words.sort()


# 병합 정렬 함수
def merge_sort(arr, start, end):
    if start < end:
        middle = (start + end) // 2 # 중간점
        merge_sort(arr, start, middle) # 전반부 정렬
        merge_sort(arr, middle + 1, end) # 후반부 정렬
        merge(arr, start, middle, end) # 병합


# 병합 정렬 함수
def merge(arr, start, middle, end):
    i = start
    j = middle + 1
    t = 0
    # 병합을 위한 tmp 형성
    tmp = []
    # 분할된 부분까지 tmp 내의 원소들을 정렬
    while i <= middle and j <= end:
        # 시작점의 원소가 더 작다면
        if len(arr[i]) <= len(arr[j]):
            # 위치 그대로
            tmp.append(arr[i])
            t += 1
            i += 1
        # 시작점의 원소가 더 크다면
        else:
            # 위치 변경
            tmp.append(arr[j])
            t += 1
            j += 1
    # 왼쪽 배열 부분이 남은 경우 재반복
    while i <= middle:
        tmp.append(arr[i])
        t += 1
        i += 1
    # 오른쪽 배열 부분이 남은 경우 재반복
    while j <= end:
        tmp.append(arr[j])
        t += 1
        j += 1
    # 초기화
    i = start
    t = 0
    # 원래의 배열을 정렬된 tmp로 바꿔주기(병합)
    while i <= end:
        # 원래의 요소를 정렬된 요소로 바꾸기 (저장 횟수 + 1)
        arr[i] = tmp[t]
        i += 1
        t += 1

# 시간초과 방지를 위해 병합 정렬 사용
merge_sort(words, 0, N - 1)

# 중복 단어 제거
stack = []
for word in words:
    if word not in stack:
        stack.append(word)

# 출력
for o in range(len(stack)):
    print(stack[o])