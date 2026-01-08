## https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import OrderedDict

def solution(cacheSize, cities):
    # 캐시 크기가 0이면, 어떤 도시를 와도 무조건 miss
    if cacheSize == 0:
        return 5 * len(cities)

    cache = OrderedDict()  # key: city(lower), value는 의미 없어서 1로 둠
    time = 0

    for city in cities:
        city = city.lower()  # 대소문자 무시 규칙

        if city in cache:
            # cache hit: +1
            time += 1

            # LRU 갱신 - 해당 키를 가장 최근 사용 위치로 이동
            cache.move_to_end(city)

        else:
            # cache miss: +5
            time += 5

            # 캐시가 꽉 찼으면 가장 오래된 것 제거
            if len(cache) == cacheSize:
                cache.popitem(last=False)  # 앞쪽이 가장 오래된 항목

            # 새 항목을 가장 최근 사용으로 추가
            cache[city] = 1

    return time
