'''
https://www.acmicpc.net/problem/11000

강의실 배정

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	9806	2924	2067	29.174%
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다.

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데,
최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다.
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (1 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.

예제 입력 1
3
1 3
2 4
3 5
예제 출력 1
2
'''
import sys
input=sys.stdin.readline

#n을 입력받는다
n=int(input())

#for문에서 필요한 리스트 선언 및 초기화
meeting=[0]*(n*2)
#for문에서 필요한 변수 선언 및 초기화
i=0
#입력받음과 동시에 meeting리스트에 값 넣기
for start, end in [list(map(int,input().split())) for _ in range(n)] :
    meeting[i] = [start,1] #시작시간과 1 담기
    meeting[i+1] = [end,-1] #종료시간과 -1 담기
    i+=2

#수업시작시간 기준, 동일하다면 수업종료시간을 기준으로 정렬한다.
meeting.sort(key=lambda x:(x[0],x[1]))

cnt,result=0,0
for _,num in meeting :
    cnt+=num
    #최댓값을 갱신
    result=max(result, cnt)

print(result)


