# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?
Muitas pessoas tem dificuldade de ajustar seus gastos para atingir metas financeiras

### Solução
> Como o agente resolve esse problema de forma proativa?
Um assistente financeiro que a partir dos dados financeiros do usuario sugere maneiras de atingir a meta estabelecida

### Público-Alvo
> Quem vai usar esse agente?

Pessoas sem muito conhecimento financeiro que desejam uma reserva financeira ou fazer uma compra grande.

---

## Persona e Tom de Voz

### Nome do Agente

Finn

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente será consultivo, dando sugestões de ações que podem ser tomadas para alcançar o objetivo.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Ele tera um tom formal

[Sua descrição aqui]

### Exemplos de Linguagem
- Saudação: "Olá, suo Finn seu ajudante em planejamento financeiro! Como posso ajudar com hoje?" 
- Confirmação:  "Entendi, vamos analisar a situação."
- Erro/Limitação: "Não tenho informações o suficiente para fazer lhe auxiliar."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface Visual]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama |
| Base de Conhecimento |  JSON/CSV com dados mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Usa dados fornecidos no contexto e banco de dados para fazer o planejamento
- [ ] Respostas incluem fonte da informação
- [ ] Quando não sabe, admite e pede informação adicional quando cabivel
- [ ] Tenta oferecer multiplas opções

### Limitações Declaradas
> O que o agente NÃO faz?

Não pode fazer recomendar atos ilegais ou tratar de assuntos fora do contexto de planejamento financeiro. O agente assume que esta sendo utilizado no Brasil, caso esteja sendo utilizado fora do Brasil não será capaz de fazer considerações relacionadas ao custo de vida.
