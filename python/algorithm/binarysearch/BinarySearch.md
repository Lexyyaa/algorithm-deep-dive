# 이진탐색
 - 이진탐색의 시간복잡도는 Olog(n)이다.
 - 순자탐색의 시간복잡도는 O(n)이다.
 - 정렬된 배열에서 특정한 값을 찾을 때 사용된다.
 - 탐색 범위를 절반씩 좁혀가며 값을 찾는다.
 - 탐색 대상이 정렬되어 있어야 한다.
 - 재귀적 방법과 반복적 방법으로 구현할 수 있다.
 - 중간 인덱스를 계산하여 탐색 범위를 조정한다.
 - Python에서 list에 특정 원소가 있는지 판별하는 함수는 'in' 키워드를 사용한다.
 - python 에서 in 키워드는 시간복잡도가 O(n)이다.

### 이진탐색 예제코드 

```python

    finding_target = 14
    finding_numbers = [n for n in range(1, 21)]  # 1부터 20까지의 숫자 리스트 생성
    
    def binary_search(target,array) : 
        curr_min = 0 # 최솟값 
        curr_max = len(array) - 1 # 최대값 
        mid_idx = curr_max + curr_min // 2  # 중간값 
        
        find_cnt = 0 # 탐색 횟수 
        
        while curr_min <= curr_max : 
            find_cnt += 1  # 탐색 횟수 증가
            if array[mid_idx] == target : 
                return True;
            elif array[mid_idx] < target :
                curr_min = mid_idx + 1 
            else :
                curr_max = mid_idx - 1
            mid_idx = (curr_max + curr_min) // 2
        
        return False;
    
    ## 만약에 start, end 를 인자로 받는다면 
    
    def binary_search(target,array,start,end) : 
        find_cnt = 0 # 탐색 횟수 
        
        while start <= end : 
            find_cnt += 1  # 탐색 횟수 증가
            mid_idx = (start + end) // 2  # 중간값 
            if array[mid_idx] == target :
                return array[mid_idx]
            elif array[mid_idx] < target :
                start = mid_idx + 1 
            else :
                end = mid_idx - 1
        
        return None
```