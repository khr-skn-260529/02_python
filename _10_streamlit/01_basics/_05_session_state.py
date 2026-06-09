import streamlit as st
from traitlets.utils import descriptions

st.title('Session State')

description = """
- Streamlit은 버튼 클릭 등 사용자 상호 작용이 발생하면 스크립트(코드)를 위에서 아래로 다시 시작한다

- 그래서 일반 변수에 저장된 값들이 매번 초기화된다

- session_state를 이용하면 같은 사용자 안에서 값을 유지한다
  (사용자 기준 : 브라우저)
"""

st.markdown(description)

# Session : 서버에 접속한 사용자(클라이언트) 객체
# streamlit run -> 내 컴퓨터가 서버 컴퓨터
# 지금 작성하고 있는 코드가 서버 코드


# 버튼 클릭 횟수 카운트
count:int=0     # 초기값 : 0

#clicked = st.button('클릭 시 count 1 증가')
#clicked     # Streamlit Magic -> 화면 출력

if st.button('클릭 시 count 1 증가'):
    count += 1      #카운트 1 증가

st.write('클릭한 횟수: ', count)
# 버튼을 클릭 할 때마다 코드 재부팅 되기 때문에 여러번 눌러도 누적되지 않음
# 반복해서 버튼을 눌러도 False - True만 반복되어 count=1...

####################################################

st.subheader('session_state를 이용한 count', divider='rainbow')

# session_state
# - 서버 컴퓨터 메모리 영역에 접속한 사용자별 객체

# st.session_state에 count가 없으면 수행
# -> 최초 1회 접속 시에만 실행
if 'count' not in st.session_state:
    st.session_state['count'] = 0   # 초기화

if st.button("클릭 시 st.session_state['count'] 1 증가"):
    st.session_state['count'] += 1  # 카운트 1 증가

if st.button("클릭 시 st.session_state['count'] 1 감소"):
    st.session_state['count'] -= 1  # 카운트 1 감소

st.write('클릭한 횟수: ', st.session_state['count'])












