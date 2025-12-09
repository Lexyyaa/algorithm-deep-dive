## https://school.programmers.co.kr/learn/courses/30/lessons/86971
## 전력망을 둘로나누기

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# result = 3

# n = 4
# wires = [[1,2],[2,3],[3,4]]
# ## result = 0

# n = 7
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
# ## result = 1

# 우선 배열을 오름차순으로 정렬함
# wires.sort(key=lambda x: (x[0], x[1]))
# 아 그럴필요가 없구나? 1 ≤ v1 < v2 ≤ n 입니다. 라는 조건이 있네

def count_nodes(node_num, removed_wire, visited, wires) :
    visited.add(node_num)
    count = 1

    for v1, v2 in wires :
        if [v1,v2] == removed_wire :
            continue
        if v1 == node_num and v2 not in visited:
            count += count_nodes(v2, removed_wire, visited, wires)
        elif v2 == node_num and v1 not in visited:
            count += count_nodes(v1, removed_wire, visited, wires)
    return count


def solution(n, wires):
    answer = None

    for removed_wire in wires:
        visited = set()

        v1, v2 = removed_wire

        cnt = count_nodes(v1, removed_wire, visited, wires)
        diff = abs(n - 2 * cnt)

        if answer is None or diff < answer:
            answer = diff

    return answer