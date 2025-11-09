# 🧮 Exercício 16 – Menu de Tabuadas com Operações Matemáticas

Este exercício tem como objetivo praticar o uso de **repetições aninhadas (`while` dentro de `while`)** e **estruturas de menu interativas**.

---

## 🧩 Enunciado 16.1 – Tabuadas com Menu de Operações

**Descrição:**  
Crie um programa que exiba um **menu de opções** com as seguintes operações:

1️⃣ Subtração  
2️⃣ Adição  
3️⃣ Multiplicação  
4️⃣ Divisão  
0️⃣ Sair  

O programa deve:
- Exibir a **tabuada** da operação escolhida (de 1 a 10).  
- Permitir escolher **novas operações** até que o usuário digite `0`.  
- Usar **repetições aninhadas** para gerar as tabuadas.

---

### 💡 Exemplo de execução

O que deseja fazer?
1 - Subtração
2 - Adição
3 - Multiplicação
4 - Divisão
0 - Sair

Digite sua opção: 3
Tabuada de multiplicação com 5
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

Ao escolher “0”, o programa deve exibir:

---

### 🎯 Objetivos

- Consolidar o uso de **loops aninhados (`while` dentro de `while`)**  
- Praticar **menus interativos e controle de fluxo com `if / elif / else`**  
- Gerar **tabuadas dinâmicas** para múltiplas operações  
- Reforçar **organização lógica e clareza na saída do programa**

---

### 🔹 Dicas Extras

- Use uma variável de controle (`fazer`) para definir quando sair do loop principal.  
- Dentro do loop, alterne entre operações conforme a escolha do usuário:
  ```python
  if fazer == 3:
      print(f"{t} x {v} = {t * v}")
  elif fazer == 2:
      print(f"{t} + {v} = {t + v}")
