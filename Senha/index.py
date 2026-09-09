senha = input('Digite sua senha: ')
pontuacao = 0

#Verifica o Tamanho
if len(senha)  >= 8:
    pontuacao += 1

# Verifica letra maiúscula
for caractere in senha:
    if caractere.islower():
        pontuacao += 1
        break

# Verifica letra minúscula
for caractere in senha:
    if caractere.isdigit():
        pontuacao += 1
        break

# Verifica 


