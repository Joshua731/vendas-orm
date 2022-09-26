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

### Cliente
**Como** um Cliente, **quero** comprar os produtos que estão no projeto, **para que** o produto comprado me satisfaça.
#### Acceptance Criteria
1 - **Dado** um produto que está na minha lista de compras, **quando** ele estiver na promoção, **então** efetuo a compra do produto.
2 - **Dado** um produto que está na minha lista de compras, **quando** ele estiver fora do prazo de validade **então** procuro por outro produto.
