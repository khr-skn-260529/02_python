#set(집합)
# 중복 허용X
# 순서 유지X
# 시퀀스 타입X
# 순회(iterable) 가능
# 집합 관련 메서드 제공

print('--- set ---')
st={2,3,4,1,2,3,1,3,1,2,4,4}
print(st) #{1, 2, 3, 4} -> 중복 제거됨

print('--- list->set 변경 (중복제거) ---')
lst=[3,2,1,3,3,1,2,3,3,4,2,4,2]
st2=set(lst) #set으로 변경
print('st2: ',st2)
# print(st2[2]) -> 에러 발생. set은 순서 존재X

#set->list 변환
lst2=list(st2)
print('lst2[2]: ',lst2[2])

print('--- tuple->set 변경 (중복제거) ---')
tpl=(3,2,1,3,3,1,2,3,4,2)
st3=set(tpl)
print('st3: ',st3)

#요소 추가(add)
print('--- 요소 추가(add) ---')
my_nums={20,30,40}
my_nums.add(10)
my_nums.add(10) #중복제거
my_nums.add(10) #중복제거
print('my_nums: ',my_nums)

#요소 제거(remove)
#제거하고 싶은 값을 명시해야함
print('--- 요소 제거(remove) ---')
my_nums.remove(10)
print('my_nums: ',my_nums)

#전체 제거(clear)
print('--- 전체 제거(clear) ---')
my_nums.clear()
print('clear 후 my_nums: ',my_nums)

#set 순회
print('--- set 순회 ---')
my_nums={30,50,70,90}
#my_nums에서 값을 하나 꺼내 num 변수에 저장(반복)
for num in my_nums:
    print(num)

#집합연산
print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합