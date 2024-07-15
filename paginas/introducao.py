import streamlit as st

def show():
    st.markdown('''
### Documentação do Projeto

---

# Tech Challenge: Previsão do Preço do Petróleo

## 1. Introdução
Este projeto tem como objetivo analisar os dados históricos do preço do petróleo, realizar uma análise exploratória dos dados (EDA), desenvolver modelos de Machine Learning para prever o preço do petróleo e criar um dashboard interativo para visualização dos resultados.

## 2. Coleta de Dados
Os dados históricos do preço do petróleo foram coletados do site do [IPEA](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view). A base de dados contém duas colunas principais: data e preço (em dólares).
Tambem coletamos dados usando yahoo finance para de ativos do mercado do petróleo:
* XLE: Energy Select Sector SPDR Fund
O **Energy Select Sector SPDR Fund (XLE)** é um fundo negociado em bolsa (ETF) que busca fornecer resultados de investimento que, antes das despesas, correspondam geralmente ao desempenho do índice de Energy Select Sector. Este ETF é projetado para representar o setor de energia da S&P 500, incluindo empresas envolvidas na produção e distribuição de petróleo e gás, equipamentos de perfuração e outros serviços de energia.

* CL=F: WTI Crude Oil
O **WTI Crude Oil (CL=F)**, ou Petróleo Bruto West Texas Intermediate, é um tipo de petróleo bruto usado como referência no preço do petróleo. É extraído e negociado principalmente nos Estados Unidos e é conhecido por sua alta qualidade devido ao seu baixo teor de enxofre e densidade relativamente baixa.

* BZ=F: Brent Crude Oil
O **Brent Crude Oil (BZ=F)** é uma referência importante para o preço do petróleo a nível mundial. Extraído principalmente do Mar do Norte, o Brent é utilizado como referência para os preços de cerca de dois terços das negociações globais de petróleo bruto. O Brent é conhecido por sua qualidade ligeiramente inferior ao WTI, mas é mais amplamente utilizado como padrão global de preços.


## 3. Análise Exploratória dos Dados (EDA)
A análise exploratória foi realizada para entender melhor a distribuição dos preços do petróleo, identificar tendências e padrões, e detectar outliers.

|                          | Energy Select Sector SPDR Fund | WTI Crude Oil | Brent Crude Oil | Barril     |
|--------------------------|--------------------------------|---------------|-----------------|------------|
| **Count**                | 6430.000000                    | 5998.000000   | 4210.000000     | 6380.000000|
| **Mean**                 | 57.461869                      | 64.518905     | 78.741886       | 64.578966  |
| **Std**                  | 21.085923                      | 25.282054     | 24.660009       | 30.077153  |
| **Min**                  | 19.799999                      | **-37.630001** | 19.330000       | 9.120000   |
| **25%**                  | 36.150002                      | 45.340000     | 59.325000       | 40.277500  |
| **50%**                  | 60.014999                      | 63.105000     | 77.154999       | 63.110000  |
| **75%**                  | 74.300003                      | 83.255001     | 101.250002      | 84.945000  |
| **Max**                  | 101.290001                     | 145.289993    | 146.080002      | 143.950000 |

### Por que o WTI Crude Oil chegou a ter preço negativo?

O preço negativo do WTI Crude Oil observado nos dados pode ser explicado por um evento histórico ocorrido em abril de 2020. Durante essa época, o mercado de petróleo enfrentou uma situação sem precedentes devido a uma combinação de fatores:

**Queda na Demanda Global:** 
   * A pandemia de COVID-19 levou a uma drástica redução na demanda global por petróleo. Com a maioria dos países impondo lockdowns e restrições de viagens, o consumo de petróleo diminuiu significativamente.

**Excesso de Oferta:** 
   * Ao mesmo tempo, a produção de petróleo não foi ajustada rapidamente para compensar a queda na demanda. Isso levou a um excesso de oferta no mercado.

                
**Capacidade de Armazenamento:** 
   * O excesso de oferta e a queda na demanda levaram ao esgotamento da capacidade de armazenamento. Os locais onde o petróleo poderia ser armazenado ficaram saturados.

                
**Vencimento dos Contratos Futuros:**
   * Os preços negativos ocorreram especificamente para os contratos futuros do WTI Crude Oil com vencimento em maio de 2020. Os traders que mantinham esses contratos eram obrigados a aceitar a entrega física do petróleo. Com a falta de espaço de armazenamento, muitos se viram obrigados a pagar para que outros aceitassem a entrega, resultando em preços negativos.

                
Esses fatores combinados criaram uma situação excepcional onde os preços do petróleo caíram abaixo de zero, algo nunca antes visto na história dos mercados de petróleo.               

## Análise da Série Temporal
![série Temporal](img/serie-temporal.png)

                
                ''')

