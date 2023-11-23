import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 개미
[출력: T초가 지난 후에 개미의 순서 출력]
1. 개미가 일렬로 이동할 때 가장 앞의 개미를 제외한 나머지 개미는 모두 앞에 개미 한 마리 존재
2. 두 그룹이 만났을 때 1초에 한번씩 개미는 서로를 점프함(뛰어넘기)
3. 자신의 앞에 반대 방향으로 움직이던 개미가 있는 경우에만 점프
4. 이동예시 
CBA> <DEF
CB> <D A> <EF
C> <D B> <E A> <F

CBADEF => CBDAEF => CDBEAF
5. 첫 번째 그룹 방향 >(오른쪽)
6. 두 번째 그룹 방향 <(왼쪽)
@ 풀이
(1) 그냥 풀기
"""


# 뛰어넘기 함수
def jump(G1, G2, word):
    time = 0
    # T초만큼 반복
    while time < T:
        flags = [[0] * (N1 + N2)]
        string = ''
        for w in range(N1 + N2 - 1):
            if word[w] in G1:
                if word[w + 1] in G2:
                    string += word[w + 1]
                    string += word[w]
                else:
                    string += word[w]
                    if w == N1 + N2 - 2:
                        string += word[w + 1]
            else:
                if word[w] not in string:
                    string += word[w]
                if w == N1 + N2 - 2:
                    string += word[w + 1]
        word = string
        time += 1
    #     print(f'time: {time}, string {string}')
    #
    # print(f'답: {word}')
    return word


# 첫번째 그룹 수 N1, 두번째 그룹 수 N2
N1, N2 = map(int, input().split())
# 첫번째 그룹
G1 = input().rstrip()
# 방향에 맞춰서 변경하기
word1 = ''
for g in G1:
    word1 = g + word1
# 두번째 그룹
G2 = input().rstrip()
# 두 그룹합친 문자열
word = word1 + G2
# 시간초 T
T = int(input())

print(jump(G1, G2, word))