## https://www.acmicpc.net/problem/3040


import sys

# 9명의 난쟁이 키를 입력받는다
heights = [int(sys.stdin.readline()) for _ in range(9)]

total = sum(heights)

# 7명의 합이 100이어야 하므로,
# 제외할 2명의 합은 (전체합 - 100)
target = total - 100

# 제외할 두 난쟁이의 "인덱스"를 저장할 변수
exclude_i, exclude_j = -1, -1

# 9명 중 서로 다른 2명을 골라 합이 target이 되는 쌍을 찾는다
# i < j 로 조합만 체크 (중복 방지)
for i in range(9):
    for j in range(i + 1, 9):
        # 이 두 명을 제외하면 나머지 7명의 합이 100이 됨
        if heights[i] + heights[j] == target:
            exclude_i, exclude_j = i, j
            break
    # 이미 찾았으면 바깥 루프도 탈출
    if exclude_i != -1:
        break

# 찾은 두 명을 제외하고 나머지 7명을 출력 (입력 순서 그대로)
for idx in range(9):
    if idx == exclude_i or idx == exclude_j:
        continue
    print(heights[idx])
