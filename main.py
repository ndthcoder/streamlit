import streamlit as st
import time

st.title("đây là bài 5")
st.write("đây là bài 5")
name = st.text_input("Nhập tên của bạn")
st.write("Chào", name)
if st.button("SSay Hello"):
    st.write("Hello")
    st.balloons()

prg = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    prg.progress(i+1)


