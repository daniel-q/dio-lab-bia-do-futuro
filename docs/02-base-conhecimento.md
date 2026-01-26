# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |
| `custos_de_vida.json` | JSON | Ajustar a analise para o contesto do cliente |

> [!TIP]

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Adicionado os dados mocados de custo de vida de diferentes estados

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.


Os dados serão carregados no prompt via código

'''
import pandas as pd
import json

historico = pd.read_csv('data/historico_atendimento.csv')
historico = pd.read_csv('data/transacoes.csv')

with open('data/perfil_investidor.json','r', encoding = 'utf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json','r', encoding = 'utf-8') as f:
  perfil = json.load(f)

with open('data/custos_de_vida.json','r', encoding = 'utf-8') as f:
  perfil = json.load(f)
'''

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os custos de vida e produtos financeiro serão carregadas para todos e o histórico de atendimento, transações e perfil do cliente serão carregados individualmente para cada cliente

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Estado: São Paulo
- Status: Cadados
- Filhos: 2
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
