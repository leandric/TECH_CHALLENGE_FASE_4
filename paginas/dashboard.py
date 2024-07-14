import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_fake_data():
    np.random.seed(42)
    dates = pd.date_range(start='2020-01-01', periods=365)
    prices = np.random.normal(50, 10, size=len(dates)).round(2)
    return pd.DataFrame({'Date': dates, 'Price': prices})

def show():
    st.title("Dashboard do Preço do Barril de Petróleo")
    st.write("Este é um dashboard com dados fictícios sobre o preço do barril de petróleo. Substitua esses dados pelos dados reais conforme necessário.")

    # Gerando dados fictícios
    df = generate_fake_data()

    # Filtros
    st.sidebar.header("Filtros")
    start_date = st.sidebar.date_input("Data de Início", df['Date'].min())
    end_date = st.sidebar.date_input("Data de Fim", df['Date'].max())

    if start_date > end_date:
        st.sidebar.error("Data de início não pode ser posterior à data de fim.")
    else:
        filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

        # Gráficos
        st.subheader("Preço do Barril ao Longo do Tempo")
        st.line_chart(filtered_df.set_index('Date')['Price'])

        st.subheader("Histograma de Preços")
        st.bar_chart(filtered_df['Price'].value_counts().sort_index())

        st.subheader("Estatísticas dos Preços")
        st.write(filtered_df.describe())

        # Mais gráficos podem ser adicionados aqui conforme necessário

def replace_with_real_data():
    """
    Função para substituir dados fictícios por dados reais.
    """
    # Substitua a geração de dados fictícios pela leitura dos seus dados reais.
    # Exemplo:
    # df = pd.read_csv('path/to/your/real_data.csv')
    # return df
    pass

# Chamando a função show para exibir a página
show()
