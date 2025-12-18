## https://school.programmers.co.kr/learn/courses/30/lessons/138476

"""
자 만약이걸 사람손으로 하면 어떻게 될까?
그럼 텐져린 리스트에서 하나씩꺼내서 1이 몇개고 2가 몇개고
그런걸 하겠지? 그러고 딕셔너리에 저장을 하겠지?

근데 이 문제에서 요구하는건 종류의 최소값이니까....
만약에 k가 4인데 사이즈가 1인 귤이 4개가 이미 니왔다면...
답은 1임

아 이거 그리디문제구나?
그렇다면.. 몇개가 있는지에 대해서 정렬을 한번 해줘야하는군!

그럼 사이즈가 다 다른 귤이 1개씩 있다면.. 그러면 좀 시간이랑 메모리 낭비가 좀 있겠구만..

시간복잡도 공간복잡도 확인해봅시다!


"""

def solution(k, tangerine):
    # 크기별 개수 세기
    counts = {}
    for size in tangerine:
        if size in counts:
            counts[size] += 1
        else:
            counts[size] = 1

    # 개수만 뽑아서 정렬
    freq_list = list(counts.values())
    freq_list.sort(reverse=True)

    # 큰 것부터 더해서 k개 이상 되는 순간까지!
    total = 0
    answer = 0

    for freq in freq_list:
        total += freq
        answer += 1
        if total >= k:
            break

    return answer