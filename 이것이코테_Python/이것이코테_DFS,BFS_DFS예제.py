#DFS 메소드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리한다.
    #처음에 v=1
    visited[v] = True
    print(v, end=' ')


    #현재 노드와 연결된 다른 노드를 재귀적으로 방문한다.
    for i in graph[v]: #i는 1부터시작 graph의 요소가 i가 된다.

        if not visited[i]: #visited[i]가 true가 아니라면 즉,false라면,
            #방문하지 않았을 경우에만 dfs()를 호출, 방문했을 경우에는 노드가 연결된 정보 다음정보로
            dfs(graph, i, visited)


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

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited=[False]*9 #visited=[False,False,False......]

#정의된 DFS함수를 호출
dfs(graph, 1, visited)
