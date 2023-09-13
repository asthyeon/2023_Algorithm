import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하기
@ 풀이
(1) 이중 포문이 아닌 방법을 찾기
(2) 부분합 경우의 수
       1 3 6 7 9 -> 3개
나머지 1 0 0 1 0
         2 5 6 8 -> 1개
나머지   2 2 0 2
           3 4 6 -> 2개
나머지     0 1 0  
             1 3 -> 1개
나머지       1 0
               2 -> 0개
나머지         0
               합 : 7개 
(3) 누적합 리스트에서 부분합 구하기
pre_sum[i] - pre_sum[i - 1] 
(4) 이 부분합을 M으로 나눴을 때 나머지가 0
(pre_sum[i] - pre_sum[i - 1]) / M = 0
(5) 분배 법칙
pre_sum[i] / M = pre_sum[i - 1] / M
(6) 나머지가 같은 경우를 찾으면 됨
조합 nCr = 서로 다른 n 개 중에 r 개를 선택
5C2 서로 다른 5개 중에 2개를 선택 
= 5! / (5 - 2)! x 2!
= 5 x 4 x 3 x 2 x 1 / (3 x 2 x 1) x (2 x 1)
= 5 x 4 / 2
= n(n-1) / r 
(7) 부분합이 아닌 그 자체 누적합으로 나머지가 0인 경우도 더하기
# 결론
나머지가 같은 부분합의 개수 구하기
나머지가 같은 부분합 중 2개를 찾는 조합 수 + 나머지가 그 자체로 0인 누적합 수
"""

# 수 N, 나누는 수 M
N, M = map(int, input().split())

# N 개의 수
N_list = list(map(int, input().split()))

# 나머지가 같은 수 리스트
same_remain = [0] * M
# 누적합의 나머지 구하기
pre_sum = 0
remain = [0] * N
for i in range(N):
    # 누적합
    pre_sum += N_list[i]
    # 누적합의 나머지
    remain[i] = pre_sum % M
    # 나머지에 해당하는 나머지가 같은 수 리스트 +1
    same_remain[pre_sum % M] += 1

# 누적합 그 자체로 나머지가 0인 경우 미리 더하기
cnt = same_remain[0]
# 조합 공식으로 나머지가 같은 수 2개를 선택하는 경우의 수 더하기
for j in range(M):
    cnt += (same_remain[j] * (same_remain[j] - 1)) // 2

print(cnt)

