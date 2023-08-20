import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 단어 정렬
1. 길이가 짧은 것부터
2. 같으면 사전 순
3. 중복된 단어는 하나만 남기고 제거
'''

# 단어의 개수
N = int(input())

# 단어 입력
words = []
for _ in range(N):
    words.append(input().rstrip())

# 사전순 정렬
words.sort()

# 버블정렬
for i in range(N - 1, 0, -1):
    for j in range(i):
        # 단어 길이 순으로 정렬
        if len(words[j]) > len(words[j + 1]):
            words[j], words[j + 1] = words[j + 1], words[j]

# 중복 단어 제거
stack = []
for word in words:
    if word not in stack:
        stack.append(word)

# 출력
for o in range(len(stack)):
    print(stack[o])