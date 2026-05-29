#변수(variable): 값(literal)을 저장하는 메모리 상의 공간

#변수 선언 방법
# 변수명=값
a=10 #(a라는 공간에 10(literal)을 대입하라
b='홍길동'

print('a = ', a)
print('b = ', b)

#= : 대입연산자
#우항의 값을 좌항의 변수에 대입
num=100
print('num = ', num)
num="abcdefg"
print('num = ', num)
#변수는 저장된 값이 변할 수 있음

#대소문자를 구별함(snake case)
#teamname =/= Teamname
teamname='핼장이'
Teamname='혤쨩이'
print('teamname = ', teamname)
print('Teamname = ', Teamname)

#한글 변수명 지정 가능
팀명=3조
print(팀명)

#변수명은 숫자로 시작해서는 안됨
name_1="콩쥐"
#1_name='팥쥐'
_1_name=('신데렐라')

#언더바를 제외한 모든 특수문자 사용불가
#파이썬 예약어는 변수명으로 사용불가(if, for, while,...)

#파이썬 예약어 확인법
import keyword
print(keyword.kwlist)







