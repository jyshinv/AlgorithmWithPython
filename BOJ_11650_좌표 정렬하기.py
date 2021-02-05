import sys
input = sys.stdin.readline
#점의 개수 n을 입력받는다
n = int(input())

arr=[]
#i번점의 위치 x,y를 n번 튜플로 입력받아 리스트에 담는다.
for i in range(n) :
    x, y=map(int, input().split())
    arr.append((x,y))

#sorted함수를 이용해 각 튜플 0번째 기준으로 오름차순 정렬시킨다.
#각 튜플의 0번째 기준으로 오름차순하고 0번째 값이 같으면 1번째 값을 보고 오름차순 정렬시킨다.
arr=sorted(arr, key=lambda i: (i[0],i[1]))

#정렬이 수행된 결과를 출력한다.
for i in arr :
    print(i[0],i[1],sep=' ')