class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.paginas}")
        print("-" * 30)

livros = [
    Livro("Matéria Escura", "Blake Crouch", 352),
    Livro("Renegados", "Marissa Meyer", 512),
    Livro("Rádio Silêncio", "Alice Oseman", 448),
    Livro("O Império Final", "Brandon Sanderson", 612),
    Livro("Assassinato no Expresso do Oriente", "Agatha Christie", 200)
]

for livro in livros:
    livro.detalhes()