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

# Execução direta
if __name__ == "__main__":
    executar_calculo_bonus_interativo()
