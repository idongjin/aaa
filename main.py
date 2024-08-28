import streamlit as st
st.title('나의 첫 웹 서비스 만들기!!')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요:', ['망고빙수','아몬드봉봉'])
if st.button('인사말 생성') : 
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?! 저도 좋아요!!')
  
import streamlit as st

st.title('나의 첫 웹 서비스 만들기!!')

name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요:', ['망고빙수', '아몬드봉봉'])

blood_type = st.selectbox('혈액형을 선택해주세요:', ['A형', 'B형', 'O형', 'AB형'])

if st.button('인사말 생성'):
    personality = ''
    
    if blood_type == 'A형':
        personality = '신중하고 꼼꼼한 성격을 가지고 있네요.'
    elif blood_type == 'B형':
        personality = '자유롭고 개성 있는 성격을 가지고 있군요.'
    elif blood_type == 'O형':
        personality = '활발하고 사교적인 성격을 가지고 있네요.'
    elif blood_type == 'AB형':
        personality = '독특하고 창의적인 성격을 가지고 있군요.'

    st.write(f'{name}님! 당신이 좋아하는 음식은 {menu}이군요?! 저도 좋아요!!')
    st.write(f'그리고 {name}님은 {blood_type}, {personality}')

