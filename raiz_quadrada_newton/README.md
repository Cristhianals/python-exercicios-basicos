# 🧠 Exercício 18 – Raiz Quadrada pelo Método de Newton

Este exercício aplica o **método de Newton-Raphson** para calcular a **raiz quadrada aproximada** de um número.  
O objetivo é usar **iterações sucessivas** para obter um resultado cada vez mais preciso.

---

## 🧩 Enunciado 18.1 – Cálculo da Raiz Quadrada

**Descrição:**  
Escreva um programa que calcule a **raiz quadrada** de um número usando o **método de Newton**.

- Seja `n` o número cuja raiz quadrada queremos obter.  
- Comece com uma **estimativa inicial** `b = 2`.  
- Calcule uma nova aproximação `p` com a fórmula:

\[
p = \frac{b + (n / b)}{2}
\]

- Em seguida, calcule o quadrado de `p`.  
- A cada passo, faça `b = p` e recalcule `p` com a mesma fórmula.  
- O processo termina quando a **diferença absoluta** entre `n` e `p²` for menor que `0.0001`.

---

### 💡 Exemplo de execução

Digite um número e diremos sua raiz quadrada (0 para sair): 9
Na 1ª iteração, aproximação atual da raiz: 2.250000 → p² = 5.0625
Na 2ª iteração, aproximação atual da raiz: 3.004166 → p² = 9.0250
Na 3ª iteração, aproximação atual da raiz: 3.000006 → p² = 9.0000

Resultado:  
A raiz quadrada aproximada de 9 é **3.000006**

---

### 🎯 Objetivos

- Aplicar **iterações sucessivas com aproximação numérica**  
- Compreender o funcionamento do **método de Newton-Raphson**  
- Trabalhar com **erros absolutos e tolerância de precisão** (`< 0.0001`)  
- Reforçar controle de loops e variáveis de atualização

---

### 🔹 Dicas Extras

- Use `abs()` para calcular o **valor absoluto** da diferença:
  ```python
  if abs(a - n) < 0.0001:
      break
