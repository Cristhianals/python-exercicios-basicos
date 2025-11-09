# 🚀 Exercício 6 – Imprimindo Apenas Números Ímpares

Este exercício tem como objetivo praticar **loops `while` e seleção de números com operadores aritméticos**.  
Você vai escrever programas que exibem apenas os números ímpares de 1 até um valor definido pelo usuário, explorando diferentes formas de implementar a lógica.

---

## 🧩 Enunciado 6.1 – Números Ímpares com Condicional

**Descrição:**  
Crie um programa que pergunte ao usuário qual será o último número a ser exibido e imprima **apenas os números ímpares** entre 0 e esse número.  
Use o operador `%` para identificar os ímpares.

Exemplo de saída se o usuário digitar `10`:

1
3
5
7
9


### 🎯 Objetivo
- Praticar **loops `while`**  
- Usar **condicionais (`if`) dentro do loop**  
- Trabalhar com **operadores aritméticos (`%`)**  

---

## 🧩 Enunciado 6.2 – Números Ímpares com Incremento Inteligente

**Descrição:**  
Reescreva o programa anterior de forma mais simples, **começando do 1 e incrementando de 2 em 2**, evitando a necessidade de verificar se o número é ímpar.

Exemplo de saída se o usuário digitar `10`:

1
3
5
7
9


### 🎯 Objetivo
- Aprender a **otimizar código**  
- Usar **incremento inteligente** para gerar apenas os números desejados  
- Consolidar o uso de **loops `while` controlados pelo usuário**  

---

## 🔹 Dicas Extras

- Para verificar se um número é ímpar, você pode usar:
```python
if x % 2 != 0:
    print(x)
