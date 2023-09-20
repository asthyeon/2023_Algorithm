import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모을 수 있는 에너지 양의 최댓값 구하기
1. N 개의 에너지 구슬이 일렬로 놓임
2. i 번째 에너지 구슬의 무게는 W
3. 에너지를 모으는 방법은 다음과 같고 반복 가능
 - 선택한 에너지 구슬의 번호 x, 첫 번째와 마지막 구슬 선택 불가
 - x 번째 에너지 구슬 제거
 - (x-1 번째의 무게 W) x (x+1 번째의 무게) 의 에너지를 모을 수 있음
 - N 을 1 감소 시키고, 에너지 구슬을 1 번부터 N 번까지 다시 번호 매기기
@ 풀이
(1) 백트래킹으로 풀기
"""


# 백트래킹 함수
def backtracking(num, energy, path, W):
    global max_energy
    # 재귀를 종료하는 기저 조건
    if num == N:
        if max_energy < energy:
            max_energy = energy
        return

    for i in range(1, N - 1):
        if path[i] == 0:
            continue
        left = 0
        right = 0
        # 왼쪽 탐색해서 제거되지 않은 구슬 찾기
        for l in range(i - 1, -1, -1):
            if path[l] == 1:
                left = W[l]
                break
        # 오른쪽 탐색해서 제거되지 않은 구슬 찾기
        for r in range(i + 1, N):
            if path[r] == 1:
                right = W[r]
                break
        energy += left * right
        path[i] = 0
        num += 1
        backtracking(num, energy, path, W)
        num -= 1
        path[i] = 1
        energy -= left * right


# 에너지 구슬의 개수 N
N = int(input())

# 에너지 구슬의 무게
W = list(map(int, input().split()))

path = [1] * N
num = 2
max_energy = 0
energy = 0

backtracking(num, energy, path, W)

print(max_energy)