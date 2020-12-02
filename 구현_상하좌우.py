'''
입력받기 예제(파이썬)
-두 수를 공백으로 입력받기
n, m = map(int, input().split())
-여러 수를 공백 기준으로 입력받아 리스트로 변환
data = list(map(int, input().split()))
-여러 문자를 공백 기준으로 입력받아 리스트로 반환
plans=input().split()
'''

#n을 입력받는다
n = int(input())

#시작지점
x, y = 1, 1

#plans를 입력받는다.
plans= input().split() #split()은 공백을 기준으로 분리하여 '리스트'로 반환]

#움직임 타입
move_types=['L', 'R', 'U', 'D']

#L, R, U, D 방향에 따른 각 지점의 좌표의 이동방향 (x,y)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


#이동 계획을 하나씩 확인
for plan in plans : #plans는 ex) R R R U D D
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        # plan 한개를 move_types 요소 모두와 비교해서 같으면
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]

    #nx와 ny가 범위를 넘었는 지 넘지 않았는 지 검사
    if nx<1 or ny<1 or nx>n or ny>n :
        continue

    #위에서 넘지 않았는 지 검사해서 넘지 않았으면 실제로 이동
    x, y = nx, ny

print(x,y)









