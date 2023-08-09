import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다
# 골드바흐 파티션: 짝수 N을 두 소수의 합으로 나타내는 표현
# 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수 구하기
1. 두 소수의 순서만 다른 것은 같은 파티션
2. 에라토스테네스의 체 이용
'''

T = int(input())

# 소수 리스트 생성(초기값 True)
arr = [True for _ in range(1000001)]
for i in range(2, (int(1000000 ** 0.5) + 1)):
    # i 가 소수일 때,
    if arr[i] is True:
        # i 를 제외한 i 의 배수 지우기
        j = 2
        while (i * j) <= 1000000:
            arr[i * j] = False
            j += 1

for tc in range(1, T + 1):
    N = int(input())

    # 두 소수의 합은 N
    count = 0
    # 이중 포문을 안쓰기 위해 N 을 2로 나누고 N / 2 값도 넣기 위해 + 1
    for k in range(2, (int(N / 2) + 1)):
        if arr[k] is True and arr[N - k] is True:
            count += 1

    print(count)

# # 시간초과
# for tc in range(1, T + 1):
#     N = int(input())
#
#     # 두 소수의 합은 N
#     count = 0
#     for k in range(2, N):
#         for l in range(2, N):
#             if arr[k] is True and arr[l] is True:
#                 if N == (k + l):
#                     # 중복 제거하기
#                     if k == l:
#                         count += 1
#                     else:
#                         count += 0.5
#
#     print(int(count))



