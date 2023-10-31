import os
import sys

lista_livro = []

def cadastrar_livro(id_global):
    print('-' * 30 + ' MENU CADASTRAR LIVRO ' + '-' * 30)
    print('Id do livro: {}'.format(id_global))
    nome = input('Informe o nome do livro: ')
    autor = input('Informe o autor (a) do livro: ')
    editora = input('Informe a editora (o) do livro: ')
    print('*' * 82)
    
    novo_livro = {'id': id_global, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(novo_livro)
    
    return id_global + 1 

def consultar_livro():
    while True:
        print('-' * 30 + ' MENU CONSULTAR LIVRO ' + '-' * 30)
        print('Escolha a opção desejada: ')
        print('1 - Consultar Todos os Livros')
        print('2 - Consultar Livro por id')
        print('3 - Consultar Livro(s) por autor')
        print('4 - Limpar Tela')
        print('5 - Retornar')
        try:
            opc = int(input('Opção: '))
            print('*' * 82)
            if opc == 1:
                print(lista_livro)
            elif opc == 2:
                try:
                    id_livro = int(input('Digite o id do livro: '))
                    livro_encontrado = None
                    for livro in lista_livro:
                        if livro['id'] == id_livro:
                            livro_encontrado = livro
                            break
                    if livro_encontrado is not None:
                        print(livro_encontrado)
                    else:
                        print('ID não encontrado.')
                except ValueError:
                    print('Opção inválida. Tente novamente.')
            elif opc == 3:
                try:
                    autor_livro = input('Digite o nome do autor do livro: ')
                    autor_encontrado = []
                    for livro in lista_livro:
                        if livro['autor'] == autor_livro:
                            autor_encontrado.append(livro)
                    if autor_encontrado:
                        print(autor_encontrado)
                    else:
                        print('Autor não encontrado.')
                except ValueError:
                    print('Opção inválida. Tente novamente.')
            elif opc == 4:
                limpar_tela()
            elif opc == 5:
                return
            else:
                print('Opção inválida.')
        except ValueError:
            print('Não aceitamos valores não numéricos.') 
            

def remover_livro():
    print('-' * 30 + ' MENU REMOVER LIVRO ' + '-' * 30)
    try:
        livro_removido = int(input('Digite o id do livro a ser removido: '))
        print('*' * 20)
        livro_encontrado = None
        for livro in lista_livro:
            if livro['id'] == livro_removido:
                livro_encontrado = livro
                break
        if livro_encontrado is not None:
            lista_livro.remove(livro_encontrado)
            print(f'Livro com ID {livro_removido} foi removido com sucesso.')
        else:
            print('ID não encontrado.')
    except ValueError:
        print('ID não encontrado.')

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