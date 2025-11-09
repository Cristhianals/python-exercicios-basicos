# 🚀 Exercício 9 – Multiplicação Usando Apenas Soma

Este exercício tem como objetivo praticar **lógica algorítmica**, implementando a multiplicação de dois números **apenas com soma**, sem usar o operador `*`.

---

## 🧩 Enunciado 9.1 – Multiplicação por Soma Sucessiva

**Descrição:**  
Crie um programa que leia dois números do usuário e calcule a multiplicação do primeiro pelo segundo **somando o primeiro número várias vezes**.  

Por exemplo:

4 * 5 = 4 + 4 + 4 + 4 + 4 = 20


### 🎯 Objetivo
- Entender **multiplicação como soma repetida**  
- Praticar **loops `while`**  
- Trabalhar com **variáveis auxiliares e controle de contagem**

---

## 🧩 Enunciado 9.2 – Formato de Saída Detalhado

**Descrição:**  
Modifique o programa para imprimir o resultado no formato:

4 multiplicado por 5 é 20


Certifique-se de **não usar o operador `*`**, apenas **soma** dentro de um loop.

### 🎯 Objetivo
- Consolidar **loops controlados por contador**  
- Aprimorar **formatação de saída com f-strings**  
- Reforçar **entendimento da multiplicação como soma repetida**

---

## 🔹 Dicas Extras

- Use uma **variável auxiliar** para armazenar o resultado da soma:
```python
resultado = 0
for i in range(vezes):
    resultado += numero
