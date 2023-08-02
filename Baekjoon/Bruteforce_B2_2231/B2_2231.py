import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 분해합: N
N = int(input())

# 가장 작은 생성자 구하기
for i in range(N):
    # i 를 문자열로 바꾸고, map으로 자릿수를 하나씩 분리하여 다시 정수형으로 변환
    # 각 자릿 수를 더하고 i 자체를 더한 값이 N이랑 같다면 생성자이므로 i 출력
    if N == i + sum(map(int, str(i))):
        print(i)
        # 가장 작은 생성자 출력을 위해 i 값이 나오면 반복문 종료
        break
# 생성자가 없다면 0 출력
else:
    print(0)
