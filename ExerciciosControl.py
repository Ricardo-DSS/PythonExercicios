import this
import ExerciciosModel
this.opcao = -1

def menu():
    print('Menu\n\n' +
          '\n1. Exercício 1' +
          '\n2. Exercício 2' +
          '\n3. Exercício 3' +
          '\n4. Exercício 4' +
          '\n5. Exercício 5' +
          '\n6. Exercício 6' +
          '\n7. Exercício 7' +
          '\n8. Exercício 8' +
          '\n9. Exercício 9' +
          '\n10. Exercício 10' +
          '\n0. Sair' +
          '\n\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def executar():
    while this.opcao != 0:
        menu()
        if this.opcao == 0:
            print('Obrigado')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio1())
        elif this.opcao == 2:
            print(ExerciciosModel.exercicio2())
        elif this.opcao == 3:
            print(ExerciciosModel.exercicio3())
        elif this.opcao == 4:
            print(ExerciciosModel.exercicio4())
        elif this.opcao == 5:
            print(ExerciciosModel.exercicio5())
        elif this.opcao == 6:
            print(ExerciciosModel.exercicio6())
        elif this.opcao == 7:
            print(ExerciciosModel.exercicio7())
        elif this.opcao == 8:
            print(ExerciciosModel.exercicio8())
        elif this.opcao == 9:
            print(ExerciciosModel.exercicio9())
        else:
            print('Opção informada não é válida!')
