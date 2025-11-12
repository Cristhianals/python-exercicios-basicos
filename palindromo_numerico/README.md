# 🔁 Exercício 20 – Verificar se um Número é Palíndromo

Um número é chamado de **palíndromo** quando ele permanece o mesmo ao ter seus dígitos invertidos.  
Por exemplo:
- 454 → é palíndromo  
- 10501 → é palíndromo  
- 123 → **não é** palíndromo

---

## 🧩 Enunciado

Escreva um programa que leia um número e verifique se ele é **palíndromo**.  
O programa deve funcionar para qualquer número inteiro positivo.

O programa deve encerrar quando o usuário digitar `0`.

---

### 💡 Exemplo de execução

---

### 🎯 Conceitos Envolvidos

- **Conversão entre tipos (`int` e `str`)**
- **Laços `while`**
- **Uso de operadores aritméticos (`%`, `//`)**
- **Comparação de strings**

---

### 🔍 Lógica Explicada

1. O programa lê o número como uma string (`n`), mas também o converte para inteiro (`a`) para manipulação matemática.  
2. Enquanto `a` for maior que zero, ele extrai o **último dígito** (`a % 10`) e o adiciona à string `s`.  
3. Quando termina o laço, `s` contém o número invertido.  
4. Finalmente, o programa compara `n` e `s`.  
   - Se forem iguais → o número é palíndromo.  
   - Caso contrário → não é.

---

### 🧠 Curiosidade

Palíndromos não aparecem só em números!  
Também existem **palavras palíndromas**, como:
- “arara”
- “radar”
- “osso”

---

### ⚙️ Sugestão de Extensão

Tente adaptar o código para:
- **Verificar palavras** também (não apenas números).
- **Ignorar espaços e acentuação** em frases palíndromas, como:  
  “A base do teto desaba”.

---

