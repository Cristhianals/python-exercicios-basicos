# 🚀 Exercício 10 – Divisão Inteira Usando Apenas Soma e Subtração

Este exercício tem como objetivo praticar **lógica algorítmica**, implementando a **divisão inteira de dois números** sem usar o operador `/`.  
A ideia é entender a divisão como **quantas vezes podemos subtrair o divisor do dividendo**.

---

## 🧩 Enunciado 10.1 – Divisão Inteira com Subtração

**Descrição:**  
Crie um programa que leia dois números do usuário (`dividendo` e `divisor`) e calcule:

- O **quociente inteiro**  
- O **resto da divisão**

**Regras:**
- Não use o operador `/` ou `%`  
- Utilize apenas **loops `while` e operadores de soma/subtração**  

Exemplo:

20 dividido por 4 é: 5 e a sobra é 0


### 🎯 Objetivo
- Compreender a **divisão como subtração repetida**  
- Praticar **loops controlados por contador**  
- Consolidar o uso de **variáveis auxiliares**  

---

## 🧩 Enunciado 10.2 – Controle de Entrada

**Descrição:**  
Implemente um loop principal que permita ao usuário **realizar várias divisões**, até que ele digite `0` como dividendo para sair.  
Caso o divisor seja `0`, o programa deve exibir uma mensagem de **erro** sem encerrar o loop.

### 🎯 Objetivo
- Treinar **controle de fluxo com `while True` e `break`**  
- Reforçar boas práticas de **validação de entrada**  
- Consolidar compreensão de **loops e condições aninhadas**  

---

## 🔹 Dicas Extras

- Use **uma variável acumuladora** para somar o divisor até alcançar o dividendo:
```python
acumulado = 0
contador = 0
while acumulado + divisor <= dividendo:
    acumulado += divisor
    contador += 1
