import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def generate_fake_data():
    np.random.seed(42)
    dates = pd.date_range(start='2020-01-01', periods=365)
    prices = np.random.normal(50, 10, size=len(dates)).round(2)
    return pd.DataFrame({'Date': dates, 'Price': prices})
    
def show():
    st.title("Dashboard do Preço do Barril de Petróleo")
    st.write("O petróleo é uma das commodities mais importantes do mundo, influenciando significativamente a economia global. Entre as várias referências de preços de petróleo, o Brent é uma das mais utilizadas, servindo como benchmark para o preço de dois terços do petróleo mundial. Este dashboard tem como objetivo fornecer uma análise detalhada dos preços históricos do petróleo Brent, bem como realizar previsões futuras para auxiliar na tomada de decisões estratégicas.")

    st.markdown('### Objetivos do Dashboard')
    st.write("**1 - Análise Histórica de Preços**")
    st.write("- Apresentar a variação dos preços do petróleo Brent ao longo dos anos.")
    st.write("- Identificar tendências e padrões históricos que possam influenciar os preços futuros.")
    
    st.write("**2 - Comparação com Outros Índices:**")
    st.write("- Comparar os preços do Brent com outros índices de petróleo e commodities relacionadas.")
    st.write("- Analisar a correlação entre o preço do petróleo Brent e variáveis econômicas relevantes.")

    st.write("**3 - Previsões de Preços:**")
    st.write("- Utilizar modelos de machine learning para prever os preços futuros do petróleo Brent.")
    st.write("- Fornecer insights sobre possíveis cenários econômicos com base nas previsões realizadas.")

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







# Função para carregar os dados
@st.cache
def load_data():
    file_path = 'D:/FIAP/FASE 4/TECH_CHALLENGE_FASE_4/base.csv'
    df = pd.read_csv(file_path)
    # Convertendo a coluna 'Date' para datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df

# Carregar os dados
data = load_data()

# Remover linhas com datas inválidas
data = data.dropna(subset=['Date'])


# Visão Geral dos Preços
st.subheader("Visão Geral dos Preços")

st.write("Série Temporal:")
fig1 = px.line(data, x='Date', y=['Brent Crude Oil', 'WTI Crude Oil', 'barril'], title='Preços do Brent, WTI e Barril')
st.plotly_chart(fig1)

st.write("- Tendência de Alta de Longo Prazo (1998-2008): Os preços dos ativos relacionados ao petróleo mostraram uma tendência de alta consistente de 1998 até 2008. Esta tendência pode estar relacionada ao crescimento econômico global e ao aumento da demanda por petróleo.")
st.write("- Crise Financeira Global (2008-2009): Em 2008, há uma queda acentuada nos preços dos ativos, coincidente com a crise financeira global. Esta queda foi resultado de uma contração econômica global, que reduziu a demanda por petróleo.")
st.write("- Recuperação Pós-Crise (2009-2014): Após a crise de 2008-2009, os preços dos ativos começaram a se recuperar, atingindo novos picos em torno de 2012-2014. Isso pode estar associado à recuperação econômica global e ao aumento da demanda por petróleo.")
st.write("- Queda dos Preços do Petróleo (2014-2016): Entre 2014 e 2016, os preços do petróleo caíram significativamente devido a um excesso de oferta global de petróleo, incluindo o aumento da produção de petróleo de xisto nos Estados Unidos.")
st.write("- Oscilações e Recuperação (2016-2019):Após a queda de 2014-2016, os preços dos ativos mostraram oscilações, mas mantiveram uma tendência de recuperação moderada até 2019.")
st.write("- Impacto da Pandemia de COVID-19 (2020): Em 2020, há uma queda abrupta e temporária nos preços do petróleo, coincidindo com a pandemia de COVID-19. Isso resultou em uma queda drástica na demanda por petróleo devido a lockdowns globais e restrições de viagens, levando até a preços negativos em contratos futuros de petróleo, como observado no WTI Crude Oil.")
st.write("- Recuperação Pós-Pandemia (2021-2024): Após o impacto inicial da pandemia, os preços dos ativos voltaram a subir conforme a demanda por petróleo começou a se recuperar. Esta recuperação é visível na série temporal até 2024.")


