## https://school.programmers.co.kr/learn/courses/30/lessons/1844


from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 시작점이나 도착점이 벽이면 애초에 불가능
    if maps[0][0] == 0 or maps[n-1][m-1] == 0:
        return -1

    # 방문 여부 + 최단거리 기록용 배열
    # dist[r][c] = (0,0)에서 (r,c)까지의 최단 거리 (방문 전이면 0)
    dist = [[0] * m for _ in range(n)]

    # BFS를 위한 큐 (r, c)
    q = deque()

    # 시작점 초기화
    q.append((0, 0))
    dist[0][0] = 1
    # 문제에서 "칸 수"로 세므로 시작 칸을 1로 둠

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()

        # 현재 칸에서 4방향으로 이동 시도
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            # 1) 범위 밖이면 무시
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            # 2) 벽(0)이면 이동 불가
            if maps[nr][nc] == 0:
                continue

            # 3) 이미 방문한 칸이면(거리 기록이 있으면) 스킵
            if dist[nr][nc] != 0:
                continue

            # 여기까지 왔으면 "이동 가능 + 미방문" 칸
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    # BFS가 끝났는데 도착점 거리가 0이면 도달 못한 것
    return dist[n-1][m-1] if dist[n-1][m-1] != 0 else -1


