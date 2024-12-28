def funcA(a,b,c):
    return a+1,b+1,c+1 # 콤마로 여러개 값 반환하는 것 처럼 구현

resultA = funcA(1,2,3) # 튜플 하나의 형태로 반환된다
print(resultA) 

resulta,resultb, resultc = funcA(1,2,3) # 여러 변수로 나눠 받게 하면 자동언패킹된다
print(f'resulta,resultb, resultc : {resulta}, {resultb}, {resultc}')
