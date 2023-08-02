import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# N 번째 영화
N = int(input())

# 반복할 숫자 형성
num = 0

# 666 이 들어간 숫자 카운트
count = 0

# 종말의 수 666 이 들어가는 숫자 반복
while True:
    # 숫자 1씩 상승
    num += 1
    # 만일 숫자에 666이 들어가있으면
    if str(666) in str(num):
        # 666이 들어간 숫자 카운트 +1
        count += 1
        # 만일 카운트가 N번째라면
        if count == N:
            # 숫자 출력 및 반복 종료
            print(num)
            break