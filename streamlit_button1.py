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
        independent_var = list(data.columns)
        return data, independent_var

# # buat fungsi untuk mengambil variablenya
# def ambil_var():
#     data = load_data()
#     independent_var = list(data.columns)
#     return independent_var
    
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
    
    # load nama variable
    if independent_var is not None:
        selected_var = st.multiselect("Pilih variabel bebas", independent_var)
        # tunjukkan variabel yang dipilih
        st.write("Anda telah memilih", selected_var)
    
    
    # simpan data ke Excel
    st.header("Simpan data ke Excel")
    save_data(data)

if __name__ == "__main__":
    main()