# Análise de Tendências
st.subheader('Análise de Tendências')
fig2 = px.line(data, x='Date', y=['Brent Crude Oil', 'WTI Crude Oil'], title='Tendências de Preços do Brent e WTI')
st.plotly_chart(fig2)

st.subheader("Insights")
st.write("Correlação entre Ativos:")
st.write("Os preços dos diferentes ativos (Energy Select Sector SPDR Fund, WTI Crude Oil, Brent Crude Oil, e o preço do barril de petróleo Brent) tendem a se mover juntos, indicando alta correlação entre eles. Isso pode ser visto nas tendências e oscilações similares ao longo do tempo.")
st.write("Volatilidade:")
st.write("A volatilidade é evidente em vários períodos, especialmente durante crises econômicas e eventos globais significativos, como a crise financeira de 2008 e a pandemia de COVID-19 em 2020.")
st.write("Resiliência e Recuperação:")
st.write("O mercado de petróleo mostrou resiliência, com preços se recuperando após quedas significativas. A recuperação pós-crise financeira e pós-pandemia são exemplos notáveis dessa resiliência.")

# Correlação entre Preços

st.subheader('Correlação entre Preços')
fig3 = px.scatter(data, x='Brent Crude Oil', y='barril', title='Correlação entre Preços do Brent e do Barril')
st.plotly_chart(fig3)



# Função para carregar os dados
@st.cache
def load_data_preços():
    file_path = 'D:/FIAP/FASE 4/TECH_CHALLENGE_FASE_4/base_de_precos.csv'
    dfpreços = pd.read_csv(file_path)
    # Convertendo a coluna 'Date' para datetime
    dfpreços['Data'] = pd.to_datetime(dfpreços['Data'], errors='coerce')
    return dfpreços

# Mostrar os dados carregados
st.write('**Dados Carregados:**')
st.write(dfpreços)


# Calcular a matriz de correlação
correlation_matrix = dfpreços.corr()

# Exibir a matriz de correlação como um gráfico de heatmap
st.write('**Matriz de Correlação (Heatmap):**')
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlação')
plt.show()

# Mostrar a matriz de correlação como dataframe
st.write('**Matriz de Correlação (Dataframe):**')
st.write(correlation_matrix)

st.subheader('Análise da Correlação Focada no Barril')
st.write("Vamos focar na correlação do preço do barril de petróleo Brent (barril) com os demais ativos:")
st.write("1 - Correlação entre Barril e Energy Select Sector SPDR Fund (0.822582):")
st.write("- Correlação Positiva Forte: Uma correlação de 0.82 indica uma relação positiva forte entre o preço do barril de petróleo Brent e o Energy Select Sector SPDR Fund. Isso sugere que, quando o preço do barril aumenta, o preço do fundo de energia também tende a aumentar. Essa relação forte pode ser explicada pelo fato de que empresas dentro do Energy Select Sector SPDR Fund são diretamente afetadas pelos preços do petróleo, que impactam seus custos e receitas.")
st.write(" 2 - Correlação entre Barril e WTI Crude Oil (0.980815):")
st.write("- Correlação Positiva Muito Forte: A correlação de 0.98 indica uma relação quase perfeita entre o preço do barril de petróleo Brent e o WTI Crude Oil. Isso significa que os preços dos dois tipos de petróleo tendem a se mover juntos quase exatamente. Essa alta correlação é esperada, dado que ambos são benchmarks globais para preços do petróleo e estão sujeitos a influências semelhantes do mercado global.")
st.write("3 - Correlação entre Barril e Brent Crude Oil (0.996401):")
st.write("- Correlação Positiva Quase Perfeita: A correlação de 0.996 é praticamente perfeita, o que é intuitivo, pois barril refere-se ao preço do Brent Crude Oil. Portanto, qualquer movimento no preço do Brent Crude Oil é refletido diretamente no preço do barril de petróleo Brent. Esta correlação quase perfeita confirma que estamos lidando com dados praticamente idênticos.")



