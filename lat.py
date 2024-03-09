import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from kalkulatorsegitiga import kalkulatorsegitiga
from image1 import main

#import matplotlib.pyplot as plt

#st.write("coding club 2024 ")
#df = pd.DataFrame({
#   'No':[1,2,3,4],
#    'Nama' :['ety','kia','pute','anita'],
#    'nilai':[91,89,80,100]

#})

#df
PAGES = {
     "page 1" : page_1,
     "Page 2" : page_2,
     "Page 3" : page_3,
     "page 4" : kalkulatorsegitiga,
     "konverensi foto" : main,
}
st.sidebar.image("upin ipin.jpg", width = 200)
page = st.sidebar.radio("halaman", list(PAGES.keys()))
PAGES[page]()