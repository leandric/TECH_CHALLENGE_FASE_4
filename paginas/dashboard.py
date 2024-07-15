import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.title("Dashboard")
    st.write("Conteúdo da página de dashboard.")

    # Carregar os dados
    file_path = 'base_dash.csv'  # Atualize com o caminho correto se necessário
    data = pd.read_csv(file_path)

    # Convertendo a coluna 'ds' para datetime
    data['ds'] = pd.to_datetime(data['ds'])

    # Filtro de datas
    st.sidebar.header('Filtrar por data')
    start_date = st.sidebar.date_input('Data de início', data['ds'].min())
    end_date = st.sidebar.date_input('Data de fim', data['ds'].max())

    # Aplicar filtro
    filtered_data = data[(data['ds'] >= pd.to_datetime(start_date)) & (data['ds'] <= pd.to_datetime(end_date))]

    # Título do dashboard
    st.title('Dashboard de Valores do Petróleo Brent')

    # Gráfico de série temporal
    st.header('Valores do Petróleo Brent ao Longo do Tempo')
    fig, ax = plt.subplots()
    ax.plot(filtered_data['ds'], filtered_data['y'])
    ax.set_xlabel('Data')
    ax.set_ylabel('Valor do Barril ($)')
    ax.set_title('Valores do Petróleo Brent ao Longo do Tempo')
    st.pyplot(fig)

    # Cálculo de médias mensais e anuais
    filtered_data['month'] = filtered_data['ds'].dt.to_period('M')
    filtered_data['year'] = filtered_data['ds'].dt.to_period('Y')

    monthly_avg = filtered_data.groupby('month')['y'].mean().reset_index()
    yearly_avg = filtered_data.groupby('year')['y'].mean().reset_index()

    # Gráfico de médias mensais
    st.header('Média Mensal dos Valores do Petróleo Brent')
    fig, ax = plt.subplots()
    ax.plot(monthly_avg['month'].astype(str), monthly_avg['y'])
    ax.set_xlabel('Mês')
    ax.set_ylabel('Valor Médio do Barril ($)')
    ax.set_title('Média Mensal dos Valores do Petróleo Brent')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Gráfico de médias anuais
    st.header('Média Anual dos Valores do Petróleo Brent')
    fig, ax = plt.subplots()
    ax.plot(yearly_avg['year'].astype(str), yearly_avg['y'])
    ax.set_xlabel('Ano')
    ax.set_ylabel('Valor Médio do Barril ($)')
    ax.set_title('Média Anual dos Valores do Petróleo Brent')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Indicação de possível compra
    st.header('Indicação de Possível Compra')
    current_price = filtered_data['y'].iloc[-1]
    average_price = filtered_data['y'].mean()

    if current_price < average_price:
        st.success(f'O preço atual do barril (${current_price:.2f}) está abaixo da média (${average_price:.2f}). Pode ser um bom momento para comprar.')
    else:
        st.warning(f'O preço atual do barril (${current_price:.2f}) está acima da média (${average_price:.2f}). Pode ser prudente esperar.')
