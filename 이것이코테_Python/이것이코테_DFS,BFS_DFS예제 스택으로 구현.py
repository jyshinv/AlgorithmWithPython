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
stack=[]

#stack에 1 넣기
stack.append(1)
visited[1] = True
print(1,end=' ')

i=0
check=0
#stack이 채워져있다면 돌아라
while stack :
    check+=1
    #stack의 top이 현재 위치이다.
    cur=graph[stack[-1]][i]
    if not visited[cur]: #현재 위치에 연결된 노드를 하나씩 탐색하는데 방문하지 않았다면
        stack.append(cur) #stack에 더해주고
        print(cur,end=' ') #출력해준다.
        visited[cur] = True #방문처리를 해준다.
        i=0 #0으로 초기화
    else : #방문했다면
        i=i+1 #i를 1 증가해준다.
        if len(graph[stack[-1]]) == i :
            stack.pop()
            i=0 #0으로 초기화

print(check)