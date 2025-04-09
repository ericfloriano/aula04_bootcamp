
# 💰 Calculadora de Bônus em Python

Este projeto apresenta um código Python interativo para calcular o bônus salarial de funcionários.  
O sistema foi desenvolvido com foco em **validação robusta**, **uso de type hints** e **reutilização de funções**.

---

## 📌 Funcionalidades

- ✅ Validação de nome (sem números, espaços ou caracteres especiais)
- ✅ Entrada de salário e bônus com tratamento de erros
- ✅ Cálculo do bônus com base em um KPI fixo (R$1000 + salário × bônus)
- ✅ Armazenamento dos resultados em uma lista de tuplas
- ✅ Design modular: funções reutilizáveis para importar em outros projetos

---

## 🧠 Como Funciona

### 🧩 1. Estrutura Modular

- O código é separado em funções específicas:
  - `validar_nome`
  - `solicitar_nome`
  - `solicitar_valor`
  - `calcular_bonus`
  - `executar_calculo_bonus_interativo`

### 🔄 2. Execução Interativa

- O usuário pode informar múltiplos funcionários.
- A qualquer momento pode digitar `sair` para encerrar.

### 📦 3. Importação por Outros Projetos

Se você quiser usar o cálculo de bônus em outro projeto, basta importar a função:

```python
from bonus_calculador import calcular_bonus

resultado = calcular_bonus(3000, 0.2)
print(resultado)  # saída: 1600.0
```

---

## 🧾 Código Fonte

```python
# arquivo: bonus_calculador.py
import string
from typing import Tuple, List

def validar_nome(nome: str) -> bool:
    if len(nome.strip()) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    elif any(char in string.whitespace for char in nome):
        raise ValueError("O nome não deve conter espaços.")
    elif any(char not in string.ascii_letters for char in nome):
        raise ValueError("O nome não deve conter caracteres especiais.")
    return True

def solicitar_nome() -> str:
    while True:
        nome = input("Digite seu nome (ou digite 'sair' para encerrar): ").strip()
        if nome.lower() == "sair":
            return "sair"
        try:
            if validar_nome(nome):
                print("Nome válido:", nome)
                return nome
        except ValueError as e:
            print(e)

def solicitar_valor(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Por favor, digite um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def calcular_bonus(salario: float, bonus: float) -> float:
    return 1000 + salario * bonus

def executar_calculo_bonus_interativo() -> List[Tuple[str, float, float]]:
    resultados: List[Tuple[str, float, float]] = []

    print("=== Cálculo de Bônus ===")

    while True:
        nome: str = solicitar_nome()
        if nome.lower() == "sair":
            break

        salario: float = solicitar_valor("Digite o valor do seu salário: ")
        bonus: float = solicitar_valor("Digite o valor do bônus recebido (ex: 0.1 para 10%): ")

        bonus_recebido: float = calcular_bonus(salario, bonus)
        resultados.append((nome, salario, bonus_recebido))

        print(f"\n{nome}, seu salário é R$ {salario:.2f} e seu bônus final é R$ {bonus_recebido:.2f}.\n")

    if resultados:
        print("\n=== Resumo Final dos Bônus Calculados ===")
        for nome, salario, bonus in resultados:
            print(f"{nome}: Salário R$ {salario:.2f} | Bônus R$ {bonus:.2f}")
    else:
        print("\nNenhum dado foi inserido.")

    return resultados

if __name__ == "__main__":
    executar_calculo_bonus_interativo()
```

---

## 🚀 Como Executar

1. Salve o código acima no arquivo `bonus_calculador.py`
2. Execute no terminal com:

```bash
python bonus_calculador.py
```

---

## 🔗 Licença

Este projeto é de uso livre para fins educacionais.