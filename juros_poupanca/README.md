# 🚀 Exercício 12 – Juros de Poupança e Depósitos Mensais

Este exercício tem como objetivo praticar **cálculo de juros compostos** usando loops, além de trabalhar com **entradas iterativas do usuário**.

---

## 🧩 Enunciado 12.1 – Juros de Poupança Simples

**Descrição:**  
Crie um programa que pergunte ao usuário:

- O **depósito inicial**  
- A **taxa de juros mensal**

O programa deve:

- Exibir o **saldo mês a mês** para os **24 primeiros meses**  
- Exibir o **total de ganho com juros** ao final do período

Exemplo:

Mês 1: saldo = 1050.00, rendimento = 50.00
...
Mês 24: saldo = 12345.67, rendimento = 2345.67
Total ganho: 2345.67


### 🎯 Objetivo
- Praticar **loops `while` e cálculos acumulativos**  
- Entender o conceito de **juros compostos**  
- Consolidar **formatação de saída com f-strings**

---

## 🧩 Enunciado 12.2 – Juros com Depósitos Mensais Adicionais

**Descrição:**  
Altere o programa para perguntar também:

- O **valor depositado mensalmente**  

Regras:

- Este valor será **depositado no início de cada mês**  
- O cálculo dos juros deve **considerar este depósito para o mês seguinte**  
- Exibir mês a mês e o total de ganho ao final

### 🎯 Objetivo
- Trabalhar com **entrada iterativa dentro de loops**  
- Consolidar conceito de **juros sobre capital acumulado**  
- Praticar **organização de variáveis e lógica de cálculos financeiros**

---

## 🔹 Dicas Extras

- Utilize variáveis separadas para:
  - **capital inicial**  
  - **saldo acumulado**  
  - **rendimento total**  

- Exemplo de cálculo de juros:
```python
saldo = saldo + (saldo * taxa / 100)
