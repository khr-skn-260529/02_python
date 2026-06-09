import streamlit as st
from pygments.styles import rainbow_dash

# 실행 명령어
# streamlit run [파일명].py

# streamlit 으로 텍스트 작성하기
# 페이지 제목
st.title('Hello, Streamlit!💩')

# 단락 제목
st.header('header')
# 단락 부제목
st.subheader('subheader',divider=True)
st.subheader(':green[색 지정 가능] subheader',divider='rainbow')

# 내용 작성
# text: 단순 글자
st.text('text test!!!')

# write: 단순 글자 뿐만 아니라
#        마크다운, 표, 리스트, 차트, 입력 타입 들에 따라 출력 방식이 정해짐
st.write('write test!!!')
st.write('write **markdown** 지원')
st.write("`code block`")

# markdown
st.markdown('### markdown')

#html
st.html('<h3><mark>html</mark>도 지원<h3>')

st.subheader(':red[magic]',divider='orange')

'streamlit magic'
'변수나 리터럴 값이 출력 구문 내에 없어도 화면에 값을 기록하는 기능'
100
lst=[10,20,30]
lst
dct={'a':100,'b':200}
dct

# code block
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python",line_numbers=True)

# latex : 수식
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# badge
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

# metric
st.subheader(':blue[metic]', divider='blue')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# columns(): 컬럼 분할
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")





