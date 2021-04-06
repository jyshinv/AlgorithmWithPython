'''
https://www.acmicpc.net/problem/10828
스택

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	97880	37340	26970	38.764%

문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
예제 출력 1
2
2
0
2
1
-1
0
1
-1
0
3
예제 입력 2
7
pop
top
push 123
top
pop
top
pop
예제 출력 2
-1
-1
123
123
-1
-1
'''
#파이썬에서 False 대체 0, True는 0빼고 나머지 수
import sys
input=sys.stdin.readline

#스택이 비어있는 지 검사하는 함수(비어있다면 True를 반환한다.)
def isEmpty(stack) :
    if not stack :
        return True
    else :
        return False

#test case 개수 입력받기
tc = int(input())

#stack으로 사용할 빈 list만들기
stack = []

#명령어와 숫자 입력받기
for _ in range(tc) :
    cmd = input().split() #push 1 입력 시 cmd=['push', '1']

    if cmd[0] == 'push' :
        #스택에 값을 대입한다.
        stack.append(cmd[1])
    elif cmd[0] == 'pop' :
        #isEmpty가 true이면 -1을 출력 그렇지 않으면 pop한 후 pop한 값을 출력
        print(-1) if isEmpty(stack) else print(stack.pop())
    elif cmd[0] == 'top' :
        # isEmpty가 true이면 -1을 출력 그렇지 않으면 리스트의 가장 끝 인덱스 값 출력
        print(-1) if isEmpty(stack) else print(stack[-1])
    elif cmd[0] == 'size' :
        #스택(리스트)의 사이즈를 반환
        print(len(stack))
    elif cmd[0] == 'empty' :
        # isEmpty가 true이면 1을 출력 그렇지 않으면 0을 출력
        print(1) if isEmpty(stack) else print(0)


