# 🤖 Finn: Seu Planejador Financeiro Inteligente

O **Finn** é um agente financeiro consultivo desenvolvido para ajudar brasileiros a organizarem seus gastos e atingirem metas de longo prazo (como reservas de emergência ou grandes compras) de forma realista e segura.

## 🎯 Caso de Uso
O Finn resolve a dificuldade de planejamento financeiro para pessoas sem conhecimentos técnicos na área. Ele analisa a renda, o padrão de gastos e o custo de vida regional para sugerir ajustes práticos no orçamento.

## 🧠 Inteligência e Persona
- **Nome:** Finn.
- **Personalidade:** Consultivo, calmo, formal e educativo.
- **Estratégia Anti-Alucinação:** O agente utiliza estritamente os dados fornecidos nos arquivos CSV/JSON e admite quando não possui informações suficientes para uma análise.

## 🛠️ Tecnologias Utilizadas
- **Interface:** Streamlit.
- **LLM:** Google Gemini (modelo `gemini-2.5-flash`).
- **Linguagem:** Python com bibliotecas Pandas e GenAI.

## 📊 Base de Conhecimento
O agente consome dados mockados para personalizar a experiência:
- `perfil_investidor.json`: Dados demográficos e metas do usuário.
- `transacoes.csv`: Histórico recente de receitas e despesas.
- `custo_de_vida.json`: Referência de gastos por estado brasileiro.
- `produtos_financeiros.json`: Opções de investimento para recomendações.
- `historico.txt`: Memória de curto prazo das conversas anteriores.

## 🏗️ Estrutura do Projeto
```text
src/
├── app.py              # Interface visual em Streamlit
├── agenteT.py          # Lógica principal, integração com Gemini e RAG
├── config.py           # Gestão de variáveis de ambiente
└── requirements.txt    # Dependências do projeto
