## https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    # 방향 문자 -> (dx, dy)
    move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    x, y = 0, 0

    # 방문한 길 저장
    # 길은 방향이 없음(양방향 동일)
    edges = set()

    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy  # 다음 좌표

        # 좌표는 -5~5 밖으로 못 나감
        # 밖으로 나가는 이동은 무시 (현재 좌표 그대로)
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        # 현재점 a과 다음점 b 사이의 길을 기록함
        # (a,b)와 (b,a)를 같은 값으로 만들기 위해 정렬
        a = (x, y)
        b = (nx, ny)
        if a > b:
            a, b = b, a

        # set에 넣으면:
        # - 처음 지나간 길이면 새로 추가됨
        # - 이미 지나간 길이면 중복이라 변화 없음
        edges.add((a, b))

        # 실제 이동 반영
        x, y = nx, ny

    # set에 남은 간선 수 = 처음 지나간 길 수
    return len(edges)
