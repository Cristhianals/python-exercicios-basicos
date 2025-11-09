# 🔢 Exercício 17 – Verificação e Geração de Números Primos

Este exercício tem como objetivo praticar **divisões sucessivas, controle de repetição e raciocínio lógico matemático** para identificar números primos.

---

## 🧩 Enunciado 17.1 – Verificar se um Número é Primo

**Descrição:**  
Escreva um programa que leia um número e verifique se ele é ou não **número primo**.  

Para isso:
- Calcule o **resto da divisão** do número por 2, e depois por todos os **números ímpares até o valor lido**.  
- Se algum resto da divisão for igual a zero, o número **não é primo**.  
- Considere:
  - 0 e 1 **não são primos**
  - 2 é o **único número primo par**

O programa deve continuar executando até que o usuário digite `0`.

---

## 🧩 Enunciado 17.2 – Imprimir os N Primeiros Números Primos

**Descrição:**  
Modifique o programa anterior para:
- Ler um número `n`
- Imprimir os **n primeiros números primos**

---

### 💡 Exemplo de execução

Digite um número (0 para sair): 5
O número 5 é primo

Digite um número (0 para sair): 8
O número 8 não é primo

Digite um número (0 para sair): 0
Saindo...

E para o segundo programa:

Digite quantos números primos deseja ver: 5
2 3 5 7 11
---

### 🎯 Objetivos

- Compreender o conceito de **número primo**
- Usar **loops e condicionais** para testar divisibilidade
- Aprender a **interromper loops** com `break`
- Aplicar **repetições aninhadas** para gerar sequências de primos

---

### 🔹 Dicas Extras

- Para o teste de primalidade:
  ```python
  primo = True
  for i in range(2, n):
      if n % i == 0:
          primo = False
          break


