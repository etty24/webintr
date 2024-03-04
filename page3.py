import streamlit as st
def page_3():
    st.title("Halamat 3")
    st.write('Menampilkan Halaman Dari file MD (MarkDown)')

    with open ('data.md' , 'r') as file:
        isi_teks = file.read()
        st.markdown(isi_teks)