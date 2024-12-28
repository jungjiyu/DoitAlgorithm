#
# 문제 :
# 평균 구하기
# 새로운 평균을 구하는 프로그램을 작성하시오.
#
# 풀이과정:
# 일단 시험 본 과목수 입력 받기
# 일단 원본 성적을 띄어쓰기 기준으로 구분하여 입력받기 -> split( )  사용
# 최댓값 구하기 -> max( 리스트 ) 활용
# 모든 점수에 변형 가하기 -> 인자값/앞서구한최댓값*100 을 내용으로하는 함수 def 후 map( 해당함수 , 리스트 )
# 변형된 점수들의 최솟값 구하기 -> sum(리스트)/과목수

##try1 :
count = int(input())
originList = list(map(int, input().split()))
#print(f'count:{count}, originList:{originList}')
maxScore = max(originList)
#print(f'maxScore:{maxScore}')

def foo(a):
    return a/maxScore*100

manipulatedList = list(map(foo,originList))
#print(f'manipulatedList:{manipulatedList}')
print(sum(manipulatedList)/count)

