# https://www.acmicpc.net/problem/10815

import sys
N = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))

# card_list = [6, 3, 2, 10, -10]
# number_list = [10, 9, -5, 2, 3, 4, 5, -10]

result_list = []

# for num in number_list :
#     if num in card_list :
#         result_list.append(1)
#     else :
#         result_list.append(0)
#
# print(" ".join(map(str, result_list)))

# 이렇게하면 시간 초과 나옴 왜? 순차탐색하기 때문
# 저 IN 연산이 O(N) 이기 때문
# 그렇다면 이걸 이분탐색하는 코드로 바꿔보자

card_list.sort() # 이분탐색은 정렬이 되어 있어야 함!!

for num in number_list :
    curr_min_idx = 0
    curr_max_idx = N - 1
    mid_idx = (curr_min_idx + curr_max_idx) // 2

    while curr_min_idx <= curr_max_idx :
        if card_list[mid_idx] == num :
            result_list.append(1)
            break
        elif card_list[mid_idx] < num :
            curr_min_idx = mid_idx + 1
        else :
            curr_max_idx = mid_idx - 1
        mid_idx = (curr_min_idx + curr_max_idx) // 2
    else : # while 문이 break 로 종료되지 않고 끝까지 도달했을 때
        result_list.append(0)

print(" ".join(map(str, result_list)))