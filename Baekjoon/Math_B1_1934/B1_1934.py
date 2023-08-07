import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# A 와 B 의 최소 공배수 구하기

'''

T = int(input())
for tc in range(1, T + 1):
    # 자연수 A, B
    A, B = map(int, input().split())

    # 소인수 분해 함수
    def Fatorization(number):
        # 각 소인수
        two = 0
        thr = 0
        fiv = 0
        sev = 0
        ele = 0
        while True:
            if number % 2 == 0:
                number = number / 2
                two += 1
            if number % 3 == 0:
                number = number / 3
                thr += 1
            if number % 5 == 0:
                number = number / 5
                fiv += 1
            if number % 7 == 0:
                number = number / 7
                sev += 1
            if number % 11 == 0:
                number = number / 11
                ele += 1
            if number == 1:
                break
        # 비교할 소인수 리스트 구하기
        primes = [two, thr, fiv, sev, ele]
        return primes

    # 소인수 리스트로 최소 공배수 구하기

    # 최소공배수로 사용할 리스트
    multiples = []

    # 두 리스트를 비교하여 더 큰 값을 multiples 에 넣기
    for i in range(5):
        if Fatorization(A)[i] >= Fatorization(B)[i]:
            multiples.append(Fatorization(A)[i])
        else:
            multiples.append(Fatorization(B)[i])

    # 최소 공배수 구하기
    common_multiple = (2 ** multiples[0]) * (3 ** multiples[1]) * (5 ** multiples[2]) * (7 ** multiples[3]) * (11 ** multiples[4])
    print(common_multiple)