import sys
import book

def menu() -> int:
    print('')
    print('---------------------')
    print('1 - Cadastrar livro')
    print('2 - Listar livros')
    print('3 - Localizar livro')
    print('4 - Grafico de quantidade por gênero')
    print('0 - Sair')
    try:
        option = int(input('Informe a opção: '))
    except ValueError:
        option = -1
    return option

def main() -> int:
    book.populate()
    while True:
        option = menu()
        match option:
            case 1:
                book.add()
            case 2:
                book.show()
            case 3:
                book.locate()
            case 4:
                book.graphic()
            case 0:
                break
    return 0

if __name__ == '__main__':
    sys.exit(main())