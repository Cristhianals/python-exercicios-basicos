# 🏠 Exercício 22 – Aprovação de Empréstimo Bancário

Escreva um programa para **aprovar o empréstimo bancário** destinado à compra de uma casa.

O programa deve perguntar:
- 💰 O valor da casa  
- 👷 O salário do comprador  
- 📆 A quantidade de **meses** para pagar  

A prestação mensal não pode ser superior a **30% do salário**.

---

### 💡 Exemplo de execução

Qual o valor da casa? 300000
Qual o seu salário? 5000
Quantos meses deseja pagar? 120

Em 120 meses a prestação será R$2500.00, que é maior que 30% do salário, não será possível realizar o empréstimo.
Recomendamos aumentar o número de meses para reduzir a parcela.


---

### 🎯 Conceitos Envolvidos

- Entrada de dados (`input`)  
- Conversão de tipos (`float`, `int`)  
- Operadores aritméticos (`/`, `*`)  
- Estruturas condicionais (`if/else`)  
- Formatação de saída (`f-strings`)  

---

### 🔍 Lógica Explicada

1. Ler o valor da casa, salário e tempo de pagamento.  
2. Calcular a prestação mensal (`valor / meses`).  
3. Determinar o valor máximo permitido (`30% do salário`).  
4. Comparar a prestação com o limite.  
5. Informar se o empréstimo é aprovado ou não e sugerir número de meses para adequar a parcela.

