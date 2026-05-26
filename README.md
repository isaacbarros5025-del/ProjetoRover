# 🚀 Projeto Rover Lunar

Sistema web desenvolvido com Python + Streamlit para gerenciamento e controle remoto de um Rover Lunar utilizando comunicação via Socket TCP/IP com ESP32/Arduino.

---

# 📌 Sobre o Projeto

O sistema permite:

- 👤 Cadastro e login de usuários
- 🚗 Cadastro de rovers
- 📊 Dashboard com informações dos projetos
- 🎮 Controle remoto do rover via navegador
- 📡 Comunicação em tempo real com ESP32/Arduino
- 🗑 Exclusão de rovers cadastrados

---

# 🛠 Tecnologias Utilizadas

- 🐍 Python
- 🌐 Streamlit
- 🗄 SQLite
- 📡 Socket TCP/IP
- 🤖 ESP32 / Arduino IDE

---

# 🎮 Funcionalidades

## 🔐 Sistema de Login
Usuários podem criar contas e acessar o sistema.

## 🚗 Cadastro de Rover
Permite registrar:
- Nome do rover
- Equipe
- Integrantes
- Linguagem utilizada
- Status do projeto
- Descrição

## 📊 Dashboard
Exibe:
- Quantidade total de rovers
- Últimos projetos cadastrados

## 🎮 Área de Controle
Controle remoto do rover com comandos:

- ⬆ Frente
- ⬇ Ré
- ⬅ Esquerda
- ➡ Direita
- 🛑 Parar

Os comandos são enviados via Socket TCP/IP para o ESP32.

---

# 📡 Comunicação Rover ↔ Sistema

O sistema utiliza comunicação TCP/IP.

O Streamlit envia comandos:


- w = frente
- s = trás
- a = esquerda
- d = direita
- p = parar

O ESP32 recebe os comandos e executa os movimentos do rover.

# 🗂 Estrutura do Projeto
- ProjetoRover/
- │
- ├── main.py
- ├── rover.db
- ├── requirements.txt
- ├── README.md
- └── venv/

# ▶ Como Executar
## 1️⃣ Instalar o Python

- Baixe e instale o Python:

https://www.python.org/downloads/

- ⚠ Durante a instalação marque:

- ✅ Add Python to PATH
 
## 2️⃣ Clonar o repositório
- git clone https://github.com/seu-usuario/projeto-rover.git

## 3️⃣ Entrar na pasta
- cd projeto-rover

## 4️⃣ Criar ambiente virtual
- python -m venv venv

## 5️⃣ Ativar ambiente virtual
- Windows
- venv\Scripts\activate
Caso apareça erro de permissão no PowerShell:
- Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

## 6️⃣ Instalar dependências
- pip install -r requirements.txt

## 7️⃣ Executar o projeto
- streamlit run main.py
📦 Dependências

## Exemplo do requirements.txt:

- streamlit
- 🤖 Hardware Utilizado
- ESP32
- Ponte H
- Motores DC
- Chassi Rover
- Bateria
- Rede Wi-Fi local

# 👨‍💻 Equipe de Desenvolvimento
- DIEGO RODRIGUES COSTA DE OLIVEIRA CASTRO
- GUSTAVO SILVA DOS ANJOS
- ISAAC BARROS DE LIMA
- JOÃO PEDRO CRUZ OLIVEIRA
- JÚLIO CESAR DOS SANTOS NASCIMENTO

# 📄 Licença

Projeto desenvolvido para fins educacionais.
