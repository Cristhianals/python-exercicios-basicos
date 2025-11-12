# 🚀 Exercício 7 – Múltiplos de 3

Este exercício tem como objetivo praticar **loops `while` e operadores aritméticos** para gerar múltiplos de um número.  
Você vai escrever programas que exibem os **10 primeiros múltiplos de 3** ou todos múltiplos de 3 até um número definido pelo usuário.

---

## 🧩 Enunciado 7.1 – Múltiplos de 3 com Condicional

**Descrição:**  
Crie um programa que pergunte ao usuário o valor máximo (`fim`) e imprima todos os **múltiplos de 3** entre 0 e esse valor, usando **condicional `if`** dentro do loop.

Exemplo de saída se o usuário digitar `20`:

0
3
6
9
12
15
18


### 🎯 Objetivo
- Praticar **loops `while`**  
- Usar **condicional (`if`)**  
- Trabalhar com **operador módulo (%)**  

---

## 🧩 Enunciado 7.2 – Múltiplos de 3 com Incremento Inteligente

**Descrição:**  
Reescreva o programa anterior de forma mais eficiente, **incrementando a variável de 3 em 3**, sem precisar de uma condicional.

Exemplo de saída se o usuário digitar `20`:

0
3
6
9
12
15
18


### 🎯 Objetivo
- Otimizar loops usando **incremento inteligente**  
- Consolidar controle de loops para gerar **sequências específicas**  

---

## 🧩 Enunciado 7.3 – Primeiros 10 Múltiplos de 3

**Descrição:**  
Crie um programa que imprima os **10 primeiros múltiplos de 3**, começando do 3.

Exemplo de saída:

3
6
9
12
15
18
21
24
27
30


### 🎯 Objetivo
- Trabalhar com **loops controlados pelo número de iterações**  
- Combinar **incremento fixo** com contagem de elementos  
- Consolidar aprendizado sobre **sequências e múltiplos**

---

## 🔹 Dicas Extras

- Para verificar se um número é múltiplo de 3, use:
```python
if x % 3 == 0:
    print(x)
