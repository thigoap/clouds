Title: 03. Conceitos Fundamentais de Dados Relacionais
Date: 2022-05-25
Category: MS Azure
Link: https://docs.microsoft.com/pt-br/learn/modules/explore-relational-data-offerings/
Course: MS Learn - Conceitos Fundamentais de Dados Relacionais

# Dados Relacionais

- em um banco de dados relacional, você modelará coleções de entidades do mundo real na forma de tabelas;
- uma entidade pode ser qualquer coisa para a qual você deseja registrar informações; geralmente objetos e eventos importantes;
- as tabelas relacionais são um formato para dados estruturados e cada linha de uma tabela tem as mesmas colunas;
- os tipos de dados disponíveis que você pode usar ao definir uma tabela dependem do sistema de banco de dados que você está usando;

## Normalização

- é um termo usado por profissionais de banco de dados para um processo de design de esquema que minimiza a duplicação de dados e impõe a integridade dos dados;
    1. Separar cada entidade em sua própria tabela;
    2. Separar cada atributo discreto em sua própria coluna;
    3. Identificar exclusivamente cada instância de entidade (linha) usando uma chave primária;
    4. Usar colunas de chave estrangeira para vincular entidades relacionadas;
- as instâncias de cada entidade são identificadas exclusivamente por uma ID ou outro valor de chave, conhecido como chave primária;
- quando uma entidade faz referência a outra (por exemplo, um pedido tem um cliente associado), a chave primária da entidade relacionada é armazenada como uma chave estrangeira;
- em alguns casos, uma chave (primária ou estrangeira) pode ser definida como uma chave composta com base em uma combinação exclusiva de várias colunas;

## Linguagem SQL

- SQL significa Linguagem de Consulta Estruturada e é usada para se comunicar com um banco de dados relacional;
- Alguns dialetos populares do SQL incluem:
    - **T-SQL (Transact-SQL)**: essa versão do SQL é usada pelo Microsoft SQL Server e pelos serviços de SQL do Azure;
    - **pgSQL**: esse é o dialeto que tem extensões implementadas no PostgreSQL;
    - **PL/SQL**: esse é o dialeto usado pela Oracle. PL/SQL significa Procedural Language/SQL;

### Tipos de Instrução SQL

### Instruções DDL
- usadas para criar, modificar e remover tabelas e outros objetos em um banco de dados (tabela, procedimentos armazenados, exibições, entre outros);

| Instrução  | Descrição                                                                                          |
| -----------|----------------------------------------------------------------------------------------------------|
| CREATE     | Cria um objeto no banco de dados, como uma tabela ou uma exibição.                                 |
| ALTER      | Modifica a estrutura de um objeto. Por exemplo, alterar uma tabela para adicionar uma nova coluna. |
| DROP       | Remova um objeto do banco de dados.                                                                |
| RENAME     | Renomeia um objeto existente.                                                                      |

### Instruções DCL
- usadas para gerenciar o acesso a objetos em um banco de dados, concedendo, negando ou revogando permissões a usuários ou grupos específicos;  

| Instrução  | Descrição                                               |
| -----------|---------------------------------------------------------|
| GRANT      | Conceder permissão para executar ações específicas.     |
| DENY       | Negar permissão para executar ações específicas.        |
| REVOKE     | Remover uma permissão concedida anteriormente.          |

### Instruções DML
- usadas para para manipular as linhas em tabelas. Essas instruções permitem recuperar (consultar) dados, inserir novas linhas ou modificar linhas existentes;

| Instrução	 | Descrição                              |
| -----------|----------------------------------------|
| SELECT	 | Ler linhas de uma tabela               |
| INSERT	 | Inserir novas linhas em uma tabela     |
| UPDATE	 | Modificar dados em linhas existentes   |
| DELETE	 | Excluir linhas existentes              |

## Objetos de Banco de Dados

### Exibição
- uma exibição é uma tabela virtual com base no conjunto de resultados de uma consulta **SELECT**;
- é possível consultar a exibição e filtrar os dados de maneira muito semelhante à de uma tabela;

### Procedimento Armazenado
- um procedimento armazenado define instruções SQL que podem ser executadas sob comando;
- você pode definir um procedimento armazenado com parâmetros para criar uma solução flexível para ações comuns que talvez precisem ser aplicadas aos dados com base em uma chave ou em critérios específicos;

### Índice
- um índice ajuda a pesquisar dados em uma tabela. Imagine um índice em uma tabela como um índice no final de um livro. Um índice de livro contém um conjunto classificado de referências, com as páginas nas quais cada referência ocorre;
- **IMPORTANTE**: um índice consome espaço de armazenamento e sempre que você insere, atualiza ou exclui dados em uma tabela, é necessário haver manutenção nos índices dessa tabela;