# 🤖 Bia: Mentora de Reserva de Emergência

[![GitHub star](https://img.shields.io/github/stars/jacielefreitas63-tech/assistente-voz-IA-DIO?style=social)](https://github.com/jacielefreitas63-tech/assistente-voz-IA-DIO)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto foi desenvolvido como parte do desafio *"Criando Experiências Digitais com IA Generativa"* da trilha de IA da *DIO (Digital Innovation One). A **Bia* é uma assistente inteligente focada em ajudar usuários a construir seu primeiro pilar de segurança financeira: a Reserva de Emergência.

---

## 🚀 Solução Proposta

Muitas pessoas não sabem o valor exato que precisam poupar antes de começar a investir. A *Bia* resolve isso através de:
* *Cálculo Personalizado:* Diferencia automaticamente a meta entre profissionais CLT (6 meses) e Autônomos (12 meses).
* *Educação Financeira:* Explica conceitos como SELIC, CDI e Liquidez Diária de forma simples.
* *Segurança:* Utiliza técnicas de anti-alucinação para não recomendar investimentos de alto risco (como cripto ou apostas).

---

## 🛠️ Tecnologias Utilizadas

* *Python:* Linguagem base para a lógica do agente.
* *Streamlit:* Interface de usuário rápida e intuitiva.
* *JSON/CSV:* Persistência de dados e base de conhecimento.
* *LLM (GPT-4):* Motor de inteligência para compreensão de linguagem natural.
* *Mermaid:* Documentação de arquitetura via código.

---

## 🏗️ Estrutura do Repositório

O projeto segue as diretrizes da DIO para organização de agentes de IA:

* 📁 *data/*: Contém as bases de conhecimento (perfil do usuário e produtos financeiros).
* 📁 *docs/*:
    * 01-documentacao-agente.md: Visão geral e persona.
    * 02-base-conhecimento.md: Detalhes sobre os dados utilizados.
    * 03-prompts.md: Configurações de System Prompt e Few-shot.
    * 04-metricas-e-avaliacao.md: Planos de teste e metas de qualidade.
* 📄 *app.py*: O código-fonte principal do assistente.

---

## 📊 Arquitetura do Sistema

```mermaid
graph TD
    A[Usuário] -->|Input| B(Interface Streamlit)
    B -->|Contexto| C{Agente Bia}
    C -->|Consulta| D[Base de Dados JSON]
    D -->|Retorno| C
    C -->|Resposta Validada| B
    B -->|Saída| A
