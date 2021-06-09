'''
https://www.acmicpc.net/problem/10988
팰린드롬인지 확인하기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	10247	6841	5943	68.539%

문제
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

예제 입력 1
level
예제 출력 1
1
예제 입력 2
baekjoon
예제 출력 2
0
'''

import sys
input=sys.stdin.readline

#문자열을 입력받는다.
word=input().rstrip()

if word == word[::-1] :
    print(1)
else :
    print(0)

