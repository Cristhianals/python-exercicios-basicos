# ➗ Exercício 19 – Resto da Divisão Usando Soma e Subtração

Este exercício tem como objetivo **simular a operação de divisão inteira** e calcular o **resto da divisão**, utilizando apenas **soma e subtração**.

---

## 🧩 Enunciado 19.1 – Cálculo do Resto da Divisão

**Descrição:**  
Escreva um programa que leia dois números inteiros e calcule o **resto da divisão inteira** entre eles.  

Regras:
- Não use os operadores `/`, `//` ou `%`.  
- Use apenas **soma e subtração** para chegar ao resultado.  
- Se o **dividendo for menor que o divisor**, o programa deve lidar com isso de forma apropriada.

---

### 💡 Exemplo de execução

Digite o dividendo: 10
Digite o divisor: 3
O resto da divisão é 1

Caso o dividendo seja menor:

Digite o dividendo: 2
Digite o divisor: 5
O dividendo é menor que o divisor.
Resto = 2

---

### 🎯 Objetivos

- Reforçar o entendimento da **divisão como subtrações sucessivas**  
- Aplicar **loops e condicionais** para simular uma operação matemática  
- Compreender o papel do **resto** e como ele surge da diferença entre dividendos e divisores

---

### 🔹 Dicas Extras

- A lógica central pode ser expressa assim:
  ```python
  while dividendo >= divisor:
      dividendo -= divisor
  resto = dividendo
