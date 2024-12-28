
import random

#p.26 디버깅 활용사례 살펴보기
#배열의 합 관련 코드


testcase = int(input())
answer = 0

A = [0]*(100001) # 값이 0인 요소 100001 개 생성하요 초기화


# 난수로 리스트 요소값 설정
for i in range(0,10001):
    A[i] = random.randrange(1,101) # 1<= <=100 의 난수 생성 하고, 이로 인덱스 10000 까지 초기화


#테스트 케이스 실행 - (지역변수) answer 의 값을 설정
for t in range(1,testcase+1):# 바깥에서 전역변수로 설정되어 계속 값이 add 만 되고, 0 으로 초기화가 안되서 testcase 마다 값이 누적되는 논리적 오류
    start, end = map(int,input().split()) #입력받은 문자열을 화이트스페이스 단위로 쪼갠 리스트의 각 요소를 int형으로 형변환 -> 시작과 끝 인덱스 받음

    for i in range(start, end+1):
        answer += A[i]

    print(str(testcase)+""+str(answer/2)) 