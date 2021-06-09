#행(ROW)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)] #[[],[],[]] 으로 만들어진다.

#노트 0에 연결된 노드 정보 저장(노드)
graph[0].append(1)
graph[0].append(2)

#노드 1에 연결된 노드 정보 저장(노드)
graph[1].append(0)

#노드 2에 연결된 노드 정보 저장(노드)
graph[2].append(0)

print(graph)

#결과 [[1, 2], [0], [0]]