import matplotlib.pyplot as plt
import numpy as np

class Book:
    def __init__(self, title, author, genre, amount):
        self.title = title
        self.author = author
        self.genre = genre
        self.amount = amount

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
    
def graphic():
    print('')
    print('Preparando o gráfico...')
    series = {}
    for book in books:
        if book.genre in series:
            series[book.genre] += book.amount
        else:
            series[book.genre] = book.amount
    print(series)
    plt.bar(series.keys(), series.values())
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()