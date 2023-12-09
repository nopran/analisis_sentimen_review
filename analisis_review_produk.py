import streamlit as st


def main() :
    st.title("Klasifikasi Sentimen Review Produk (Studi Kasu Lazada Dataset)")
    menu_options = {
     "Home" :":house:",
     "Dataset":":book:",
     "Model":":gear:",
     "Analisis Deskriptif ":":bar_charts:",
     "About":":ballon:"
     }


    st.sidebar.title("Menu")
    choice = st.sidebar.radio("",list(menu_options,keys()),format_func=lambda x: f"{menu_options[x]}{x}")
