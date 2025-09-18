class Book:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

books = []

def populate():
    print('Inicializando com alguns livros cadastrados...')
    books.append(Book('A Cirurgiã', 'Leslie Wolfe', 'Suspense', 2))
    books.append(Book('O Assasinato no verão de 1999', 'Jeneva Rose', 'Suspense', 3))
    books.append(Book('Arrume Sua Cama', 'William H. McRaven', 'Auto Ajuda', 1))
    books.append(Book('O Espelho do Homem Morto', 'Agatha Christie', 'Suspense', 3))
    books.append(Book('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Fantasia', 2))
    books.append(Book('O Alienista', 'Machado de Assis', 'Ficção', 4))
    books.append(Book('Eu, Robô', 'Issac Asimov', 'Ficção', 1))
    books.append(Book('Python', 'Daniel Correa', 'Tecnologia', 2))
    books.append(Book('Unleashed C', 'Martin Bob', 'Tecnologia', 2))


def add():
    print('')
    print('Cadastrar um novo livro. por favor:')
    titulo = input('Informe o título....: ')
    autor = input('Informe o autor.....: ')
    genero = input('Informe o gênero....: ')
    quantidade = int(input('Informe a quantidade: '))
    book = Book(titulo, autor, genero, quantidade)
    books.append(book)
    print('Livro cadastrado')

def _show(books): 
    books.sort(key=lambda b: b.titulo)
    print('')
    print('"Título","Autor","Gênero",Quantidade')
    for book in books:
        print(f'"{book.titulo}","{book.autor}","{book.genero}",{book.quantidade}')

def show():
    _show(books)

def locate():
    print('')
    titulo = input('Informe o título para localizar:')
    filtered = list(filter(lambda b: titulo.lower() in b.titulo.lower(), books))
    if len(filtered) == 0:
        print('Nenhum livro encontrado...')
    else:
        _show(filtered)
    
    