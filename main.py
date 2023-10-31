import os
import sys

def limpar_tela():
    sistema = os.name
    if sistema == 'posix':  
        os.system('clear')
    elif sistema == 'nt':  
        os.system('cls')
    else:
        print("Sistema não suportado: Não é possível limpar a tela neste sistema.")

def main():
    id_global = 1
    while True:
        print('-' * 33 + ' MENU PRINCIPAL ' + '-' * 33)
        print('Escolha a opção desejada: ')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')
        print('3 - Remover Livro')
        print('4 - Atualizar Livro(s)')
        print('5 - Limpar Tela')
        print('6 - Sair')
        try:
            opc = int(input('Opção: '))
            print('*' * 82)
            if opc == 1:
                id_global = cadastrar_livro(id_global)
            elif opc == 2:
                consultar_livro()
            elif opc == 3:
                remover_livro()
            elif opc == 4:
                atualizar_livro()
            elif opc == 5:
                limpar_tela()
            elif opc == 5:
                sys.exit()
            else:
                print('Opção inválida.')
        except ValueError:
            print('Não aceitamos valores não numéricos.')

main()