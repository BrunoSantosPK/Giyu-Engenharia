# Giyu: Sistema para Gestão de Projetos de Engenharia e Controle de Orçamentos
*Esta documentação ainda está em construção, uma vez que feedbacks estão sendo coletados ao longo da execução. Ferramentas, assinaturas e demais pontos menores podem sofrer alteração. Quando finalizado, este aviso será removido.*

## Apresentação

Dentro da engenharia, sobretudo em projetos de construção, o controle das etapas, dos materiais, da mão de obra e, principalmente, dos custos é um fator de grande importância. A porcentagem de entrega define o pagamento pelo cliente e o alocamento de custos garante que o orçamento disponível não seja estourado, evitando problemas administrativos.

Assim, este projeto tem como objetivo prover facilidade na gestão de projetos de engenharia, definir uma forma consistente de registro histórico, entregar visualização de dados eficientemente e realizar melhor alocamento de recursos para redução de gastos.

## Conteúdo

Giyu é composto por três produtos diferentes em abordagem, mas que se comunicam no mesmo ecossistema. São eles: API, UI e Report BI.

A API tem como função permitir a manipulação dos dados de forma segura, abstraindo todas as regras de negócio e validações necessárias para o funcionamento da gestão de projetos e controle de orçamento. É nela que informações como "quantidade prevista" e "quantidade real" são trabalhadas e traduzidas para a modelagem de dados necessária.

A UI é a forma visual para interagir com a API. Não existe impedimento para que usuários executem as ações por meio de chamadas da API, porém é de conhecimento que não é a forma mais intuitiva para usuários não acostumados. Assim, a UI se apresenta como necessário para leigos em tecnologia, mas que desejam realizar a gestão dos seus projetos.

O Report BI é a visualização analítica dos dados. É nela que os usuários poderão verificar por meio de estatísticas o andamento do projeto, assim como a melhor alocação de recursos, calculada em tempo de execução.

## Ferramentas

Para a API foi utilizado o conjunto de Python e Flask. O armazenamento de dados fica a cargo do PostgreSQL, carregado em container. Foi escolhido o Microsoft Power BI para a criação do Report BI. Por fim, a UI ainda está em processo de definição, se serão carregados por meio dos templates Flask ou criados por um framework específico para front-end.

Futuramente, todas os sistemas poderão ser inicializados em containers.

## Rotas

### Autenticação de usuário

`POST /login`

```
Body:
  user: string com nome do usuário
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
  token: string com JWT
  idUser: id do usuário logado
```

### Recuperar engenheiros cadastrados no sistema

`GET /engineer`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Query Params:
  page: inteiro com o número da página
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
  data: lista de objetos encontrados
  page: página recuperada
  totalPages: quantidade de páginas totais
```

### Cadastrar novo engenheiro no sistema

`POST /engineer`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Body:
  name: string com nome do engenheiro a ser cadastrado
  title: string com título do engenheiro
  creator: inteiro com o id do usuário que requisita a criação
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
```

### Recuperar vendedores cadastrados no sistema

`GET /seller`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Query Params:
  page: inteiro com o número da página
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
  data: lista de objetos encontrados
  page: página recuperada
  totalPages: quantidade de páginas totais
```

### Cadastrar novo vendedor no sistema

`POST /seller`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Body:
  name: string com nome do vendedor
  creator: inteiro com id do usuário que requisitou o cadastro
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
```

### Recuperar materiais cadastrados no sistema

`GET /material`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Query Params:
  page: inteiro com o número da página
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
  data: lista de objetos encontrados
  page: página recuperada
  totalPages: quantidade de páginas totais
```

### Cadastrar novo material no sistema

`POST /material`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Body:
  description: string com descrição do material que será vendido
  type: inteiro que representa o tipo do material, 1 para "mão de obra" e 2 para "material"
  creator: inteiro com o id do usuário que solicitou o cadastro
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
```

### Recuperar vendedores que oferecem um material

`GET /item/<id>`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Route Params:
  id: inteiro com o id do material que será buscado
  
Query Params:
  page: inteiro com o número da página
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
  data: lista de objetos encontrados
  page: página recuperada
  totalPages: quantidade de páginas totais
```

### Recuperar materiais oferecidos por um vendedor

`GET /item/seller/<id>`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Route Params:
  id: inteiro com o id do vendedor que será buscado
  
Query Params:
  page: inteiro com o número da página
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
  data: lista de objetos encontrados
  page: página recuperada
  totalPages: quantidade de páginas totais
```

### Cadastrar uma oferta de material nova

`POST /item`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Body:
  material: inteiro com id do material que será ofertado
  seller: inteiro com id do vendedor que ofertará
  creator: inteiro com id do usuário que solicitou o cadastro
  unitPrice: inteiro com preço unitário do produto (valor decimal multiplicado por 100, ex: 12.25 => 1225, 12,00 => 1200, 1,00 => 100)
  minDiscount: inteiro com quantidade mínima para validar o desconto
  discountPrice: inteiro com preço unitário do produto com desconto (valor decimal multiplicado por 100, ex: 12.25 => 1225, 12,00 => 1200, 1,00 => 100)
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
```

### Alterar informações de uma oferta existente

`PUT /item`

```
Header:
  token: string com o JWT
  id: string com id do usuário
  
Body:
  item: inteiro com id da oferta que será alterada
  unitPrice: inteiro com preço unitário do produto (valor decimal multiplicado por 100, ex: 12.25 => 1225, 12,00 => 1200, 1,00 => 100)
  minDiscount: inteiro com quantidade mínima para validar o desconto
  discountPrice: inteiro com preço unitário do produto com desconto (valor decimal multiplicado por 100, ex: 12.25 => 1225, 12,00 => 1200, 1,00 => 100)
  active: inteiro 0 ou 1, que informa se a oferta do material está visível ou não para orçamentos
  
Response:
  statusCode: situação da requisição
  message: log descritivo da situação da requisição, vazio se status for 200
```

## Algumas regras internas

1. O gerenciamento de datas é importante e representa uma etapa sensível. A princípio, todas as datas são salvas no banco de dados com o horário UTC (-00:00). A gestão dos fusos pode ser realizada na UI, com a seleção do mesmo pelo usuário.
2. A API apresenta alguns códigos de resposta (status code) personalizados para informar estados específicos de resultado. São eles:

Código | Significado
-------|------------
200    | Sucesso no processamento pelo servidor.
400    | Requisição inválida.
401    | Usuário não autenticado ou autorizado.
444    | Não cumprimento de alguma regra de negócio do sistema.
500    | Erros de código e exeções de sistema