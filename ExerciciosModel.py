import datetime
import this

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
    dia = abs(diaNow - dia)

    total = ano + mes + dia

    msg = 'Você tem {} dias de vida'.format(total)
    return msg

def exercicio5():
    eleitores = float(input('Informe o número total de eleitores: '))
    brancos = float(input('Informe o número total de votos em branco: '))
    nulos = float(input('Informe o número total de votos em branco: '))
    validos = float(input('Informe o número total de votos em branco: '))

    soma = brancos + nulos + validos

    if soma == eleitores:
        bran = (brancos / eleitores) * 100
        nul = (nulos / eleitores) * 100
        val = (validos / eleitores) * 100

        msg = ('\nO percentual de votos brancos é {}% \nO percentual de votos nulos é {}% \nO percentual de votos válidos é {}%'.format(bran, nul, val))
        return msg
    elif soma != eleitores:
        msg = 'As quantidades de votos brancos, nulos e validos somados não condizem com a quantidade de eleitores!'
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
        msg = 'O valor total das maçãs é: {}'.format(total)
        return msg
    elif maca >= 12:
        total = maca * 1
        msg = 'O valor total das maçãs é: {}'.format(total)
        return msg

def exercicio10():
    numeros = []
    for i in range(0,10):
        valor = int(input('Informe o {}º valor: '.format(i+1)))
        numeros.append(valor)
    numeros.sort()
    print('Os números em ordem são:')
    return numeros

def exercicio11():
    salario = float(input('Informe o valor do seu salário: '))
    vendas = float(input('Informe o valor das vendas: '))

    if vendas < 1500:
        salario = salario + (0.03 * vendas)
        msg = 'O seu salário este mês é R$ {}'.format(salario)
        return msg
    elif vendas > 1500:
        vendasParcial = (vendas - 1500) * 0.05
        salario = salario + vendasParcial + (1500 * 0.03)
        msg = 'O seu salário este mês é R$ {}'.format(salario)
        return msg

def exercicio12():
    nConta = int(input('Informe o número da conta: '))
    saldo = float(input('Informe o saldo atual da conta: '))
    debito = float(input('Informe o debito atual da conta: '))
    credito = float(input('Informe o valor atual do crédito: '))

    saldoAtual = saldo - debito + credito

    if saldoAtual < 0:
        msg = 'A conta {}, está com saldo negativo'.format(nConta)
        return msg
    elif saldoAtual > 0:
        msg = 'A conta {}, está com saldo positivo'.format(nConta)
        return msg

def exercicio13():
    n = int(input('Informe um número: '))

    while (n > 10) and (n < 1):
        print('Selecione um valor válido entre 1 e 10')

    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, (n*i)))

def exercicio14():
    n = int(input('Informe um valor: '))
    numeros = []
    i = 0
    while n < 0:
        n = int(input('Escreva um valor válido, isto é, maior do que 1: '))

    for i in range(1, n+1):
        numeros.append(i)

    msg = 'Os números entre 1 e {} é: {}'.format(n, numeros)
    return msg

def exercicio15():
    lista = []
    negativo = 0

    for i in range(1, 11):
        num = int(input('Informe o {}° número: '.format(i)))
        lista.append(num)
        if num < 0:
            negativo += 1

    msg = 'Entre os números listados há {} valores negativos'.format(negativo)
    return msg

def exercicio16():
    lista = []
    soma = 0

    for i in range(1, 11):
        num = int(input('Informe o {}° número: '.format(i)))
        lista.append(num)
        if num < 40:
            soma += num

    msg = 'Entre os números informados, a soma dos valores abaixo de 40 é: {}'.format(soma)
    return msg

def exercicio17():
    soma = 0
    for i in range(15, 101):
        soma += i
    media = soma / 85

    msg = 'A média aritmética dos números entre 15 e 100 é {}'.format(media)
    return msg

def exercicio18():
    n = int(input('Informe o valor de números a serem lidos: '))
    lista = []
    soma = 0

    for i in range(1, n+1):
        num = int(input('Informe o {}° número'.format(i)))
        lista.append(num)
        soma += num

    media = soma / n
    lista.sort()
    print('O maior número entre os digitados é: {}'.format(lista[n-1]))
    print('A média é: {}'.format(media))

def exercicio19():
    lista = []
    somaNota = 0
    qtdAlunos = 0
    for i in range(1, 21):
        nota = float(input('Informe a {}ª nota:'.format(i)))
        lista.append(nota)
        somaNota += nota
    media = somaNota / 20
    for i in range(1, len(lista)):
        if lista[i] > media:
            qtdAlunos += 1

    msg = 'A média de notas da turma foi de {} e a quantidade de alunos acima da média foi de {}'.format(media, qtdAlunos)
    return msg

def exercicio20():
    maiorSalario = []
    continuar = 1
    populacao = 0
    contSmallSalary = 0
    valorSalario = 0
    numeroFilhos = 0

    while continuar == 1:
        salario = float(input('Informe o seu salário: '))
        nFilhos = int(input('Informe o número de filhos: '))

        maiorSalario.append(salario)
        numeroFilhos += nFilhos
        valorSalario += salario
        populacao += 1

        continuar = int(input('Deseja coletar mais dados? (1 = SIM) (Qualquer tecla = NÃO): '))

    mediaSalario = valorSalario / populacao
    mediaFilhos = numeroFilhos / populacao
    maiorSalario.sort()
    maior = maiorSalario[populacao-1]

    for i in range(1, len(maiorSalario)):
        if maiorSalario[i] < 150:
            contSmallSalary += 1

    percentual = (contSmallSalary / populacao) * 100

    msg = 'A média salarial é R$ {} \nA média de filhos é: {} \nO maior salário foi de RS {} \nO percentual da população com salário menor do que 150 foi de {}%'.format(mediaSalario, mediaFilhos, maior, percentual)
    return msg













