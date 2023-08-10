import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 부분문자열 구하기
1. set 를 이용해서 중복 제거하기
2. 인덱싱을 이용하기
3. readline을 쓰면 오답으로 나옴
'''

# 문자열 string
string = input()

# 중복이 없는 집합 만들기
subset = set()

'''
# 예시 ababc 의 부분집합 인덱싱 목록
[0:1] [1:2] [2:3] [3:4] [4:5]

[0:2] [1:3] [2:4] [3:5]

[0:3] [1:4] [2:5]

[0:4] [1:5]

[0:5]
'''

# 전체 인덱싱을 슬라이싱으로 구하기
# (set에 넣으므로 중복 자동 제거)
for i in range(len(string)):
    for j in range(i, len(string)):
        subset.add(string[i:j + 1])

print(len(subset))