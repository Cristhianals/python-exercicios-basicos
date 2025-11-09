# 🚀 Exercício 8 – Tabuada com Loops Aninhados

Este exercício tem como objetivo praticar **loops aninhados (`while` dentro de `while`)** e a **formatação de saída**, criando um programa que imprime a tabuada de 1 até 10 de forma organizada.

---

## 🧩 Enunciado 8.1 – Tabuada Completa

**Descrição:**  
Crie um programa que exiba a tabuada do 1 até 10 no seguinte formato:

Tabuada do 1
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10

Tabuada do 2
2 x 1 = 2
...
2 x 10 = 20


O programa deve usar **loops aninhados (`while`)** para percorrer os números da tabuada e os multiplicadores.

### 🎯 Objetivo
- Praticar **loops aninhados**  
- Aprender a **formatar saídas** com `print`  
- Consolidar o uso de **incrementos e controle de variáveis**  

---

## 🧩 Enunciado 8.2 – Tabuada com Variável Única de Controle

**Descrição:**  
Reescreva o programa anterior usando **uma única variável de controle externa**, ajustando os multiplicadores dentro do loop principal para simplificar o código, mas mantendo o mesmo formato de saída.

### 🎯 Objetivo
- Explorar diferentes formas de organizar **loops aninhados**  
- Treinar **controle de fluxo** e **reutilização de variáveis**  
- Aprimorar a **legibilidade do código**

---

## 🔹 Dicas Extras

- Para formatar a saída, use **f-strings** do Python:
```python
print(f"{tabuada} x {numero} = {tabuada * numero}")
