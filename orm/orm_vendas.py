from sqlalchemy import create_engine, Column, Integer, String, inspect, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

URL = "mysql+mysqlconnector://root:123456@localhost:3306/ORM"

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    CPF = Column(String(150), nullable=False)
    children_pessoa_cliente = relationship('Cliente')
    children_pessoa_vendedor = relationship('Vendedor')


class Cliente(Base):
    __tablename__ = "Cliente"
    id_cliente = Column(Integer, primary_key=True)
    children_cliente_venda = relationship('Venda')
    children_cliente_cupom = relationship('Cupom')
    cliente_id_pessoa = Column(Integer, ForeignKey('Pessoa.id_pessoa'))


class Vendedor(Base):
    __tablename__ = "Vendedor"
    id_vendedor = Column(Integer, primary_key=True)
    children_vendedor_venda = relationship('Venda')
    vendedor_id_pessoa = Column(Integer, ForeignKey('Pessoa.id_pessoa'))


class Venda(Base):
    __tablename__ = "Venda"
    id_venda = Column(Integer, primary_key=True)
    venda_id_vendedor = Column(Integer, ForeignKey('Vendedor.id_vendedor'))
    quant_produto = Column(Integer, nullable=False)
    venda_id_cliente = Column(Integer, ForeignKey("Cliente.id_cliente"))
    venda_id_mercado = Column(Integer, ForeignKey("Mercado.id_mercado"))


class Cupom(Base):
    __tablename__ = "Cupom"
    id_cupom = Column(Integer, primary_key=True)
    cupom_id_cliente = Column(Integer, ForeignKey("Cliente.id_cliente"))
    desconto = Column(Float, nullable=False)
    cupom_id_mercado = Column(Integer, ForeignKey("Mercado.id_mercado"))


class Mercado(Base):
    __tablename__ = "Mercado"
    id_mercado = Column(Integer, primary_key=True)
    nome_mercado = Column(String(150), nullable=False)
    children_mercado_venda = relationship('Venda')
    children_mercado_cupom = relationship('Cupom')
    children_mercado_eventoestoque = relationship('EventoEstoque')


class Fornecedor(Base):
    __tablename__ = "Fornecedor"
    id_fornecedor = Column(Integer, primary_key=True)
    nome_fornecedor = Column(String(150), nullable=False)
    children_fornecedor_estoque = relationship("Estoque")


class Estoque(Base):
    __tablename__ = "Estoque"
    id_estoque = Column(Integer, primary_key=True)
    quant_prod = Column(Integer, nullable=False)
    estoque_id_fornecedor = Column(Integer, ForeignKey("Fornecedor.id_fornecedor"))
    produto = Column(String(150), nullable=False)
    preco = Column(Float, nullable=False)
    children_estoque_eventoestoque = relationship("EventoEstoque")


class EventoEstoque(Base):
    __tablename__ = "EventoEstoque"
    id_eventoestoque = Column(Integer, primary_key=True)
    id_estoque = Column(Integer, ForeignKey("Estoque.id_estoque"))
    id_mercado = Column(Integer, ForeignKey("Mercado.id_mercado"))
    novo_preco = Column(Float, nullable=False)
    quant_estoque = Column(Integer, nullable=False)


class Teste(Base):
    __tablename__ = "teste"

    teste = Column(String(250), nullable=True)


def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        pessoa = Pessoa(nome='Joshua', CPF='47444179816')
        session.add(pessoa)

        def cadastra_cliente():
            cliente = Cliente(cliente_id_pessoa=1)
            session.add(cliente)

        def cadastra_vendedor():
            vendedor = Vendedor(vendedor_id_pessoa=1)
            session.add(vendedor)

        def cadastra_venda():
            venda = Venda(quant_produto=3, venda_id_vendedor=1, venda_id_cliente=1, venda_id_mercado=1)
            session.add(venda)

        cadastra_cliente()
        cadastra_vendedor()
        cadastra_venda()

        cupom = Cupom(desconto=1.00, cupom_id_cliente=1, cupom_id_mercado=1)
        session.add(cupom)

        mercado = Mercado(nome_mercado='Sempre Mais')
        session.add(mercado)

        fornecedor = Fornecedor(nome_fornecedor="Sandro")
        session.add(fornecedor)

        estoque = Estoque(quant_prod=100, produto="Banana", preco=2.00, estoque_id_fornecedor=1)
        session.add(estoque)

        estoque_evento = EventoEstoque(novo_preco=1.50, quant_estoque=99)
        session.add(estoque_evento)


if __name__ == "__main__":
    main()