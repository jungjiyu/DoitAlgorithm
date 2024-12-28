#
# 문제 :
# 숫자의 합 구하기
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
#
# 풀이과정:
#
# 일단 공백 없다 -> split( ) 을 걍 쓰는건 아니다 -> split('')는?
#     : 구분자를 '' 로 해버리면 구분자 없다는 에러난다
#     Traceback (most recent call last):
#       File "C:\Backend\doitAlgorithm\ch03datastructure\baekjoon11720.py", line 15, in <module>
#         splitList=inputStr.split('')
#                   ^^^^^^^^^^^^^^^^^^
#     ValueError: empty separator
#
#
# try1 :그럼 input 문자열을 전체 int 형변환 한다음에 자릿수 단위로 끊는 로직 작성해야겠군 -> (input 값을 다 활용안했지만) 채점 성공 뜸
# try2 :그럼 input 값을 다 활용해야겠군 -> 문자열을 입력값 받은 만큼 리스트 인덱스로 접근하여 int 형변환처리해 계산 

##try1 : input 값 다 안 쓴 버전
trash = input()
inputStr = input()
inputInt = int(inputStr)
# print(f'inputInt : {inputInt}')


sum=0
num=inputInt

while(num != 0 ): # num%10 != 0 하면 안된다 :  num%10 != 0은 당장 첫번째 자리수가 0 이라는 것만 체크하는 거지, 이게 앞자리수들이 더 없는지를 체크하진 못한다.
#     print(f'num%10: {num%10}')
    sum +=num%10
    num//=10 # num/=10 하면 안된다! 소수점뒷부분있지만정수부한자리도없는수%10 하면 0.XXX로 소숫점 부분까지 더해진다
#     print(f'sum : {sum},num : {num}')
print(sum)


##try2 : input 값 다 사용했더니 잘 돌아감
count = int(input())
inputStr = input()
#print(f'count:{count}, inputStr : {inputStr}')


sum=0

for i in range(count):
    sum+=int(inputStr[i])
 #   print(sum)

print(sum)


##solution

##internetsol1



