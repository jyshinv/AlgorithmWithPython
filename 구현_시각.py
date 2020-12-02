#n을 입력받는다
n = int(input())

#n이 5라면 00시 00분 00초 ~ 05시 59분 59초 까지 검사

count = 0
for i in range(n+1) :
    for j in range(60) :
        for k in range(60) :
            #매 시각 안에 '3'이 포함되어 있다면 카운트 증가.
            #3:5:25라면 '3525'중 3이 포함되어 있으므로 count증가
            if '3' in str(i)+str(j)+str(k) :
                count = count+1

print(count)




