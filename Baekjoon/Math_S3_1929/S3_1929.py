import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# M 이상 N 이하의 소수 모두 출력
1. 소수를 구하는 에라토스테네스의 체 사용해보기
'''

# M 이상 N 이하
M, N = map(int, input().split())

# 처음엔 모든 수가 소수인 것으로 가정
arr = [True for i in range(N + 1)]

# 에라토스테네스의 체 알고리즘
for i in range(2, (int(N ** 0.5) + 1)):
    # i가 소수인 경우 (남은 수인 경우)
    if arr[i] == True:
        # i 를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= N:
            arr[i * j] = False
            j += 1

# 모든 소수 출력
# M 이상부터 시작하므로 범위 설정
for i in range(M, N + 1):
    if i > 1:
        if arr[i]:
            print(i)