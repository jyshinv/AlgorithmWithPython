import sys
n=int(sys.stdin.readline())

#data에서 가장 큰 수만큼 방을 만들고 0으로 초기화해준다.
arr=[0]*10001
for _ in range(n) :
    data = int(sys.stdin.readline())
    arr[data] += 1
    #arr[int(sys.stdin.readline())] += 1 위의 두 줄은 한줄로 줄일 수 있다.

#arr에 저장된 수만큼 값을 출력한다.
for i in range(10001) :
    if arr[i] != 0:
        for _ in range(arr[i]) :
            print(i)



