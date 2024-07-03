# usar type hint nas variáveis, usar funções e dicionários

BONUS: int = 1000
nome_valido: bool = False
bonus_valido: bool = False
salario_valido: bool = False

# 1) Solicita ao usuário que digite seu nome
while nome_valido == False:
    try:
        nome_usuario: str = input("Informe seu nome: ")
        if len(nome_usuario) == 0:
            raise ValueError("O nome não pode estar vazio")
            exit()
        elif any(char.isdigit() for char in nome_usuario):
            raise ValueError("O nome não pode conter números.")
        else:
            nome_valido = True

    except ValueError as e:
        print(e)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
while salario_valido == False:
    try:
        salario_usuario: float = float(input("Informe seu salario: "))
        if salario_usuario < 0:
            raise ValueError("Informe um valor válido para o salário")
        else:
            salario_valido = True
    except ValueError as e:
        print("Entrada inválida, digite um valor numérico")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
while bonus_valido == False:
    try:
        bonus_usuário: float = float(input("Informe seu bonus: "))
        if bonus_usuário < 0:
            raise ValueError("Informe um valor válido para o bonus")
        else:
            bonus_valido = True
    except ValueError as e:
        print("Entrada inválida, informe um valor numérico")

# 4) Calcule o valor do bônus final
valor_bonus_calculado: float = BONUS + salario_usuario * bonus_usuário

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá, {nome_usuario}, seu salário com o bonus será de R${valor_bonus_calculado}")
