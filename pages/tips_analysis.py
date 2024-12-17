import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Функция для загрузки данных с кэшированием
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

st.title('Анализ данных о чаевых')
st.write('Это приложение позволяет визуализировать данные о чаевых из датасета tips.csv.')

# Шаг 1. Загрузка CSV файла
uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл с данными о чаевых', type='csv')

if uploaded_file is not None:
    tips_data = load_data(uploaded_file)
    st.write('Данные о чаевых:')
    st.write(tips_data.head())

    # График распределения чаевых
    st.subheader('Распределение чаевых')
    fig, ax = plt.subplots()
    sns.histplot(tips_data['total_bill'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    # График зависимости чаевых от дня недели
    st.subheader('Зависимость чаевых от дня недели')
    fig, ax = plt.subplots()
    sns.boxplot(x='day', y='total_bill', data=tips_data, ax=ax)
    st.pyplot(fig)

    # График зависимости чаевых от времени суток
    st.subheader('Зависимость чаевых от времени суток')
    fig, ax = plt.subplots()
    sns.boxplot(x='time', y='total_bill', data=tips_data, ax=ax)
    st.pyplot(fig)

    # Функционал скачивания графиков
    st.sidebar.header('Скачать графики')
    if st.sidebar.button('Скачать график распределения чаевых'):
        fig.savefig('histogram.png')
        with open('histogram.png', 'rb') as file:
            btn = st.download_button(
                label="Скачать график распределения чаевых",
                data=file,
                file_name="histogram.png",
                mime="image/png"
            )

    if st.sidebar.button('Скачать график зависимости чаевых от дня недели'):
        fig.savefig('boxplot_day.png')
        with open('boxplot_day.png', 'rb') as file:
            btn = st.download_button(
                label="Скачать график зависимости чаевых от дня недели",
                data=file,
                file_name="boxplot_day.png",
                mime="image/png"
            )

    if st.sidebar.button('Скачать график зависимости чаевых от времени суток'):
        fig.savefig('boxplot_time.png')
        with open('boxplot_time.png', 'rb') as file:
            btn = st.download_button(
                label="Скачать график зависимости чаевых от времени суток",
                data=file,
                file_name="boxplot_time.png",
                mime="image/png"
            )