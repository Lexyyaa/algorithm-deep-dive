
## https://school.programmers.co.kr/learn/courses/30/lessons/431050

def solution(triangle):
    n = len(triangle)

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                # 맨 왼쪽은 바로 위 (i-1, 0)에서만 올 수 있음
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:
                # 맨 오른쪽은 바로 위 왼쪽 (i-1, j-1)에서만 올 수 있음
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                # 가운데는 위의 두 경로 중 더 큰 누적합을 선택
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    # 마지막 줄 중 최댓값이 꼭대기에서 바닥까지의 최대 합
    return max(triangle[-1])
