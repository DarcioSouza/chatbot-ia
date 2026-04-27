import streamlit as st

st.set_page_config(page_title="Chatbot de Atendimento IA")

st.title("🤖 Chatbot de Atendimento Inteligente")

st.caption("Atendimento automatizado com Inteligência Artificial (simulada)")

# histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# mostrar histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# entrada do usuário
user_input = st.chat_input("Digite sua pergunta...")

# função de resposta simulada (INTELIGENTE)
def gerar_resposta(pergunta):
    pergunta = pergunta.lower()

    if "preço" in pergunta or "valor" in pergunta:
        return "Nossos planos começam a partir de R$ 49,90 por mês. Posso te explicar os detalhes 😊"

    elif "suporte" in pergunta:
        return "Nosso suporte funciona 24h por dia, 7 dias por semana."

    elif "serviço" in pergunta:
        return "Oferecemos soluções em tecnologia, automação e inteligência artificial."

    elif "oi" in pergunta or "olá" in pergunta:
        return "Olá! 👋 Como posso te ajudar hoje?"

    else:
        return "Ótima pergunta! Vou encaminhar isso para um especialista e retorno em breve 😉"

# lógica principal
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    resposta = gerar_resposta(user_input)

    st.session_state.messages.append({"role": "assistant", "content": resposta})

    with st.chat_message("assistant"):
        st.write(resposta)

    # botão para limpar conversa
if st.button("🔄 Reiniciar conversa"):
    st.session_state.messages = []
    st.rerun()