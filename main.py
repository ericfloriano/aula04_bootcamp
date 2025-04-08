import string

# Inicialização das variáveis de controle
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

# Declaração de variáveis com tipo
nome: str
salario: float
bonus: float
bonus_recebido: float

# Solicita ao usuário que digite seu nome
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        
        if len(nome.strip()) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        elif any(char in string.whitespace for char in nome):
            raise ValueError("O nome não deve conter espaços.")
        elif any(char not in string.ascii_letters for char in nome):
            raise ValueError("O nome não deve conter caracteres especiais.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do salário
while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus
while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido (ex: 0.1 para 10%): "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

# Cálculo do bônus recebido
bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# Exibe resultado final
print(f"\n{nome}, seu salário é R$ {salario:.2f} e seu bônus final é R$ {bonus_recebido:.2f}.")
