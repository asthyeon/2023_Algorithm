import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 적어도 M 미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값 구하기
1. 목재절단기 동작
- 절단기에 높이 H 지정
- 톱날이 땅으로부터 H 미터 위로 올라감
- 한 줄에 연속해있는 나무 모두 절단
- 높이가 H보다 큰 나무는 H 위의 부분이 잘림
- 낮은 나무는 잘리지 않음
2. 나무를 필요한 만큼만 자름
@ 풀이
(1) 이분 탐색 사용
"""


# 이분탐색 함수
def binary_search(M, trees):
    start = 0
    end = max(trees)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        # 자른 나무의 길이
        wood = 0
        for tree in trees:
            # 자른 값이 음수가 아니라면
            if tree - mid >= 0:
                wood += tree - mid
        # 자르고 남은 나무의 길이가 필요한 나무만큼이라면 종료
        if wood == M:
            result = mid
            break
        # 자르고 남은 나무의 길이가 필요한 나무보다 길다면
        if wood > M:
            result = mid
            start = mid + 1
        # 자르고 남은 나무의 길이가 필요한 나무보다 짧다면
        else:
            result = mid
            end = mid - 1

    return print(result)


# 나무의 수 N, 필요한 나무 길이 M
N, M = map(int, input().split())

# 나무의 높이들
trees = list(map(int, input().split()))

binary_search(M, trees)