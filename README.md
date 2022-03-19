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