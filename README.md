# algorithm-deep-dive

- 12.03 링크드리스트
    - 개념정리([LinkedList.md](python%2Falgorithm%2Flinkedlist%2FLinkedList.md))
    - 요세푸스 문제 https://www.acmicpc.net/problem/1158 ([backjoon_1185.py](python%2Falgorithm%2Flinkedlist%2Fbackjoon_1185.py))

<!------------------------------------------------------
- 12.04 이진탐색
    - 개념
    - 문제1
    - 문제2
  ```
    링크드 리스트는 노드가 이어져있는 형태! 
  
  class Node : 
    def __init__(self, data):
      self.data = data
      self.next = None
  
  # 3이라는 값을 가지는 Node를 만드려면 
  node = Node(3) 
  
  링크드리스트라는 클래스를 한번 만들어볼거에요! 
  Linked는 head node만 딱 들고있습니다
  기차를 올려보면 맨 앞칸만 저장해놓는거에여!! 
  
  다음ㄴ ㅗ드를 보기위해서는 각 노드의 Next를 조회해서 찾아가야합니다 
  
  class LinkedList : 
    def __init__(self,value):
      self.head = Node(value) # head에 시작하는 Node를 연결합니다.
  
  linked_list = LinkedList(3) # 3이라는 값을 가지는 노드를 시작노드로 연결합니다.
  
  자 이제 
  append라는걸 만들면 
  
  class LinkedList : 
    def __init__(self,value):
      self.head = Node(value) # head에 시작하는 Node를 연결합니다.
  
    def append(self,value): # LInkedlist에 가장 끝에있는 노드에 새로운 노드를 연결합니다
        cur = self.head
        while cur.next : # 다음 노드가 있을때까지 계속 이동
            cur = cur.next
        cur.next = Node(value) # 마지막 노드에 새로운 노드를 연결합니다.
  
    def print_all(self) :
        cur = self.head
        while cur : # while cur is not None: 이라고 해도 되는구나! 
            print(cur.data)
            cur = cur.next
  
    def get_node(self,index): # index 번째의 노드를 찾아봅시다 
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
  
    def add_node(self,index,value) : # index 번째에 node를 추가해봅시다 
        # index-1번째 노드를 구해서 next를 현재노드로 해주고
        # index번째 노드를 구해서 현재노드의 next로 해주면 되는거잖아요? 
        # 하지만 여기서 주의할점!! index가 linked_list의 길이를 초과하면 안되고 
        # index-1 이 0보다 작으면 그냥 throw 하도록 해야함 
        if index < 1 or index > self.length() :
            raise IndexError("Index out of bounds")
        curr_node = Node(value)
        prev_node = get_node(index-1)
        next_node = get_node(index)
        prev_node.next = curr_node
        curr_node.next = next_node
       
    def delete_node(self,index) : # index 번째 노드를 삭제함당
        # 이전노드의 next를 그 그 다음노드로 해주면 되잖아요? 
        if index < 1 or index > self.length() :
            raise IndexError("Index out of bounds")
  
        prev_node = get_node(index-1)
        next_node = get_node(index+1)
        prev_node.next = next_node  
        # 앞 뒤를 이어주면 되는거잔하요? 
        
  
  
  ```
- 12.05 재귀함수
    - 개념
    - 문제1
    - 문제2
  
- 12.06 재귀함수,완전탐색 
    - 개념
    - 문제1
    - 문제2

- 12.07 프로그래머스 완전탐색,,, 
    - 개념
    - 문제1
    - 문제2

- 12.08 정렬
    - 개념
    - 문제1
    - 문제2
    - 강의 : 6 JVM
- 12.09 스택
    - 개념
    - 문제1
    - 문제2
    - 강의 : 7 JVM과 GC
- 12.10 큐
    - 개념
    - 문제1
    - 문제2
    - 강의 : 2 프로세서와 스레드 + 3 생성과실행
- 12.11 해쉬 
    - 개념
    - 문제1
    - 문제2
    - 강의 : 4,5 스레드생명주기
- 12.12 해쉬 
    - 개념
    - 문제1
    - 문제2
    - 강의 : 6 메모리가시성 7 동기화 synchronized
- 12.13 프로그래머스 해쉬
    - 개념
    - 문제1
    - 문제2

- 12.14 프로그래머스 큐 스택 
    - 개념
    - 문제1
    - 문제2
    - 강의 : 8 고급동기화 - concurrent.Lock
- 12.15 트리
    - 개념
    - 문제1
    - 문제2
    - 강의 : 
- 12.16 트리 
    - 개념
    - 문제1
    - 문제2
    - 강의 : 9+10 생산자, 소비자 문제 
- 12.17 힙
    - 개념
    - 문제1
    - 문제2
    - 강의 : 
- 12.18 힙 
    - 개념
    - 문제1
    - 문제2
    - 강의 : 11 CAS 동기화와 원자적 연산 
- 12.19 그래프 
    - 개념
    - 문제1
    - 문제2

- 12.20 그래프 
    - 개념
    - 문제1
    - 문제2
    - 강의 : 12 동시성 컬렉션

