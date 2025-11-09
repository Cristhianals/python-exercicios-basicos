# ⚡ Exercício – Cálculo do Preço da Energia Elétrica

O programa calcula o **preço a pagar pela energia elétrica**, considerando o **tipo de instalação** e o **consumo em kWh**, com tarifas diferentes para residencial, comercial e industrial.

---

## 🧩 Enunciado

Escreva um programa que:

1. Pergunte a quantidade de **kWh consumida**.  
2. Pergunte o **tipo de instalação**:  
   - `R` → Residencial  
   - `C` → Comercial  
   - `I` → Industrial  
3. Calcule o **preço a pagar** de acordo com a tabela:

| Tipo | Até (kWh) | Tarifa (R$) | Acima (kWh) | Tarifa (R$) |
|------|-----------|-------------|------------|-------------|
| R    | 500       | 0,40        | >500       | 0,65        |
| C    | 1000      | 0,55        | >1000      | 0,60        |
| I    | 5000      | 0,55        | >5000      | 0,60        |

---

### 💡 Exemplo de execução

Qual a quantidade de kWh consumida? 600
Qual o tipo de instalação? R

O preço a pagar pelo consumo de energia é R$390,00


---

### 🎯 Conceitos Envolvidos

- Entrada de dados (`input`)  
- Conversão de tipos (`int`, `str`)  
- Estruturas condicionais (`if/elif/else`)  
- Operadores aritméticos (`*`)  
- Formatação de saída (`f-strings`)  

---

### 🔍 Lógica Explicada

1. Ler o consumo e o tipo de instalação.  
2. Verificar a faixa de consumo de acordo com o tipo.  
3. Aplicar a tarifa correspondente.  
4. Exibir o valor total a pagar.