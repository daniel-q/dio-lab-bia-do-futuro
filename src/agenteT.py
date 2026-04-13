import os
import json
import pandas as pd
from google import genai
from dotenv import load_dotenv

# 1. Configurações Iniciais
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_ID = "gemini-2.5-flash"

# --- 2. CARREGAMENTO DA BASE DE CONHECIMENTO ---

def carregar_dados():
    try:
        historico_csv = pd.read_csv('../data/historico_atendimento.csv')
        transacoes_csv = pd.read_csv('../data/transacoes.csv')

        with open('../data/perfil_investidor.json', 'r', encoding='utf-8') as f:
            perfil = json.load(f)
        with open('../data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
            produtos = json.load(f)
        with open('../data/custo_de_vida.json', 'r', encoding='utf-8') as f:
            custos = json.load(f)

        # Montagem do bloco de Contexto fixo do usuário
        contexto_texto = f"""
### DADOS DO CLIENTE ATUAL ###
NOME: {perfil.get('nome')} | IDADE: {perfil.get('idade')} | ESTADO: {perfil.get('estado')}
RENDA: R$ {perfil.get('renda_mensal')} | PROFISSÃO: {perfil.get('profissao', 'Não informada')}
PATRIMÔNIO TOTAL: R$ {perfil.get('patrimonio_total')}
RESERVA ATUAL: R$ {perfil.get('reserva_emergencia_atual')}

### ÚLTIMAS TRANSAÇÕES ###
{transacoes_csv.tail(10).to_string(index=False)}

### PRODUTOS DISPONÍVEIS ###
{json.dumps(produtos, indent=2, ensure_ascii=False)}

### REFERÊNCIA: CUSTO DE VIDA POR ESTADO ###
{json.dumps(custos, indent=2, ensure_ascii=False)}
"""
        return contexto_texto
    except Exception as e:
        print(f"Erro ao carregar arquivos: {e}")
        return ""

# --- 3. GERENCIAMENTO DE MEMÓRIA (TXT) ---

def gerenciar_historico(pergunta=None, resposta=None, ler=True):
    caminho = '../data/historico.txt'
    if not os.path.exists('data'): os.makedirs('data')
    
    if ler:
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as f:
                # Retorna apenas as últimas 2000 letras para não estourar o prompt
                return f.read()[-2000:]
        return ""
    else:
        with open(caminho, 'a', encoding='utf-8') as f:
            f.write(f"\nUsuário: {pergunta}\nFinn: {resposta}\n{'-'*20}")

# --- 4. PROMPTS ---

SYSTEM_PROMPT = """
Você é Finn, um assistente financeiro especializado em planejamento de metas financeiras pessoais.
Seu foco é sugerir ações práticas e realistas baseadas nos dados fornecidos.
Assuma que o usuário está no Brasil. Seja consultivo, calmo e objetivo.
Siga estritamente o formato:
1. Confirmação do entendimento
2. Análise resumida da situação
3. Sugestões práticas (em lista)
4. Próximo passo sugerido
"""

EXEMPLOS = """
Exemplo:
Usuário: Quero juntar 50k em 1 ano ganhando 2k.
Finn: Entendi seu objetivo. Com essa renda, a meta é matematicamente desafiadora no prazo de 12 meses. 
Sugiro: 1. Aumentar o prazo para 48 meses. 2. Reduzir a meta inicial para 5k.
"""

# --- 5. FUNÇÃO PRINCIPAL DE PERGUNTA ---

def perguntar(mensagem_usuario):
    contexto_dados = carregar_dados()
    memoria_conversacao = gerenciar_historico(ler=True)

    config_gemini = {
        "system_instruction": SYSTEM_PROMPT,
        "temperature": 0.2, # Menos aleatoriedade para finanças
    }

    prompt_final = f"""
{contexto_dados}

HISTÓRICO DE CONVERSAS RECENTES:
{memoria_conversacao}

{EXEMPLOS}

PERGUNTA ATUAL DO USUÁRIO: {mensagem_usuario}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt_final,
            config=config_gemini
        )
        
        resposta_texto = response.text
        
        # Salva no histórico para a próxima rodada
        gerenciar_historico(pergunta=mensagem_usuario, resposta=resposta_texto, ler=False)
        
        return resposta_texto

    except Exception as e:
        return f"Desculpe, tive um erro técnico: {e}"

# --- 6. EXECUÇÃO ---

if __name__ == "__main__":
    print("--- Finn: Assistente Financeiro Ativo ---")
    while True:
        user_input = input("\nVocê: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            break
            
        print("\nFinn analisando...")
        print(f"\nFinn: {perguntar(user_input)}")
