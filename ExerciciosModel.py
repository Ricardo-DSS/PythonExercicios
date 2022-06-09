import datetime

def exercicio1():
    a = 10
    b = 20
    msg = 'Antes da troca: A {}, B = {}'.format(a,b)
    aux = a
    a = b
    b = aux
    msg = msg + '\nDepois da troca: A = {}, B = {}'.format(a,b)
    return msg

def exercicio2():
    num = int(input('Informe um número: '))
    antecessor = num - 1
    msg = 'O número anterior a {} é {}'.format(num, antecessor)
    return msg

def exercicio3():
    base = int(input('Informe o valor da base: '))
    altura = int(input('Informe o valor da altura: '))
    area = base * altura
    msg = 'A área do retângulo é {}'.format(area)
    return msg

def exercicio4():
    dia = int(input('Informe o dia do nascimento '))
    mes = int(input('Informe o mês de nascimento: '))
    ano = int(input('Informe o ano de nascimento: '))

    data = datetime.datetime.now()

    anoNow = (data.year)
    mesNow = (data.month)
    diaNow = (data.day)

    ano = (anoNow - ano) * 365
    mes = abs(mesNow - mes) * 30
    dia = (diaNow - dia)

    total = ano + mes + dia

    return total

def exercicio5():
    eleitores = float(input('Informe o número total de eleitores: '))
    brancos = float(input('Informe o número total de votos em branco: '))
    nulos = float(input('Informe o número total de votos em branco: '))
    validos = float(input('Informe o número total de votos em branco: '))

    bran = (brancos / eleitores) * 100
    nul = (nulos / eleitores) * 100
    val = (validos / eleitores) * 100

    msg = ('\nO percentual de votos brancos é {}% \nO percentual de votos nulos é {}% \nO percentual de votos válidos é {}%'.format(bran, nul, val))

    return msg

def exercicio6():
    salario = float(input('Informe o salário: '))
    ajuste = float(input('Informe o valor do reajuste em percentual: '))

    total = salario * (1 + ajuste/100)

    msg = 'O valor do salário de {} após o reajuste de {}% é de {}'.format(salario, ajuste, total)
    return msg

def exercicio7():
    custo = float(input('Informe o custo de fábrica do carro: '))
    total = custo + (custo * 0.28) + (custo * 0.45)

    msg = 'O custo final do carro para o consumidor é: {}'.format(total)

    return msg

def exercicio8():
    nota1 = float(input('Informe a 1° nota: '))
    nota2 = float(input('Informe a 2° nota: '))
    nota3 = float(input('Informe a 3° nota: '))

    media = (nota1 + nota2 + nota3) / 3

    msg = 'A média do aluno é: {}'.format(media)
    return msg

def exercicio9():
    maca = int(input('Informe a quantidade de maçãs compradas: '))

    if maca < 12:
        total = maca * 1.3
    elif maca >= 12:
        total = maca * 1

    msg = 'O valor total das maçãs é: {}'.format(total)
    return msg









