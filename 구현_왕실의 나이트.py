#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1]) #행은 1~8
col = ord(input_data[0]) +1 - ord('a')
#ord는 문자의 아스키코드 값을 알려준다. a=97

#나이트가 이동할 수 있는 8가지 방향을 정의하기
#복잡하게 생각하지 말고 2칸 1칸 +, - 조합으로 모든 경우의 수를 적어주면 된다.
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 체크
result=0
for step in steps :
    #이동하고자 하는 위치 확인
    next_row = row + step[0] #실수하지 말기!! steps의 요소가 step에 있음!
    next_col = col + step[1]

    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8 :
        result=result+1

print(result)

