#numeric - 정수, 실수, 복소수
#type(변수명 | 값) 함수 : 변수 또는 값의 타입을 확인하는 내장 함수

######
#정수 (int)
n=123

print(n, type(n))
#정수 자릿수 구분
price=1_000_000_000;
print(price, type(price))

#정수 최댓값
import sys
print(sys.maxsize, type(sys.maxsize))

#2진법, 8진법, 16진법
a=0b100 #==4
print(a, type(a))
b=0o23 #==3
print(b, type(b))
c=0xff
print(c, type(c))

######
#실수 (float)
f1=123.456
print(f1, type(f1))
f2=-999.999
print(f2, type(f2))
f3=1.0123456789012345678901234567890
print(f3, type(f3))
#소수점 16자리까지 표현 가능(근사치)


######
#복소수 (complex)
c=2j
print(c, type(c))
d=3+4j
print(d, type(d))

######
#산술연산 ( +, -, *, /, //(몫), %(modulo 나머지), **(거듭제곱) )
print(1+2) #3
print(1-2) #-1
print(1*2) #2
print(1/2) #0.5 -> 나누어 떨어질 때까지의 몫
print(1//2) #0 -> 정수 영역에서의 몫
print(1%2) #1 -> 정수 영역에서의 나머지
#거듭제곱
print(3**2) #9
print(3**3) #27
print(2**63) #int의 최대값