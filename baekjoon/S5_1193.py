import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 1/1 # 1 (1)
# 1/2 2/1 # 2 (2, 3)
# 3/1 2/2 1/3 # 3 (4, 5, 6)
# 1/4 2/3 3/2 4/1 # 4 (7, 8, 9, 10)
# 5/1 4/2 3/3 2/4 1/5 # 5 (11, 12, 13, 14, 15)

# line을 구분

# line = 홀수 up 내림차순 / under 오름차순
# line = 짝수 up 오름차순 / under 내림차순

line = 1



# if line % 2 == 0:
    
# else:



# line = 1
# while T > line:
#     T -= line
#     line += 1

# if line % 2 == 0:
#     a = T
#     b = line - T + 1
# else:
#     a = line - T + 1
#     b = T

# print(a, '/', b)