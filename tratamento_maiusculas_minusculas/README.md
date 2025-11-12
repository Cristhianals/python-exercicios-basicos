# 🚀 Exercício 11 – Aceitando Letras Maiúsculas e Minúsculas

Este exercício tem como objetivo praticar **validação de entrada de dados**, permitindo que o usuário digite **letras maiúsculas ou minúsculas** sem afetar a lógica do programa.

---

## 🧩 Enunciado 11.1 – Sistema de Pontuação com Respostas de Letras

**Descrição:**  
Crie um programa que faça **perguntas de múltipla escolha** e registre a pontuação do usuário.  
O programa deve:

- Perguntar **3 questões**  
- Aceitar respostas **em letras maiúsculas ou minúsculas**  
- Somar **1 ponto para cada resposta correta**  

Exemplo de comportamento:

resposta da questao 1: b
resposta da questao 2: A
resposta da questao 3: c
o aluno fez 3 ponto(s)


### 🎯 Objetivo
- Aprender a **tratar strings** (`upper()`, `lower()`)  
- Praticar **loops `while` e incremento de variáveis**  
- Consolidar conceitos de **condições compostas (`or`)**

---

## 🔹 Dicas Extras

- Para tratar maiúsculas e minúsculas de forma simples:
```python
if resposta.lower() == "b":
    pontos += 1
