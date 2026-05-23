# 🚀 Projeto Rover Lunar

Sistema de gerenciamento de rovers desenvolvido com Python + Streamlit + SQLite.


## 📌 Sobre o projeto

O Projeto Rover Lunar é uma aplicação web que permite:

- Cadastro de usuários
- Login de usuários
- Cadastro de rovers por equipe
- Visualização de rovers cadastrados
- Controle básico de um rover (simulação)
- Exclusão de rovers cadastrados

O sistema utiliza banco de dados local SQLite para armazenamento das informações.


## 🛠️ Tecnologias utilizadas

- Python 🐍
- Streamlit 🌐
- SQLite 🗄️


## 📁 Estrutura do projeto


projeto-rover/
- │
- ├── main.py
- ├── rover.db
- ├── requirements.txt
- └── README.md


## ▶️ Como executar o projeto

### 1. Instalar dependências

- pip install -r requirements.txt
    - Rodar aplicação:
    - streamlit run main.py
    - 👥 Funcionalidades
    - 🔐 Usuários
    - Criar conta
    - Fazer login
    - 🚗 Rovers
    - Cadastrar rover
    - Visualizar rovers cadastrados
    - Excluir rover (apenas o criador)
    - 🎮 Controle
    - Simulação de comandos (frente, trás, esquerda, direita, parar)
    - 💾 Banco de dados

O projeto utiliza SQLite com duas tabelas:

- usuarios
- rovers

Os dados são salvos localmente no arquivo:

- rover.db

📚 Observações
- Projeto desenvolvido para fins acadêmicos
- Foco em aprendizado de desenvolvimento web com Python
- Não possui integração com hardware real (apenas simulação)

## 👨‍💻 Equipe

Projeto desenvolvido por:

- Diego Rodrigues Costa de Oliveira Castro  
- Gustavo  Silva  dos  anjos
- Isaac Barros de Lima  
- João Pedro Cruz Oliveira  
- Júlio Cesar Dos Santos Nascimento

## 🚀 Demonstração online

👉 Acesse o sistema rodando ao vivo:

[🔗 Abrir Projeto Rover Lunar](https://rover-lunar-system.streamlit.app/)
