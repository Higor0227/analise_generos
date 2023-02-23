go = 'S'
masc = 0
fem = 0
pessoas = 0

while go == 'S':
    genero = str(input('Digite o gênero da pessoa: [M/F] ')).upper().strip()[0]
    if genero == 'M':
        masc += 1
    elif genero == 'F':
        fem += 1
    else:
        while genero not in 'MF':
            genero = str(input('Você não digitou corretamente! Digite o gênero: [M/F] ')).upper().strip()[0]
            if genero == 'M':
                masc += 1
            elif genero == 'F':
                fem += 1
            else:
                pass
    print('Dado registrado!')
    pessoas += 1
    go = str(input('Deseja continuar? [S/N] \n ')).upper().strip()[0]
print(f'São {pessoas}, dentro elas {masc} homens e {fem} mulheres')
