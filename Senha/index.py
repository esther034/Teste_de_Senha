print('='*30)
print('     VERIFICADOR DE SENHA')
print('='*30)

senhas_comuns = [
    '123456',
    '12345678',
    'password',
    'qwerty',
    'admin',
]

while True:

    senha = input('\nDigite sua senha: ')

    pontuacao = 0

    # Tamanho
    if len(senha) >= 8:
        pontuacao += 1
        print('✔️ Possui 8 ou mais caracteres')
    else:
        print('✖️ Possui menos de 8 caracteres')

    # Maiúscula
    tem_maiuscula = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
            break

    if tem_maiuscula:
        pontuacao += 1
        print('✔️ Possui letra maiúscula')
    else:
        print('✖️ Não possui letra maiúscula')

    # Minúscula
    tem_maiuscula = False
    
    for caractere in senha:
         if caractere.islower():
            tem_maiuscula = True
            break
    
    if tem_maiuscula:
         pontuacao += 1
         print('✔️ Possui letra minúscula')
    else:
        print('✖️ Não possui letra minuscula')

    # Número
    tem_numero = False
    
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break
    
    if tem_numero:
         pontuacao += 1
         print('✔️ Possui número')
    else:
        print('✖️ Não possui número')

    # Caractere especial
    especiais = '!@#$%&*()-_=+'
    tem_especial = False

    for caractere in senha:
        if caractere in especiais:
            tem_especial = True
            break

    if tem_especial:
        pontuacao += 1
        print('✔️ Possui caractere especial')
    else:
        print('✖️ Não possui caractere especial')

    # Verificação de senha comum
    if senha.lower() in senhas_comuns:
        print('⚠️ ATENÇÃO: essa senha é muito comum')

    # Resultado 
    print('\n='*30)
    print('           RESULTADO')
    print('='*30)

    print(f'Pontuação: {pontuacao}/5')

    if pontuacao <= 2:
        print('Força: FRACA')
        print('Dica: tente adicionar letras,números e símbolos.')

    elif pontuacao <= 4:
        print('Força: MÉDIA')
        print('Dica: sua senha pode ser melhorada.')

    else:
        print('Força: FORTE')
        print('Sua senha atende aos critérios básicos.')

    continuar = input('\nDeseja tentar outra senha? (s/n): ')

    if continuar.lower() != 's':
        print('\nPrograma encerrado.')
        break

        

    








