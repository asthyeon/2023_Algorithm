import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수열 A가 주어졌을 때 이 수열에서 적절히 몇 개의 원소를 빼서 이 수열을 삼각 수열로 만들기
[출력: 가장 긴 부분 삼각 수열의 길이 출력]
1. x, y, z 가 x + y > z, x + z > y, y + z > x 의 관계를 만족하면 세 수는 삼각관계에 있다.
2. 길이가 N인 수열 B의 모든 b[i], b[j], b[k]가 삼각관계에 있으면 이 수열은 삼각 수열
3. i, j, k는 모두 다른 값이다
4. N == 1 -> 비교가 불가능 1로 처리
5. N == 2 -> 비교가 불가능 2로 처리
6. N >= 3 -> 이 때부터 비교를 하며 가능하면 길이를 늘리고 아니면 2로 처리
@ 풀이
(1) 일단 해보기
 - A = [1, 2, 3]
   1 + 2 > 3 (X) => 불성립
 - A = [2, 3, 4, 1, 3, 4, 5]
   2 + 3 > 4
   2 + 4 > 3
   3 + 4 > 2
(2) dp 사용
- dp의 인덱스는 배열의 숫자의 인덱스, dp의 값은 그 숫자까지의 부분 수열의 길이
- 이전의 값들 중 2로 시작하는 값부터 비교
- 값을 비교하는 것이기 때문에 정렬한 후에 작은 값부터 비교
- A = [1, 2, 3, 3, 4, 4, 5]
  dp[0] = 1 (기본 값)
  dp[1] = 2 (기본 값)
  dp[2] = 2 (X) 1, 2, 3
  dp[3] = 3 (O) 2, 3, 3
  dp[4] = 4 (O) 2, 3, 4
  dp[5] = 5 (O) 2, 3, 4
  dp[6] = 2 (X) 2, 3, 5
"""


# dp 함수
def dynamic_programming(A):
    dp = [2] * N
    dp[0] = 1
    dp[1] = 2
    # 모든 dp 값을 지정하기 위한 반복
    for i in range(2, N):
        # 이전의 값들 중 가장 먼저 발견한 2를 찾을 때까지 반복(역순)
        for j in range(i - 1, -1, -1):
            if dp[j] == 2:
                for k in range(j, i):
                    x = A[k - 1]
                    y = A[k]
                    z = A[i]
                    # 가장 작은 값 2개를 더하고 가장 큰 값과 비교만 하면 성립 여부 확인가능
                    if x + y > z:
                        # 성립 시 직전에 할당된 값과 비교 값 +1 중 큰 값(직전까지 성립했다는 의미이므로)
                        dp[i] += 1
                break

    # print(f'dp: {dp}')
    return max(dp)


# 수열의 크기 N
N = int(input())
# 수열 A
A = list(map(int, input().split()))

# N 이 3 보다 작을 때는 N 값 출력
if N < 3:
    print(N)
    exit()

# 수열 오름차순 정렬
A.sort()
# print(f'A: {A}')
print(dynamic_programming(A))




















