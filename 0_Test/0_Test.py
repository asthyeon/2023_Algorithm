import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이차원 배열과 연산
[출력: A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간 출력, 100초가 지나도 안되면 -1]
1. 3 x 3 배열 A의 인덱스는 1부터 시작 및 1초가 지날 때 마다 연산 적용
 - R 연산 - 행 >= 열: 모든 행 정렬
 - C 연산 - 행 < 열: 모든 열 정렬 
2. 정렬하려면 각각의 수가 몇 번 나왔는지 알아야 함
3. 수의 등장 횟수가 커지는 순으로, 그런 수가 많으면 수가 커지는 순으로 정렬
4. 정렬된 결과를 다시 A에 넣기
 - 수와 등장 횟수를 모두 넣으며 순서는 수가 먼저
 - 다시 넣을 때 R 연산 적용: 가장 큰 행 기준으로 모든 행의 크기가 변함, C 연산은 반대
 - 행 또는 열의 크기가 커진 곳에는 0이 채워짐
 - 수를 정렬할 때 0은 무시해야 함
 - 크기가 100을 넘어가는 경우 100개를 제외한 나머지는 버림
@ 풀이
(1) 그냥 풀어보기
(2) zip을 사용해서 행을 열로 바꿔서 C 연산
"""


# R 연산 함수
def R(A):
    # 0 제거하기
    ZA = []
    for aa in A:
        naa = []
        for a in aa:
            if a != 0:
                naa.append(a)
        naa.sort()
        ZA.append(naa)
    A = ZA
    # 중복 숫자를 세며 가장 큰 길이 찾기
    max_length = 0
    NA = []
    for aa in A:
        duple = {}
        for a in aa:
            # 중복이 아니면 1
            if a not in duple:
                duple[a] = 1
            # 중복이면 +1
            else:
                duple[a] += 1
        naa = []
        # value로 정렬하기(100번만)
        cnt = 0
        for key, value in sorted(duple.items(), key=lambda x: x[1]):
            naa.append(key)
            naa.append(value)
            cnt += 2
            if cnt == 100:
                break
        NA.append(naa)
        # 가장 큰 길이 찾기
        if max_length < len(naa):
            max_length = len(naa)
    # 맥스길이와 비교하며 0을 붙이기
    for naa in NA:
        if len(naa) < max_length:
            for _ in range(max_length - len(naa)):
                naa.append(0)
    return NA


# C 연산 함수(행을 열로 바꾸고 R 연산 후 다시 행으로 바꾸기)
def C(A):
    # 행을 열로 바꾸기
    A = [list(r) for r in zip(*A)]
    # R 연산
    A = R(A)
    # 열을 다시 행으로 바꾸기
    A = [list(c) for c in zip(*A)]
    
    return A


# 행 r, 열 c, 목표 값 k
r, c, k = map(int, input().split())
# 배열 A
A = [list(map(int, input().split())) for _ in range(3)]
# 목표값 확인
# 인덱스에러가 날 경우 넘기기
if r - 1 >= len(A) or c - 1 >= len(A[0]):
    pass
elif A[r - 1][c - 1] == k:
    print(0)
    exit()

# 시간
time = 0
while time < 100:
    # 시간 카운트
    time += 1
    # 연산 판단하기
    # print(f'# 행 개수: {len(A)}')
    # print(f'# 열 개수: {len(A[0])}')
    # R 연산
    if len(A) >= len(A[0]):
        A = R(A)
    # C 연산
    else:
        A = C(A)
    # 인덱스에러가 날 경우 넘기기
    if r - 1 >= len(A) or c - 1 >= len(A[0]):
        continue
    # 목표값 확인
    if A[r - 1][c - 1] == k:
        print(time)
        exit()

# 시간 오버시
print(-1)