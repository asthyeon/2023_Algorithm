import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    word = input().rstrip()

    if word == '0':
        break

    start = 0
    end = len(word) - 1
    for w in range(len(word) // 2):
        if word[start] != word[end]:
            print('no')
            break
        start += 1
        end -= 1
    else:
        print('yes')