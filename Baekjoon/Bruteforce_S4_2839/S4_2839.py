import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 설탕 N 킬로그램
N = int(input())
# 봉지 가져가는 횟수 리스트
bag = []

# 브루트포스 방식으로 탐색
for i in range(3000):
    for j in range(3000):
        # 만일 N 이 3 과 5 의 조합으로 나타낼 수 있다면
        if N == (3 * i) + (5 * j):
            # bag 에 i+j 의 봉지 개수 더하기
            bag.append(i + j)

# 만일 봉지가 없다면 -1 출력
if bag == []:
    print(-1)
# 봉지가 있다면 bag 최솟값 출력
else:
    print(min(bag))