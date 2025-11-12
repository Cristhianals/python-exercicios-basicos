# 💰 Exercício 15 – Cálculo de Troco com Notas e Moedas

Este exercício tem como objetivo criar um programa que **calcule o troco de um valor**, decompondo-o em **notas e moedas** de diferentes valores.  

---

## 🧩 Enunciado 15.1 – Contagem de Cédulas e Moedas

**Descrição:**  
Escreva um programa que pergunte ao usuário o **valor a pagar** e calcule quantas **cédulas** e **moedas** serão necessárias para totalizar esse valor, considerando as seguintes unidades:

- 💵 Notas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1  
- 🪙 Moedas de R$ 0,50, R$ 0,25, R$ 0,10 e R$ 0,05  

O programa deve:
- Exibir a quantidade de cada cédula e moeda usada.  
- Encerrar quando o usuário digitar `0` como valor a pagar.  
- Tratar valores decimais (como R$ 7,35).  

---

### 🔹 Extensões e Modificações

1. Execute o programa para os valores:  
   **5010, 745, 384, 2, 7 e 1**  
   → Observe o comportamento da decomposição.  

2. O que acontece se digitarmos **0 (zero)** como valor a pagar?  
   → O programa deve **encerrar**.  

3. Modifique o programa para **aceitar notas de R$ 100**.  

4. Permita que ele **também conte moedas** de R$ 0,01, R$ 0,02, R$ 0,05, R$ 0,10 e R$ 0,50.  

5. Teste digitando **0,0001** — se não funcionar, **corrija o problema de precisão** dos valores muito pequenos (usando arredondamento com `round()`).

---

### 🎯 Objetivos

- Trabalhar com **loops aninhados (`while` dentro de `while`)**  
- Aplicar **condicionais em cascata (`if` / `elif` / `else`)**  
- Tratar **valores monetários com ponto flutuante**  
- Evitar erros de precisão com **arredondamento**  

---

### 💡 Dicas Extras

- Sempre que trocar de unidade (ex: de R$ 10 para R$ 5), **zere o contador** de cédulas.  
- Para evitar erros como `0.0000999999`, use:
  ```python
  apagar = round(apagar, 2)
