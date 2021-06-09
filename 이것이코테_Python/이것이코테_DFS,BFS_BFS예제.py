from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited) :
    #큐 구현을 위해 deque라이브러리 사용
    queue=deque([start])
    #현재 노드를 방문 처리
    visited[start]=True
    #queue가 빌 때까지 반복
    while queue :
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i]=True

#각 노드가 연결된 정보를 리스트 자료형으로 표현한다(2차원)
graph=[
    [], #노드는 보통 1번부터 시작하니 비워두자.
    [2,3,8], #1번 노드
    [1,7], #2번 노드
    [1,4,5], #3번 노드
    [3,5], #4번 노드
    [3,4], #5번 노드
    [7], #6번 노드
    [2,6,8], #7번 노드
    [1,7] #8번 노드
]

#각 노드가 방문한 정보를 리스트 자료형으로 표현(1차원 리스트)
visited=[False]*9

#정의 된 BFS 함수 호출
bfs(graph, 1, visited)

'''
결과
1 2 3 8 7 4 5 6 
'''