- 12.21 DFS
    - 개념
    - 문제1
    - 문제2
    - 강의 : 13 스레드풀과 Executor 프레임워크 
- 12.22 DFS
    - 개념
    - 문제1
    - 문제2
    - 강의 : 14 스레드풀과 Executor 프레임워크 
- 12.23 BFS
    - 개념
    - 문제1
    - 문제2
    - 강의 : 7 네트워크 기본이론 
- 12.24 BFS
    - 개념
    - 문제1
    - 문제2
    - 강의 : 8+9 네트워크 프로그램 
- 12.25 DP
    - 개념
    - 문제1
    - 문제2
    - 강의 : 10 세팅프로그램 11 HTTP 기본이론 12 HTTP 서버 만들기 
- 12.26 DP
    - 개념
    - 문제1
    - 문제2
    - 강의 : HTTP vs gRPC
- 12.27 라인코테
    - 개념
    - 문제1
    - 문제2
- 12.28 라인코테
    - 개념
    - 문제1
    - 문제2
    - 강의 : 13 리플렉션 
- 12.29 삼성역테 
    - 개념
    - 문제1
    - 문제2
    - 강의 : 14 애노테이션 
- 12.30 삼성역테
    - 개념
    - 문제1
    - 문제2
    - 강의 : 15 HTTP 서버 활용
- 12.31 카카오코테 
    - 개념
    - 문제1
    - 문제2
    - 개발 : 루퍼스 프로젝트 설계문서 현행화 + README 작성 + TODO 리스트 작성
- 01.01 카카오코테
    - 개념
    - 문제1
    - 문제2
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.02 프로그래머스 완탐 (7)
    - 개념
    - 문제1 https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit
    - 문제2
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.03 프로그래머스 정렬 (3) 
    - 개념
    - 문제1 https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit
    - 문제2
- 01.04 프로그래머스 DFS/BFS (7)
    - 개념
    - 문제1 https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit
    - 문제2
- 01.05 빈출유형 - 정렬
    - 문제1 https://www.acmicpc.net/problem/27488 
    두 정수를 조건에 맞게 나누는 문제
    - 문제2 https://school.programmers.co.kr/learn/courses/30/lessons/42747
    H-Index
    - https://www.acmicpc.net/problem/7578
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.06 빈출유형 - 그래프
    - https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=java
    - https://www.acmicpc.net/problem/17412
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.07 빈출유형 - DP
    - https://www.acmicpc.net/problem/2579
    - https://the-dev.tistory.com/89
    - https://kimchanjung.github.io/algorithm/2020/05/08/Coin-Change/
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.08 빈출유형 - 시뮬레이션
    - https://school.programmers.co.kr/learn/courses/30/lessons/12987
    - https://school.programmers.co.kr/learn/courses/30/lessons/49994
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.09 빈출유형 - 문자열처리 , 수학/기하학
    - https://school.programmers.co.kr/learn/courses/30/lessons/17677?language=cpp
    - https://school.programmers.co.kr/learn/courses/30/lessons/140107
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.10 빈출유형 - 구현
    - https://school.programmers.co.kr/learn/courses/30/lessons/131533
숫자 변환 규칙을 기반으로 최대값을 구하는 문제 (해당 문제는 비슷한 문제가 없어서 SQL 문제로 대체합니다)
    - https://school.programmers.co.kr/learn/courses/30/lessons/77484
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.11 빈출유형 - 기타알고리즘
    - 개념 https://www.acmicpc.net/problem/9346
    - 문제1 https://defacto-standard.tistory.com/1191
    - 문제2 https://www.acmicpc.net/problem/10819
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.12
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.13
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.14
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.15
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.16
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.17 
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.18 
    - 개발 : 이커머스플젝 소스정리 + 블로깅
- 01.19 
    - 사플 : 사플
- 01.20 
    - 사플 : 사플
- 01.21 
    - 사플 : 사플
- 01.22 
    - 사플 : 사플
- 01.23
    - 사플 : 사플
- 01.24 
    - 사플 : 사플
- 01.25 
    - 사플 : 사플
- 01.26 
    - 사플 : 사플
- 01.27
    - 사플 : 사플
- 01.28 
    - 사플 : 사플
- 01.29 
    - 사플 : 사플
- 01.30 
    - 사플 : 사플마무리!
- 01.31 
- 02.01 
    - 휴식~ 
- 02.02 
 - 출근이었으면~~
- 02.03 
- 02.04 
- 02.05 
- 02.06 
- 02.07 
- 02.08 
- 02.09 
- 02.10 
- 02.11 
- 02.12 
- 02.13 
- 02.14 
- 02.15 
- 02.16 
- 02.17 
- 02.18 
- 02.19 
- 02.20 
- 02.21 
- 02.22 
- 02.23 
- 02.24 
- 02.25 
- 02.26 
- 02.27 
- 02.28


이제 앞으로 해커랭크? 인가 암튼 영어사이트에서 1일 1코 고고~~

공부하면서 매일메일에 관련내용있으면 정리해서 개념쪽에 추가하기~~ 

-----------------------------------------------------> 