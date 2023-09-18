import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 길이가 M 이상인 단어들만 외우기
1. 단어장의 단어 순서는 다음과 같은 우선순위를 차례로 적용
 ㄱ. 자주 나오는 단어일수록 앞에 배치
 ㄴ. 해당 단어의 길이가 길수록 앞에 배치
 ㄷ. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
"""

# 단어의 개수 N, 외울 단어의 길이 기준 M
N, M = map(int, input().split())

# 단어 받기
words = []
for _ in range(N):
    word = input().rstrip()
    
    if len(word) >= M:
        words.append(word)

# 자주나오는 단어 확인
words_dict = {}
for w in words:
    if w not in words_dict:
        words_dict[w] = 1
    else:
        words_dict[w] += 1
# 내림차순 정렬(빈도순)
w_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)

# 빈도, 어길이, 알파벳순으로 리스트를 만들어서 정렬하기
result = []
# 빈도에 대한 인덱스 조정
idx = 0
if len(w_dict) >= 2:
    for i in range(1, len(w_dict)):
        # 이전 수보다 현재 수가 빈도가 더 작다면
        if w_dict[i - 1][1] > w_dict[i][1]:
            # 빈도가 같은게 없다면
            if idx == 0:
                li = [i, len(w_dict[i - 1][0]), w_dict[i - 1][0]]
                result.append(li)
            # 빈도가 같은게 있다면
            else:
                li = [i - idx, len(w_dict[i - 1][0]), w_dict[i - 1][0]]
                result.append(li)
                idx = 0
            # 마지막 값이라면 i + 1 순서로 저장
            if i == len(w_dict) - 1:
                li = [i + 1, len(w_dict[i][0]), w_dict[i][0]]
                result.append(li)
        # 이전 수와 현재 수가 빈도가 같다면
        else:
            li = [i - idx, len(w_dict[i - 1][0]), w_dict[i - 1][0]]
            result.append(li)
            # 마지막 값이라면 i 순서로 저장
            if i == len(w_dict) - 1:
                li = [i - idx, len(w_dict[i][0]), w_dict[i][0]]
                result.append(li)
            idx += 1
    # 정렬(빈도순 - 단어길이순)
    result.sort()

    # 단어 길이에 대한 인덱스 조정
    idx2 = 1
    for k in range(len(w_dict) - 2, -1, -1):
        # 빈도 수가 같다면
        if result[k + 1][0] == result[k][0]:
            # 이전 단어길이가 현재 단어길이보다 길다면
            if result[k + 1][1] > result[k][1]:
                result[k + 1][1] = idx2
                idx2 += 1
            # 이전 단어길이와 현재 단어길이가 같다면
            else:
                result[k + 1][1] = idx2
            # 마지막 순서라면
            if k == 0:
                result[k][1] = idx2
        # 빈도 수가 다른것이 나온다면 이전 것은 그대로 넣고 초기화
        else:
            result[k + 1][1] = idx2
            idx2 = 1
            # 마지막 순서라면
            if k == 0:
                result[k][1] = idx2

    # 정렬
    result.sort()

    for r in result:
        print(r[2])
else:
    print(w_dict[0][0])





