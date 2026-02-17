# WebAPP com dados do Fifa (17 - 23)

Aplicação Web Python e Streamlit usando os conjuntos de dados do fifa (17 á 23), desenvolvida como projeto minsitrado pela **Asimov Academy**, porém com modificações autorais (Filtro de escolha da edição do jogo entre 2017 e 2023 na visualização dos dados nas pages).

---
Este WebAPP é uma aplicação que mescla:

- Limpeza e filtro de dados com Pandas
- Desenvolvimento de aplicações web simples com streamlit
- Organização e estruturação de projetos (Python)

---
Em suma, a aplicação visa simplificar a visualização de dados e estatísticas de atletas e seus respectivos clubes registrados nos jogos da EA sports.
Você pode navegar pelos conjuntos de 2017 até o de 2023, e acompanhar a mudança e evolução dos jogadores no game, através do tempo.
A simples aplicação é divida na página Home (Apresentação do projeto + link para o conjunto de dados); Players (Visualização de dados do jogador escolhido
pelo usuário através do filtro de Ano do jogo e Clube); Teams (DataFrame com dados de cada atleta através do clube e ano do jogo escolhido)

--- 
Tecnologias Usadas:

- Python
- Streamlit
- Pandas
---
Estrutura do Projeto:

WEBAPP_FIFA/
|
|--datasets/
|--pages/
| |-01Players.py
| |-02Teams.py
|
|- Home.py
|- Utilidades.py
|- requirements.txt
|- README.md
