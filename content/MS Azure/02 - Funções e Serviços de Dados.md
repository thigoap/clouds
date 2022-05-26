Title: 02. Funções e Serviços de Dados
Date: 2022-05-25
Category: MS Azure
Link: https://docs.microsoft.com/pt-br/learn/modules/explore-roles-responsibilities-world-of-data/
Course: MS Learn - Funções e Serviços de Dados

# Cargos de trabalho no Mundo dos Dados

## Administrador de Banco de Dados
- responsável pelos aspectos de design, implementação, manutenção e operação de sistemas de bancos de dados locais e baseados em nuvem;
- responsável pela disponibilidade geral e pelo desempenho e otimizações consistentes dos bancos de dados;
- responsável por gerenciar a segurança dos dados nos bancos de dados, conceder privilégios sobre os dados, além de conceder ou negar acesso aos usuários conforme apropriado;

## Engenheiro de Dados
- responsável por projetar e implementar cargas de trabalho relacionadas a dados, incluindo pipelines de ingestão de dados, atividades de limpeza e transformação e armazenamentos de dados para cargas de trabalho analíticas;
- responsável por garantir que a privacidade dos dados seja mantida dentro da nuvem, abrangendo armazenamentos de dados locais e na nuvem;
- responsávelpor gerenciar e monitorar pipelines de dados para garantir que as cargas de dados tenham o desempenho esperado;

## Analista de Dados
- permite que as empresas maximizem o valor dos ativos de dados. Eles são responsáveis por explorar dados para identificar tendências e relações, projetar e criar modelos analíticos e favorecer capacidades avançadas de análise por meio de relatórios e visualizações;
- processa dados brutos e, com base em requisitos empresariais identificados, os transforma para fornecer insights relevantes;

# Serviços de Dados

## SQL do Azure
- Os serviços específicos de SQL do Azure incluem:
    - **Banco de Dados SQL do Azure**: um banco de dados de PaaS (plataforma como serviço) totalmente gerenciado hospedado no Azure;
    - **Instância Gerenciada de SQL do Azure**: uma instância hospedada do SQL Server com manutenção automatizada, que permite uma configuração mais flexível do que o BD de SQL do Azure, mas com mais responsabilidade administrativa para o proprietário;
    - **VM de SQL do Azure**: uma máquina virtual com uma instalação do SQL Server, permitindo a máxima capacidade de configuração com total responsabilidade de gerenciamento;

## Banco de dados do Azure para bancos dados relacionais de código aberto
- O Azure inclui serviços gerenciados para sistemas de banco de dados relacionais populares de código aberto, incluindo:
    - **Banco de Dados do Azure para MySQL**: um sistema de gerenciamento de banco de dados de código aberto fácil de usar que é comumente usado em aplicativos da pilha LAMP (Linux, Apache, MySQL e PHP);
    - **Banco de Dados do Azure para MariaDB**: um sistema de gerenciamento de banco de dados mais recente, criado pelos desenvolvedores originais do MySQL. Desde então, o mecanismo de banco de dados foi reescrito e otimizado para aprimorar o desempenho;
    - **Banco de dados do Azure para PostgreSQL**: um banco de dados híbrido relacional-objeto. É possível armazenar dados em tabelas relacionais, mas um banco de dados PostgreSQL também permite que você armazene tipos de dados personalizados, com propriedades não relacionais próprias;

## Azure Cosmos DB
- o Azure Cosmos DB é um sistema de banco de dados não relacional (NoSQL) de escala global que dá suporte a várias APIs (interfaces de programação de aplicativo), permitindo que você armazene e gerencie dados como documentos JSON, pares chave-valor, famílias de colunas e grafos;

## Armazenamento do Azure
- o Armazenamento do Azure é um serviço principal do Azure que permite armazenar dados em:
    - **Contêineres de blobs**: armazenamento escalonável e econômico para arquivos binários;
    - **Compartilhamentos de arquivos**: compartilhamentos de arquivos de rede, semelhante ao que normalmente é encontrado nas redes corporativas;
    - **Tabelas**: armazenamento de chave-valor para aplicativos que precisam ler e gravar valores de dados rapidamente;

## Fábrica de dados do Azure
- o Azure Data Factory é um serviço do Azure que permite definir e agendar pipelines de dados para transferir e transformar dados;
- o Azure Data Factory é usado por engenheiros de dados para criar soluções de ETL (extração, transformação e carregamento) que preenchem os armazenamentos de dados analíticos com os dados de sistemas transacionais na organização;

## Azure Synapse Analytics
- o Azure Synapse Analytics é uma solução de análise de dados abrangente e unificada que oferece uma interface de serviço única para vários recursos analíticos;

## Azure Databricks
- o Azure Databricks é uma versão integrada do Azure da plataforma popular do Databricks, que combina a plataforma de processamento de dados Apache Spark com a semântica de banco de dados SQL e uma interface de gerenciamento integrada para permitir a análise de dados em larga escala;

## Azure HDInsight
- o Azure HDInsight é um serviço do Azure que fornece clusters hospedados no Azure para tecnologias populares de código aberto de processamento de Big Data do Apache, incluindo:
    - **Apache Spark**: um sistema de processamento de dados distribuído que dá suporte a várias linguagens de programação e APIs, incluindo Java, Scala, Python e SQL;
    - **Apache Hadoop**: um sistema distribuído que usa trabalhos MapReduce para processar grandes volumes de dados com eficiência em vários nós de cluster. Os trabalhos MapReduce podem ser escritos em Java ou abstraídos por interfaces como Apache Hive, uma API baseada em SQL que é executada no Hadoop;
    - **Apache HBase**: um sistema de código aberto para armazenamento e consulta de dados NoSQL em larga escala;
    - **Apache Kafka**: um agente de mensagens para processamento de fluxo de dados;
    - **Apache Storm**: um sistema de código aberto para processamento de dados em tempo real por meio de uma topologia de spouts e bolts;

## Stream Analytics do Azure
- o Azure Stream Analytics é um mecanismo de processamento de fluxo em tempo real que captura um fluxo de dados de uma entrada, aplica uma consulta para extrair e manipular os dados do fluxo de entrada e grava os resultados em uma saída para análise ou processamento adicional;

## Azure Data Explorer
- o Azure Data Explorer é um serviço autônomo que oferece a mesma consulta de alto desempenho de dados de log e telemetria que o runtime do Data Explorer do Azure Synapse no Azure Synapse Analytics;

## Microsoft Purview
- o Microsoft Purview fornece uma solução para governança e descoberta de dados de toda a empresa. Use o Microsoft Purview para criar um mapa de seus dados e acompanhar a linhagem de dados em várias fontes de dados e sistemas, permitindo encontrar dados confiáveis para análise e relatórios;

## Microsoft Power BI
- o  Microsoft Power BI é uma plataforma para modelagem de dados analíticos e relatórios que os analistas de dados podem usar para criar e compartilhar visualizações de dados interativas;