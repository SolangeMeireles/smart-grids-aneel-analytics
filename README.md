# Smart Grids ANEEL Analytics ⚡📊

Um framework desenvolvido em Python para automação de auditoria preditiva e análise de conformidade de prazos em projetos elétricos de distribuição, em total alinhamento com a **Resolução Normativa nº 1.000/2021 da ANEEL**.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é mitigar riscos operacionais e financeiros no setor de distribuição de energia utilizando conceitos de **Engenharia 4.0**. A automação substitui a verificação manual de prazos regulatórios por um pipeline de dados ágil, capaz de identificar gargalos e emitir relatórios de alertas instantâneos para a gerência sobre projetos com prazos críticos ou estourados.

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.14+
* **Biblioteca de Análise de Dados:** Pandas
* **Ambiente de Desenvolvimento:** Visual Studio Code (VS Code)

## 📁 Estrutura do Repositório

```text
smart-grids-aneel-analytics/
│
├── data/
│   └── projetos_teste.csv       # Base de dados com o histórico dos projetos elétricos
│
├── src/
│   └── aneel_analytic.py        # Script principal com as regras de negócio e validações
│
├── outputs/
│   └── alertas_auditoria.csv    # Relatório gerado automaticamente com os projetos críticos
│
└── README.md                    # Documentação do repositório