# 링크드리스트 (Linked List)


## 링크드리스트와 어레이리스트 비교
    - 링크드리스트는 노드들이 포인터로 이어져있는 형태
    - 어레이리스트는 메모리상에 연속적으로 붙어있는 형태
    - 링크드리스트는 삽입, 삭제가 용이하지만 탐색이 느림
    - 어레이리스트는 탐색이 빠르지만 삽입, 삭제가 느림
    - 링크드리스트는 메모리 낭비가 심함 (포인터 저장공간때문에)
    - 어레이리스트는 메모리 낭비가 적음
    - 링크드리스트는 캐시 적중률이 낮음 (메모리 위치가 불규칙적이기때문에)
    - python에서의 list 자료구조는 어레이리스트 기반이지만 링크드리스트적 특성도 일부 가지고 있음 (예: deque)
    - python에서 list를 통해 linkedlist를 구현하려면 collections 모듈의 deque를 사용하는 것이 좋음
    - deque의 사용방법은 다음과 같음

```python
    from collections import deque
    
    linked_list = deque()
    
    # 노드 추가
    linked_list.append(1)  # 맨 뒤에 추가
    linked_list.appendleft(0)  # 맨 앞에 추가
    
    # 노드 삭제
    linked_list.pop()  # 맨 뒤에서 삭제
    linked_list.popleft()  # 맨 앞에서 삭제
    
    # 노드 접근
    first_node = linked_list[0]  # 첫 번째 노드 접근
    second_node = linked_list[1]  # 두 번째 노드 접근`
```   
  - 이러한 deque를 이용하여 stack과 queue도 쉽게 구현할 수 있음
  - stack은 append와 pop을 사용하여 구현 가능하며, queue는 append와 popleft를 사용하여 구현 가능함
  - length를 구하고싶다면 len(linked_list)로 구할 수 있음
  - 특정 인덱스의 원소를 추가하고싶다면 insert(index, value)를 사용하면 됨
  - 특정 인덱스의 원소를 삭제하고싶다면 del linked_list[index]를 사용하면 됨
