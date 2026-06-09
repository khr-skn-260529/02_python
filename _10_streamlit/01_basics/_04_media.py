from email.mime import image

import streamlit as st

st.title('Media - image')

#서버 이미지
st.image('../data/똥꼬푸린.jpeg',caption='똥꼬푸린이와 똥꼬친구들')

#웹 이미지
image_url= 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA5MTZfMjM5%2FMDAxNjYzMjU4OTkwMzM0._mBoTB1Q_AAhsg5cZK001r7r_2KdJxOUNV22IC8wTbMg.3eHDadmiKWY6cC7-nAbwSC93u5feDhFTCC2BPcR2VBUg.JPEG.yr051205%2FIMG_8627.JPG&type=sc960_832'
st.image(image_url, caption='웹이미지')