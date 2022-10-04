# Vendas-orm
Um sistema de vendas baseado nas técnicas de mapeamento objeto-relacional
## Conceito
**Vendas-orm** é um projeto que manipula o controle de um **supermercado** (vendas, compras, estoque, clientes, etc.) armazenando seus dados em um **banco de dados** por intermédio da linguagem **Python**, usando a técnica **ORM** (Mapeamento Objeto-Relacional). 

A biblioteca ORM utilizada em Python se chama **sqlalchemy**, tendo ela várias utilidades no quesito banco de dados. O SGDB (Sistema Gerenciador de Banco de Dados) utilizado é o **MySQL**, que interage com a linguagem **SQL**.

Dentro do projeto, os envolvidos são o **Cliente**, o **Vendedor** e o **Fornecedor**, cada um com uma **User Story**.

## User Stories
### Vendedor
**Como** um Vendedor, **quero** registrar os meus produtos no projeto, **para que** o Cliente possa ver e comprar um produto registrado.
#### Acceptance Criteria
**Dado** um produto não registrado, **quando** se obter um estoque suficiente para venda, **então** é realizado o seu registro no projeto.
#### Definition of Done
Possibilidade de cadastrar o produto dentro do código do projeto
Possibilidade de ver o produto cadastro dentro das tabelas do SGBD

### Cliente
**Como** um Cliente, **quero** comprar os produtos que estão no projeto, **para que** o produto comprado me satisfaça.
#### Acceptance Criteria
1 - **Dado** um produto **quando** ele estiver cadastrado no projeto, **então** efetuo a compra do produto.
#### Definition of Done
Possibilidade de se cadastrar no sistema do projeto
Possibilidade de comprar um produto que está registrado no SGBD do projeto

### Fornecedor
**Como** um Fornecedor, **quero** adicionar e visualizar meus produtos ao estoque **para que** eu possa ter a certeza de que eles estão da forma que os adicionei
#### Acceptance Criteria
**Dado** um cliente-vendedor **quando** estiver com o estoque vazio **então** registrarei os meus produtos no estoque
#### Definition of Done
Possibilidade de registrar o produto no estoque
Possibilidade de visualizar o produto registrado no estoque dentro do SGBD

## Modelo Relacional do Projeto (Imagem)
![MER vendas-orm2](https://user-images.githubusercontent.com/88397658/193477780-b20b1bf9-d4b8-4b2f-9c75-9782074a1530.jpg)

## Diagrama de Classes do projeto (Imagem)
![uml orm vendas](https://user-images.githubusercontent.com/88397658/193490999-6a08a9a9-9f33-41e4-a420-80a56e1ae831.png)


