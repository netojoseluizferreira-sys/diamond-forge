# models.py
# Define a classe Livro com os métodos mágicos __str__ e __repr__.
# __str__: representação amigável para usuários (print()).
# __repr__: representação técnica para desenvolvedores (repr()).
# O uso de self.__class__.__name__ garante que a representação
# use o nome correto da classe, mesmo se subclasses forem criadas.

class Livro:
    def __init__(self, titulo: str, autor: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    # Representação amigável: "'O Codigo Da Vinci' por Dan Brown (2003)"
    def __str__(self) -> str:
        return f"'{self.titulo}' por {self.autor} ({self.ano})"

    # Representação técnica: "Livro(titulo='...', autor='...', ano=...)"
    def __repr__(self) -> str:
        # Obtém o nome da classe dinamicamente (útil para subclasses)
        cls_name = self.__class__.__name__
        return f"{cls_name}(titulo='{self.titulo}', autor='{self.autor}', ano={self.ano})"