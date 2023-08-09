import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 정수 n이 주어졌을 때 n보다 크거나 같은 소수 중 가장 작은 소수 찾기
1. 소수: 1 과 자기 자신으로만 나누어지는 수
2. while 문으로 소수를 찾는 것 -> 시간 초과
3. √N 을 이용해야함 -> √N 이하로만 나눠보기
'''

T = int(input())
for tc in range(1, T + 1):
    # 정수 n
    n = int(input())

    # 함수 이용
    def prime(n):
        # n 이 0 과 1 이 아닐 때
        if n == 0 or n == 1:
            # 소수 제외
            return False
        # n 이 1 보다 클 때
        else:
            # 2보다 크고 루트 n + 1 보다 작은 정수로 반복
            for i in range(2, (int(n ** 0.5) + 1)):
                # n 이 i 로 나눠지면
                if (n % i) == 0:
                    # 소수 제외
                    return False
            # 위 반복문을 통과했을 때 소수 인정
            return True
    
    # while 반복
    while True:
        # 소수라면
        if prime(n) == True:
            # 출력 후 반복문 종료
            print(n)
            break
        # 소수가 아니라면
        else:
            # n 값 증가 후 반복
            n += 1

    # # 시간 초과
    # # 루트 n 이하로 나누기
    # while True:
    #     # 소수 조건 만들기 (1 일때 소수)
    #     prime = True
    #     # n 이 2 보다 클 때
    #     if n > 1:
    #         # 2 부터 n 보다 작거나 같은 수로 순회
    #         for i in range(2, (int(n ** 0.5) + 1)):
    #             # 만일 n 보다 작거나 같은 수로 나눠진다면
    #             if (n % i) == 0:
    #                 # 소수를 제외하고 n 값을 증가시킨후 반복문 종료
    #                 n += 1
    #                 prime = False
    #                 break
    #     else:
    #         prime = False
    #     # 소수일 경우 종료
    #     if prime is True:
    #         break
    #
    # print(n)

    # # 시간 초과
    # # n 보다 크거나 같은 수를 계속 나눠보기
    # while True:
    #     # 소수 조건 만들기 (1 일때 소수)
    #     dec = 1
    #     # 2 부터 n 보다 작거나 같은 수로 순회
    #     for i in range(2, n):
    #         # 만일 n 보다 작거나 같은 수로 나눠진다면
    #         if (n % i) == 0:
    #             # 소수를 제외하고 n 값을 증가시킨후 반복문 종료
    #             n += 1
    #             dec -= 1
    #             break
    #     # 소수일 경우 종료
    #     if dec == 1:
    #         break
    #
    # print(n)