#A, B는 피보나치 수열을 따른다. 개수만을 세어보자
k = int(input())

#k+1크기의 리스트 생성
d = [0] * (k + 1)
#d[0] = 0, d[1] = 1
d[1] = 1

#d[2]부터 계산
for i in range(2, k+1):
    d[i] = d[i-1] + d[i-2]

print(d[k-1], d[k])