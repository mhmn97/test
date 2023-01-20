import streamlit as st

st.text('Fixed width hiii')
st.markdown('# titr _Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.code('for i in range(8): foo()')

st.sidebar.radio('Select one:', [1, 2])
b = st.sidebar.slider('slider',0,100)
st.text(b)

#aks = st.camera_input("Take a picture",)

#st.image(aks)
