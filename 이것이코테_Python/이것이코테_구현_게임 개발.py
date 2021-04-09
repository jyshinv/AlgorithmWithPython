#n,m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화하기,2차원 리스트
d = [[0]*m for _ in range(n)] #n*m 행렬만들고 0으로 채워넣기 방문안함:0,방문함:1

#현재 캐릭터의 x,y 좌표와 방향을 입력받기
x, y, direction = map(int, input().split())

#2차원 리스트인 d에 현재 위치 방문처리하기
d[x][y] = 1

#전체 맵 정보를 입력받기
#빈 리스트를 만들기
array = []
for i in range(n):
    # 이런식으로 array.append()하면
    # [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
    # 로 2차원 배열이 만들어 질것임!!
    array.append(list(map(int, input().split())))


#북, 동, 남, 서에 따른 방향크기를 정의한다.
#북은 위쪽, 동은 오른쪽, 남은 아래쪽, 서는 왼쪽임
#(행x, 열y)의 이동에 따른 증감을 생각해보자!
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    #함수 안에서 전역변수의 값을 변경하려면 global 키워드를 써야한다.
    #global 키워드를 쓰지 않으면 direction은
    #turn_left 함수의 지역변수가 되어버린다.
    global direction
    direction -=1
    if direction == -1 :
        direction = 3
    #direction은 북 0 ,동 1,남 2,서 3
    #동,서,남,북 왼쪽으로 회전할 수록 수가 작아짐!
    #단, 북쪽에서 왼쪽으로 turn 하면 -1이 되므로 그때만 서쪽인 3으로 고정해주기


#시뮬레이션 시작
count =1 #시작지점은 count하고 시작
turn_time = 0
while True :
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하면서 땅인 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1 #방문처리
        x, y = nx, ny #실제로 이동
        count+=1 #카운트 증가
        turn_time=0 #turn_time은 다시 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else :
        #증가시키고 아래 if문에서 걸리지 않는다면
        #무한루프 이므로 맨위로 돌아가서 turn_left()부터 수행한다.
        turn_time +=1 #turn_time을 증가시키기
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4 :
        #바라보는 방향 그대로 하고 뒤로 한칸 가기
        nx = x-dx[direction] #바라보는 방향 반대이므로 부호 바꾸고 더해주면 된다.
        ny = y-dy[direction]
        #뒤로 갈 수 있다면 이동하기, 땅이라면 이동가능
        if array[nx][ny] == 0 :
            x,y = nx, ny
        #뒤가 바다로 막혀있다면 움직임을 멈춘다.
        else :
            #반복문을 빠져나간다.
            break
        #뒤로 갈 수 있다면 이동 후 turn_time을 초기화 해주어야한다.
        turn_time=0

#count 출력
print(count)


