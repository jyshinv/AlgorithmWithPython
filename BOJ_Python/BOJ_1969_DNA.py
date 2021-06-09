'''
https://www.acmicpc.net/problem/1969
DNA

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	4114	2213	1877	56.844%
문제
DNA란 어떤 유전물질을 구성하는 분자이다.
이 DNA는 서로 다른 4가지의 뉴클레오티드로 이루어져 있다(Adenine, Thymine, Guanine, Cytosine).
우리는 어떤 DNA의 물질을 표현할 때,
이 DNA를 이루는 뉴클레오티드의 첫글자를 따서 표현한다.
만약에 Thymine-Adenine-Adenine-Cytosine-Thymine-Guanine-Cytosine-Cytosine-Guanine-Adenine-Thymine로
이루어진 DNA가 있다고 하면, “TAACTGCCGAT”로 표현할 수 있다.
그리고 Hamming Distance란 길이가 같은 두 DNA가 있을 때,
각 위치의 뉴클오티드 문자가 다른 것의 개수이다.
만약에 “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로 Hamming Distance는 2이다.

우리가 할 일은 다음과 같다.
N개의 길이 M인 DNA s1, s2, ..., sn가 주어져 있을 때
Hamming Distance의 합이 가장 작은 DNA s를 구하는 것이다.
즉, s와 s1의 Hamming Distance + s와 s2의
Hamming Distance + s와 s3의 Hamming Distance ... 의 합이 최소가 된다는 의미이다.

입력
첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다.
그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다.
N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력하고,
둘째 줄에는 그 Hamming Distance의 합을 출력하시오.
그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다.

예제 입력 1
5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT
예제 출력 1
TAAGATAC
7
예제 입력 2
4 10
ACGTACGTAC
CCGTACGTAG
GCGTACGTAT
TCGTACGTAA
예제 출력 2
ACGTACGTAA
6
예제 입력 3
6 10
ATGTTACCAT
AAGTTACGAT
AACAAAGCAA
AAGTTACCTT
AAGTTACCAA
TACTTACCAA
예제 출력 3
AAGTTACCAA
12
'''
import sys
import collections

input=sys.stdin.readline

#n과 m을 입력받는다.
n,m=map(int,input().split())

#DNA를 입력받는다.
dna=[list(input().rstrip()) for _ in range(n)]

#dna리스트의 행과 열을 바꾼다.
tdna=list(map(list,zip(*dna)))

#결과를 나타낼 빈 리스트 생성
result=[]
cnt=0
#입력받은 DNA의 첫번째 글자들 ~ 마지막 글자들로 비교하며 가장 많이 나온 알파벳을 추출한다.
for tdna in tdna :
    # -value로 오름차순(즉, value오름차순), 동점이면 key 오름차순,
    # 즉, 가장 많이 나온 순대로 정렬하되 동점이면 알파벳 순서대로 정렬한다.
    char=sorted(collections.Counter(tdna).items(),key=lambda x: (x[1], x[0]))
    print(char)
    #결과에 가장 많이 나온 알파벳 붙이기
    result.append(char[0][0])
    #가장 많이 나온 알파벳의 개수 더하기
    cnt+=char[0][1]



print(*result,sep='')
#전체 문자 개수에서 가장 많이 나온 알파벳의 개수의 총합을 뺀다.
print(n*m-cnt)
