import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 집합을 표현하는 프로그램 만들기
1. 초기에 n + 1 개의 집합 {0}, {1}, ... , {n} 이 존재
2. 여기에 합집합 연산과 두 원소가 같은 집합에 포함되어있는지를 확인하기
3. 합집합 예시: 0 a b
4. 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산: 1 a b
5. 1로 시작하는 입력에 대해서 a 와 b 가 같은 집합이라면 yes, 아니면 no 출력
@ 풀이
(1) 유니온-파인드로 풀기
(2) 재귀제한 해제
"""
sys.setrecursionlimit(10**9)

# find 함수
def find(x):
    if n_set[x] == x:
        return x
    # 경로 압축
    n_set[x] = find(n_set[x])
    return n_set[x]


# union 함수
def union(x, y):
    # 루트 노드 찾기
    x = find(x)
    y = find(y)
    if x > y:
        n_set[x] = y
    else:
        n_set[y] = x


# n, m(연산의 개수)
n, m = map(int, input().split())

# 정수의 집합 리스트
n_set = [i for i in range(n + 1)]

# 연산 입력받기
for j in range(m):
    c, a, b = map(int, input().split())

    # 합하기
    if c == 0:
        union(a, b)
    # 같은 집합인지 확인하기
    else:
        find_a = find(a)
        find_b = find(b)
        if find_a == find_b:
            print('YES')
        else:
            print('NO')