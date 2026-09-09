senha = input('Digite sua senha: ')
pontuacao = 0

#Verifica o Tamanho
if len(senha)  >= 8:
    pontuacao += 1

# Verifica letra maiúscula
for caractere in senha:
    if caractere.isupper():
        pontuacao += 1
        break

# Verifica letra minúscula
for caractere in senha:
    if caractere.islower():
        pontuacao += 1
        break

# Verifica número
for caractere in senha:
    if caractere.isdigit():
        pontuacao += 1 
        break

# Verifica caractere especial
especiais = "!@#$%&*()-+=_"

for caractere in senha:
    if caractere in especiais:
        pontuacao += 1
        break

    # Classificação 
    if pontuacao <= 2:
        print('Força da senha: FRACA')
    elif pontuacao <= 4:
        print('Força da senha: MÉDIA')
    else:
        print('Força da senha: FORTE')

    print(f'Pontuação: {pontuacao}/5')