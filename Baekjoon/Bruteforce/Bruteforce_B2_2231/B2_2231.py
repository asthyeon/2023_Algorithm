import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 분해합: N
N = int(input())

# 가장 작은 생성자 구하기
for i in range(N):    
    # 각 자릿수 합
    num_sum = 0    
    
    # 각 자릿수를 구하고 합에 집어넣기
    j = i
    while True:
        if j < 10:
            num_sum += j % 10
            break
        else:
            num_sum += j % 10
            j = j // 10

    # 각 자릿수와 숫자 자체를 더해서 생성자가 맞는지 확인
    if N == i + num_sum:
        print(i)
        # 가장 작은 생성자 출력을 위해 i 값이 나오면 반복문 종료
        break
# 생성자가 없다면 0 출력
else:
    print(0)