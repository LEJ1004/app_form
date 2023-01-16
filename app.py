import streamlit as st

st.title()
st.header()
st.subheader('회원가입 폼')

with st.form('my_form', clear_on_submit=True):
    st.success('다음 양식을 모두 입력후 제출합니다.')
    uid = st.text_input('아이디', max_chars=12)


