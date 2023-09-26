import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N 개의 단어를 입력 받아 그룹 단어의 개수 출력
1. 그룹 단어: 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우
"""

# 단어의 개수 N
N = int(input())

# 단어 입력
cnt = 0
for _ in range(N):
    word = input().rstrip()

    # 단어 검사
    alphabet = []
    stop = False
    for w in range(1, len(word)):
        # 초항일 때만 0번째 인덱스 넣어주기
        if w == 1:
            alphabet.append(word[w - 1])
        # 이전 알파벳과 지금 알파벳이 다를 때
        if word[w - 1] != word[w]:
            # 지금 알파벳이 이미 나온적이 있다면 그룹 단어 X
            if word[w] in alphabet:
                stop = True
                break
            # 아니라면 append
            else:
                alphabet.append(word[w])
    # 그룹 단어가 아니라면 넘기기
    if stop:
        continue
    # 그룹 단어라면 cnt +1
    else:
        cnt += 1

print(cnt)

