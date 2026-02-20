import streamlit as st
import json
import os

# Função para carregar os dados das pastas que criamos
def carregar_json(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

# Configuração Visual
st.set_page_config(page_title="Bia - Mentora Financeira", page_icon="💰")
st.title("🤖 Bia: Sua Mentora de Reserva de Emergência")
st.markdown("---")

# Buscando dados na pasta /data/ que você criou
perfil = carregar_json('data/perfil_usuario.json')
produtos = carregar_json('data/produtos_financeiros.json')

if perfil:
    # Lógica de cálculo da Bia
    meses_reserva = 12 if perfil['tipo_profissional'] == "Autônomo" else 6
    valor_meta = perfil['custo_vida_mensal'] * meses_reserva
    
    st.sidebar.success(f"Perfil: {perfil['tipo_profissional']}")
    
    st.write(f"### Olá {perfil['nome']}! 👋")
    st.info(f"Para sua segurança como {perfil['tipo_profissional']}, sua meta de reserva é *R$ {valor_meta:,.2f}*.")
    
    # Exibição de produtos da base de conhecimento
    if produtos:
        st.write("#### 🏦 Onde investir sua reserva:")
        for p in produtos:
            st.warning(f"*{p['produto']}*: Risco {p['risco']} | Liquidez {p['liquidez']}")
else:
    st.error("⚠️ Erro: Certifique-se de que os arquivos JSON estão na pasta 'data'.")

# Campo de Chat
st.text_input("Pergunte algo à Bia:")
