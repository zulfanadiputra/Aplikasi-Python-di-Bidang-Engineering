# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:43:44 2023

@author: User
"""

import streamlit as st
import pandas as pd

# buat fungsi untuk load data
def load_data():
    file = st.file_uploader("Upload file Excel", type=["xlsx"])
    if file is not None:
        data = pd.read_excel(file, engine='openpyxl')
        return data
    
# buat fungsi untuk menyimpan data
def save_data(data):
    file = st.text_input("Masukkan nama file untuk disimpan", "data.xlsx")
    if st.button("Simpan ke Excel"):
        data.to_excel(file, index=False)
        st.success("Data disimpan dengan sukses")

# buat fungsi utama untuk streamlitnya
def main():
    st.title("Memasukkan dan menyimpan data melalui Excel")
    
    # load data dari Excel
    st.header("Load data dari Excel")
    data = load_data()
    if data is not None:
        st.write(data.head())
    
    # simpan data ke Excel
    st.header("Simpan data ke Excel")
    save_data(data)

if __name__ == "__main__":
    main()

