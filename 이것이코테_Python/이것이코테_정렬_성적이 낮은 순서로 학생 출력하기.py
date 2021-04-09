n=int(input())

#[(),(),()..] 이렇게 입력받을 수 있다.
arr=[]
for i in range(n) :
    data = input().split()
    arr.append((data[0], int(data[1])))


#arr내 튜블의 index 1번째 있는 요소로 오름차순 정렬 해준다.
arr = sorted(arr, key=lambda student:student[1])

#정렬이 수행된 결과를 출력한다.
for i in arr :
    print(i[0],end=' ')
