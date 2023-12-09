import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

#Fungsi memuat model dan vectorizer

def load_model_and_vectorizer():
    with open('model.pkl','rb') as model_file, open('vectorizer.pkl','rb') as vectorizer_file:
       model = pickle.load(model_file)
       vectorizer = pickle.load(vectorizer_file)  
    return model, vectorizer

def predict_sentiment(model,vectorizer,review):
    review_vectorized = vectorizer.transform([review])
    prediction = model.predict(review_vectorized)
    return prediction[0]

## Load Data
def load_data():
    data = pd.read_csv("20191002-reviews.csv")
    return data

def plot_word_cloud(data):
    text = " ".join(str(review) for review in data.reviewContent)
    wordcloud = WordCloud(background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt.gcf())

def show_desriptive_analysis(data):
    st.write('### Analsisis deskriptif')
    st.write(data.describe())
    plot_word_cloud(data)

def main() :

    st.title("Klasifikasi Sentimen Review Produk (Studi Kasus Lazada Dataset)")
    menu_options = {
     "Home" :":house:",
     "Dataset":":book:",
     "Model":":gear:",
     "Analisis Deskriptif":":bar_chart:",
     "Klasifikasi Sentiment" :":memo:",
     "About":":balloon:"
     }

    st.sidebar.title("Menu")
    choice = st.sidebar.radio("", list(menu_options.keys()), format_func=lambda x: f"{menu_options[x]} {x}")

    if choice == "Home":
        st.subheader("Home")
        st.write("Selamat datang di portofolio analisis review produk (dataset lazada)")
    elif choice =="Dataset":
        st.subheader("Dataset")
        st.write("Dataset yang digunakan")
        data = load_data()
        st.write(data.head(50))
    elif choice =="Model":
        st.subheader("Model")
        st.write("Model yang digunakan")
    elif choice =="Analisis Deskriptif":
        st.subheader("Analisis Deskriptif")
        st.write("Analisis Deskriptif ")
        data =load_data()
        show_desriptive_analysis(data)
    elif choice =="Klasifikasi Sentiment":
        st.subheader("Klasifikasi Sentiment")
        model, vectorizer = load_model_and_vectorizer()
        review_input = st.text_area('masukan review produk')
        if st.button('klasifikasi'):
            sentiment = predict_sentiment(model,vectorizer,review_input)
            st.write(f"Sentimen Prediksi: {sentiment}")
    elif choice =="About":
        st.subheader("About")
        st.write("About ")  


if __name__ == "__main__":
    main()