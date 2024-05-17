class Pedido:
    def __init__(self, id, nome, email, descricao):
        self.id = id
        self.nome = nome
        self.email = email
        self.descricao = descricao

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'descricao': self.descricao
        }
