import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# a 를 모두 연속으로 만들기 위해 필요한 교환의 회수를 최소로 하는 프로그램 만들기
1. a 와 b 로만 이루어진 문자열이 주어짐
2. 이 문자열은 원형이기 때문에 처음과 끝은 서로 인접해 있음
@ 풀이
(1) 슬라이싱 윈도우 사용
(2) a의 개수만큼 슬라이싱할 윈도우 만들기
(3) 윈도우에 들어있는 b의 최소 개수 출력
"""

word = input().rstrip()

# 윈도우 만들기
window = 0
for w in word:
    if w == 'a':
        window += 1

# 교환해야할 b의 수
min_cnt = 1000
cnt = 0
# 윈도우만큼 슬라이싱하기
for i in range(len(word)):
    for j in range(window):
        # 인덱스를 넘어가지 않는다면 그대로 탐색
        if i + j < len(word):
            if word[i + j] == 'b':
                cnt += 1
        # 인덱스를 넘어간다면 순환하기 때문에 인덱스의 처음부터 다시 탐색
        else:
            reset = i + j - len(word)
            if word[reset] == 'b':
                cnt += 1
    # 가장 작은 횟수로 교체
    if min_cnt > cnt:
        min_cnt = cnt
    cnt = 0

print(min_cnt)