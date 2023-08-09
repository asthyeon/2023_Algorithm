import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 베르트랑 공준: 
# 임의의 자연수 n에 대하여 n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다
# n보다 크고 2n보다 작거나 같은 소수의 개수 출력
1. 마지막이 0이 입력되므로 while 반복문으로 구성
2. 기존 에라토스테네스의 체 이용시 시간 초과((246,912 + 1)로 해도 초과))
3. 반복문 밖으로 소수 에라토스테네스의 체로 만든 리스트를 꺼내기
'''

# 소수를 넣을 리스트 생성(초기값은 True)
arr = [True for _ in range(246913)]

# 에라토스테네스의 체 이용
for i in range(2, (int(246912 ** 0.5) + 1)):
    # i 가 소수인 경우
    if arr[i] is True:
        # i 를 제외한 모든 i 의 배수 지우기
        j = 2
        while (i * j) <= 246912:
            arr[i * j] = False
            j += 1

# 시간 초과
while True:
    # 자연수 n
    n = int(input())

    # 종료 조건
    if n == 0:
        break

    # 모든 소수 개수 출력
    # n 보다 크고 2n 보다 작거나 같은 소수
    count = 0
    for k in range((n + 1), ((2 * n) + 1)):
        if k > 1:
            if arr[k]:
                count += 1
    print(count)





