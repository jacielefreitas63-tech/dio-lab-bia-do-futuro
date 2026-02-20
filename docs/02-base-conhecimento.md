# Base de Conhecimento

## Dados Utilizados

Descrevi abaixo os arquivos da pasta data que sustentam as decisões da Bia:

| Arquivo | Formato | Utilização no Agente |
| :--- | :--- | :--- |
| historico_financeiro.csv | CSV | Analisar o custo de vida médio do usuário nos últimos meses. |
| perfil_seguranca.json | JSON | Identificar se o usuário é CLT ou Autônomo para definir o tamanho da reserva. |
| produtos_liquidez.json | JSON | Sugerir onde guardar o dinheiro (ex: Tesouro Selic, CDB 100% CDI). |
| metas_pessoais.csv | CSV | Acompanhar a evolução dos aportes mensais para a reserva. |

---

## Adaptações nos Dados

Para esta solução, expandi os dados mockados para incluir uma diferenciação clara entre *profissionais estáveis (CLT)* e *profissionais com renda variável (Autônomos)*. Isso permite que a Bia seja mais precisa: recomendando 6 meses de cobertura para uns e 12 meses para outros.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV são carregados no início da sessão do Python e convertidos em dicionários ou DataFrames do Pandas. Essas informações são então injetadas no contexto do prompt da IA.

### Como os dados são usados no prompt?
Os dados financeiros brutos passam por uma função de resumo antes de irem para o sistema. A IA não lê todas as transações, mas sim o *total de gastos por categoria*, para manter a privacidade e não exceder o limite de tokens.

---

## Exemplo de Contexto Montado

Abaixo, um exemplo de como os dados são formatados para que a Bia entenda o caso antes de responder:

*Dados do Cliente:*
- *Nome:* Jaciele Freitas
- *Perfil:* Autônoma (Renda Oscilante)
- *Custo de Vida Mensal:* R$ 3.000

*Últimas Transações Analisadas:*
- 10/02: Supermercado - R$ 450
- 12/02: Aluguel - R$ 1.200
- 15/02: Energia - R$ 200

*Meta Sugerida pela Bia:*
- Reserva de 12 meses (R$ 36.000,00) devido ao perfil autônomo.

