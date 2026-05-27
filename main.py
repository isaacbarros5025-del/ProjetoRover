import streamlit as st
import sqlite3
import subprocess
import sys 

st.set_page_config(
    page_title="Projeto Rover Lunar",
    page_icon="🚀",
    layout="wide"
)
        
# BANCO DE DADOS (rover.db)

conn = sqlite3.connect("rover.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    senha TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rovers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rover TEXT,
    equipe TEXT,
    integrantes TEXT,
    descricao TEXT,
    linguagem TEXT,
    status TEXT,
    usuario TEXT
)
""")

conn.commit()


# FUNÇÕES

def carregar_usuarios():
    cursor.execute("SELECT usuario, senha FROM usuarios")
    return [{"usuario": u[0], "senha": u[1]} for u in cursor.fetchall()]

def salvar_usuario(usuario, senha):
    cursor.execute(
        "INSERT INTO usuarios VALUES (NULL, ?, ?)",
        (usuario, senha)
    )
    conn.commit()

def carregar_rovers():
    cursor.execute("""
        SELECT rover, equipe, integrantes, descricao, linguagem, status, usuario
        FROM rovers
    """)
    return [
        {
            "rover": r[0],
            "equipe": r[1],
            "integrantes": r[2],
            "descricao": r[3],
            "linguagem": r[4],
            "status": r[5],
            "usuario": r[6]
        }
        for r in cursor.fetchall()
    ]

def salvar_rover(rovers):
    cursor.execute("""
        INSERT INTO rovers
        VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
    """, rovers)
    conn.commit()
    
def deletar_rover(nome_rover, usuario):
    cursor.execute(
        "DELETE FROM rovers WHERE rover=? AND usuario=?",
        (nome_rover, usuario)
    )
    conn.commit()


# SESSION STATE

if "pagina" not in st.session_state:
    st.session_state.pagina = "home"

if "logado" not in st.session_state:
    st.session_state.logado = False

if "usuario" not in st.session_state:
    st.session_state.usuario = ""


# HOME

if st.session_state.pagina == "home":
    st.title("🚀 Projeto Rover Lunar")
    st.markdown("---")
    st.subheader("Sistema de Gerenciamento de Rovers")
    st.write("""
    Plataforma desenvolvida para gerenciamento de equipes e rovers.
    """)
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Fazer Login", use_container_width=True):
            st.session_state.pagina = "login"
            st.rerun()

    with col2:
        if st.button("📝 Criar Conta", use_container_width=True):
            st.session_state.pagina = "cadastro"
            st.rerun()


# CADASTRO

elif st.session_state.pagina == "cadastro":
    st.title("📝 Cadastro")

    usuario = st.text_input("Nome de usuário")
    senha = st.text_input("Senha", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Cadastrar", use_container_width=True):
            usuarios = carregar_usuarios()
            existe = False

            for u in usuarios:
                if u["usuario"] == usuario:
                    existe = True

            if usuario == "" or senha == "":
                st.warning("Preencha todos os campos!")
            elif existe:
                st.error("Usuário já existe!")
            else:
                salvar_usuario(usuario, senha)
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.session_state.pagina = "painel"
                st.success("Cadastro realizado!")
                st.rerun()

    with col2:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.pagina = "home"
            st.rerun()


# LOGIN

elif st.session_state.pagina == "login":
    st.title("🔐 Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Entrar", use_container_width=True):
            usuarios = carregar_usuarios()
            login_ok = False

            for u in usuarios:
                if u["usuario"] == usuario and u["senha"] == senha:
                    login_ok = True

            if login_ok:
                st.session_state.logado = True
                st.session_state.usuario = usuario
                st.session_state.pagina = "painel"
                st.success("Login realizado!")
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos!")

    with col2:
        if st.button("⬅ Voltar", use_container_width=True):
            st.session_state.pagina = "home"
            st.rerun()


# PAINEL

elif st.session_state.pagina == "painel":
    if not st.session_state.logado:
        st.session_state.pagina = "login"
        st.rerun()

    st.sidebar.title("🚀 Menu")
    menu = st.sidebar.radio(
        "Navegação",
        ["Dashboard", "Cadastrar Rover", "Área de Controle", "Rovers Cadastrados"]
    )

    st.sidebar.success(f"Usuário: {st.session_state.usuario}")

    if st.sidebar.button("🚪 Sair"):
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.session_state.pagina = "login"
        st.rerun()

    
    # DASHBOARD
    
    if menu == "Dashboard":
        st.title("📊 Dashboard")
        rovers = carregar_rovers()
        st.metric("Total de Rovers", len(rovers))
        st.subheader("Últimos Rovers")

        for r in rovers[-3:]:
            st.write(f"🚗 {r['rover']} | 👥 {r['equipe']}")


    # CADASTRAR ROVER
    
    elif menu == "Cadastrar Rover":
        st.title("🚗 Cadastro de Rover")

        nome_rover = st.text_input("Nome do Rover")
        equipe = st.text_input("Nome da Equipe")
        integrantes = st.text_area("Integrantes")
        descricao = st.text_area("Descrição")

        linguagem = st.selectbox(
            "Linguagem Utilizada",
            ["Python", "C++", "Java", "JavaScript", "Arduino", "Outra"]
        )

        status = st.selectbox(
            "Status do Projeto",
            ["Planejamento", "Em Desenvolvimento", "Finalizado"]
        )

        if st.button("Salvar Rover", use_container_width=True):
            if nome_rover == "" or equipe == "" or descricao == "":
                st.warning("Preencha os campos obrigatórios!")
            else:
                salvar_rover((
                    nome_rover,
                    equipe,
                    integrantes,
                    descricao,
                    linguagem,
                    status,
                    st.session_state.usuario
                ))
                st.success("Rover cadastrado com sucesso!")


    # ÁREA DE CONTROLE
  
    elif menu == "Área de Controle":
        st.title("🎮 Área de Controle")
        st.info("Controle o seu Rover em tempo real usando o teclado (WASD).")

        if st.button("Abrir Controle (Nova Janela)", use_container_width=True):
            try:
                subprocess.Popen([sys.executable, "controle.py"])
                st.success("A janela de controle foi aberta! Clique nela para pilotar o Rover.")
            except Exception as e:
                st.error(f"Erro ao tentar abrir o controle: {e}")

        st.markdown("---")
        st.subheader("📡 Status do Sistema (Painel)")
        
        cliente = st.session_state.get("cliente", None)
        if cliente:
            st.write("✅ Comunicação web ativa")
            st.write("📶 Rede LAN conectada")
            st.write("🤖 Rover online")
        else:
            st.write("❌ Desconectado do Rover")

  
    # ROVERS CADASTRADOS
    
    elif menu == "Rovers Cadastrados":
        st.title("🚘 Rovers Cadastrados")
        rovers = carregar_rovers()

        for rover in rovers:
            with st.expander(f"{rover['rover']} - {rover['equipe']}"):
                
                # BOTÃO DE EXCLUIR
                
                if rover["usuario"] == st.session_state.usuario:
                    if st.button(f"🗑 Excluir {rover['rover']}"):
                        deletar_rover(rover["rover"], st.session_state.usuario)
                        st.success("Rover excluído com sucesso!")
                        st.rerun()

                st.write(f"👥 Equipe: {rover['equipe']}")
                st.write(f"🧑‍🚀 Integrantes: {rover['integrantes']}")
                st.write(f"📝 Descrição: {rover['descricao']}")
                st.write(f"💻 Linguagem: {rover['linguagem']}")
                st.write(f"📌 Status: {rover['status']}")
                st.write(f"👤 Criado por: {rover['usuario']}")