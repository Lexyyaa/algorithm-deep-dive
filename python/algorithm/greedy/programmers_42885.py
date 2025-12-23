
## https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    people.sort() ## 정렬을!!
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        # 가장 무거운 사람부터 처리
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람도 함께 태움
        right -= 1
        boats += 1  # 보트 1대 추가

    return boats
