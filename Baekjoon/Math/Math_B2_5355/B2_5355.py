import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# T값 받기
T = int(input())
# 테스트 케이스만큼 반복
for tc in range(1, T + 1):
    # 화성 수학식
    calcul = input().split()
    
    # 화성 연산자
    MARS = ['@', '%', '#']

    # 수를 계산할 변수 생성
    num = 0
    # 화성 수학식 리스트만큼 반복
    for i in calcul:
        # i 가 화성 연산자에 있다면
        if i in MARS:
            if i == '@':
                num *= 3
            elif i == '%':
                num += 5
            else:
                num -= 7
        # i 가 화성 연산자에 없다면 첫 번째 수
        else:
            num += float(i)
    
    # 뒤에 0 하나 더 붙이기
    print(round(num, 2), 0, sep="")