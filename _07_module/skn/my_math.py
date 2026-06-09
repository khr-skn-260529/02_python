#사용자 모듈

if __name__ == '__main__':
    print('my_math.py를 직접 실행하셨군요...')
    pass
else:
    print('다른 py 파일에 my_math.py가 import 되었습니다.')
    print('*'*100)
    print('*'*100)


pi:float=3.14

x:int=20

def get_circle_area(r:float)->float:
    return pi*r*r

#private 변수 설정
# - private 설정이 강제되진 않음
# - 대신 외부에서 직접 사용하는 것을 권장하지 않음
# - import * 에서는 자동 제외됨
__z:str='hello'