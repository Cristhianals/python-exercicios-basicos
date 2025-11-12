# 💳 Exercício 13 – Quitação de Dívida com Juros Mensais

Este exercício tem como objetivo praticar **cálculos financeiros usando loops**, simulando a quitação de uma dívida com pagamentos mensais e juros.  

---

## 🧩 Enunciado 13.1 – Pagamento de Dívida

**Descrição:**  
Crie um programa que pergunte ao usuário:

- O **valor inicial da dívida**  
- A **taxa de juros mensal**  
- O **valor pago mensalmente**  

O programa deve:

- Calcular **mês a mês** o saldo da dívida  
- Imprimir:
  - O **número de meses** necessário para quitar a dívida  
  - O **total pago**  
  - O **total de juros pago**  
- Considerar que, se a última parcela for menor que o valor pago, o programa deve ajustá-la corretamente  

Exemplo:

Valor da dívida: 2000
Juros mensal: 2%
Pagamento mensal: 500

A dívida será quitada em 5 meses
Total pago: R$ 2050.00
Total de juros: R$ 50.00

### 🎯 Objetivo
- Praticar **loops `while` e controle de fluxo com condições**  
- Consolidar o conceito de **acúmulo de juros**  
- Aprender a lidar com **últimas parcelas menores**  

---

## 🔹 Dicas Extras

- Evite que a dívida se torne infinita verificando se:
```python
if juros > pagamento_mensal:
    print("A dívida nunca será quitada!")
