import streamlit as st

def show():
    st.title("Sobre o Time")
    st.write("Conheça os membros do nosso time abaixo:")

    # Definindo informações sobre cada membro
    team_members = [
        {
            "name": "Leandro Soares da Silva",
            "photo": "https://ovicio.com.br/wp-content/uploads/2022/06/20220628-goku_trw2.jpg",  # Caminho para a foto do Leandro
            "description": "Especialista em dados com experiência em Python, BigQuery, Looker e IA.",
            "linkedin": "https://www.linkedin.com/in/leandro"
        },
        {
            "name": "Membro 2",
            "photo": "https://ovicio.com.br/wp-content/uploads/2022/06/20220628-goku_trw2.jpg",  # Caminho para a foto do Membro 2
            "description": "Descrição sobre o Membro 2.",
            "linkedin": "https://www.linkedin.com/in/membro2"
        },
        {
            "name": "Membro 3",
            "photo": "https://ovicio.com.br/wp-content/uploads/2022/06/20220628-goku_trw2.jpg",  # Caminho para a foto do Membro 3
            "description": "Descrição sobre o Membro 3.",
            "linkedin": "https://www.linkedin.com/in/membro3"
        }
    ]

    # Exibindo informações sobre cada membro
    for member in team_members:
        st.subheader(member["name"])
        st.image(member["photo"], width=150)
        st.write(member["description"])
        st.write(f"[LinkedIn]({member['linkedin']})")
        st.markdown("---")

