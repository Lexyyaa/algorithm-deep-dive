## https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []

    # 1차원으로 펼친 배열에서 i번째(0-index)의 값만 직접 계산한다.
    # i -> (r, c)로 바꾸면:
    #   r = i // n  (몇 번째 행인지)
    #   c = i % n   (그 행에서 몇 번째 열인지)
    #
    # 원래 2차원 배열 규칙:
    #   arr[r][c] = max(r+1, c+1)
    # 0-index로 계산하면:
    #   arr[r][c] = max(r, c) + 1
    for i in range(left, right + 1):
        r = i // n
        c = i % n
        answer.append(max(r, c) + 1)

    return answer
