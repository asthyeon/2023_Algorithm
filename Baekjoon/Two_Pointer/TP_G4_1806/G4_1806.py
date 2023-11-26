import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 부분합
[출력: 구하고자 하는 최소의 길이 출력, 합을 만드는 것이 불가능하다면 0 출력]
1. 수열에서 연속된 수들의 부분합 중에서 그 합이 S 이상이 되는 것 중 가장 짧은 것의 길이 구하기
@ 풀이
(1) 투 포인터 사용
(2) 누적합도 이용해야 시간초과가 안남
(3) end를 0에서 시작
(4) 정렬 X
"""

# N짜리 수열, 합 S
N, S = map(int, input().split())
# 수열
sequence = list(map(int, input().split()))

start = 0
end = 0
answer = 100000000
total = sequence[start]
while True:
    # 합이 S 이상이고 길이가 더 짧으면 교체
    if total >= S:
        if answer > (end - start + 1):
            answer = end - start + 1
        total -= sequence[start]
        start += 1
    # 합이 S 미만이면 end 증가
    else:
        end += 1
        # 마지막이 N에 도달하면 종료
        if end == N:
            break
        total += sequence[end]

if answer == 100000000:
    print(0)
else:
    print(answer)