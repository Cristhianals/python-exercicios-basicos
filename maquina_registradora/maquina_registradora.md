# 🛒 Exercício 14 – Máquina Registradora

Este exercício tem como objetivo criar um programa que simule uma **pequena máquina registradora**, controlando a compra de produtos por código.

---

## 🧩 Enunciado 14.1 – Controle de Produtos

**Descrição:**  

- O programa deve solicitar ao usuário:
  - O **código do produto**  
  - A **quantidade comprada**  
- Utilize a tabela de códigos abaixo para obter o preço de cada produto:

| Código | Produto | Preço (R$) |
|--------|---------|------------|
| 1      | Produto A | 0,50      |
| 2      | Produto B | 1,00      |
| 3      | Produto C | 4,00      |
| 4      | Produto D | 7,00      |
| 5      | Produto E | 8,00      |

- O programa deve **exibir o total das compras** quando o usuário digitar `0`.  
- Qualquer outro código deve gerar a mensagem de erro: `"código inválido"`.

---

### 🎯 Objetivo
- Praticar **loops `while` e condicionais `if/elif/else`**  
- Acumular valores para calcular o **total da compra**  
- Validar entradas do usuário  

---

### 💡 Exemplo de execução

Os códigos dos produtos são 1, 2, 3, 4 e 5

Digite o código do produto (0 para sair): 1
Digite a quantidade: 3
Digite o código do produto (0 para sair): 2
Digite a quantidade: 2
Digite o código do produto (0 para sair): 6
Código inválido!
Digite o código do produto (0 para sair): 0

O total da compra foi de R$ 3,50

---

### 🔹 Dicas Extras

- Use uma variável `s` para acumular o **total da compra**.  
- Cada código válido deve **somar ao total** o valor correspondente à quantidade comprada.  
- Qualquer código fora do intervalo válido deve disparar a mensagem de **erro**.
