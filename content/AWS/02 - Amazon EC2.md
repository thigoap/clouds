Title: 02. Amazon EC2
Date: 2022-05-25
Category: AWS
Link: https://explore.skillbuilder.aws/learn/course/8287/aws-cloud-practitioner-essentials-portuguese
Course: AWS Cloud Practitioner Essentials

# Tipos de instâncias do Amazon EC2
## Instâncias de Uso Geral
- instâncias de uso geral equilibram os recursos de computação, memória e rede;
- utilizada para um aplicativo no qual as necessidades de recursos para computação, memória e rede sejam praticamente equivalentes;

## Instâncias Otimizadas para Computação
- instâncias otimizadas para computação são ideais para aplicativos vinculados à computação que se beneficiam de processadores de alto desempenho;
- aplicativos otimizados para computação são ideais para servidores web de alto desempenho, servidores de aplicativos de computação intensiva e servidores de jogos dedicados;
- você também pode usar instâncias otimizadas para computação para cargas de trabalho de processamento em lote, com o processamento de muitas transações em um único grupo;

## Instâncias Otimizadas para Memória
- instâncias otimizadas para memória são projetadas para fornecer desempenho rápido para cargas de trabalho que processam grandes conjuntos de dados na memória;
- utilizada em cenários que você tenha uma carga de trabalho que precise que grandes quantidades de dados sejam pré-carregados antes de executar um aplicativo;
- esse cenário pode ser de um banco de dados de alto desempenho ou uma carga de trabalho que envolva a execução de processamento em tempo real de uma grande quantidade de dados não estruturados;

## Instâncias de Computação Acelerada
- instâncias de computação acelerada usam aceleradores de hardware, ou coprocessadores, para executar algumas funções de forma mais eficiente do que é possível em um software executado em CPUs;
- exemplos dessas funções são cálculos de números com vírgula flutuante, processamento de gráficos e correspondência de padrões de dados;

## Instâncias Otimizadas para Armazenamento
- instâncias otimizadas para armazenamento são projetadas para cargas de trabalho que exigem alto acesso sequencial de leitura e gravação a grandes conjuntos de dados no armazenamento local;
- exemplos são sistemas de arquivos distribuídos, aplicativos de data warehouse e sistemas de processamento de transações on-line de alta frequência (OLTP)

# Definição de preço do Amazon EC2
## Instâncias sob demanda
-  instâncias sob demanda são ideais para cargas de trabalho irregulares de curto prazo que não podem ser interrompidas;
- custos antecipados ou contratos mínimos não se aplicam;
- exemplos de casos de uso para instâncias sob demanda são desenvolvimento e teste de aplicativos e execução de aplicativos com padrões de uso imprevisíveis;

## Savings Plans do Amazon EC2
- o Savings Plans do Amazon EC2 permite reduzir os custos de computação ao haver o compromisso com uma quantidade consistente de uso de computação por um período de um ou três anos;
- qualquer uso até o compromisso é cobrado de acordo com o preço de Savings Plan com desconto (por exemplo, USD 10 por hora);
- qualquer uso além do compromisso é cobrado de acordo com os preços normais de instâncias sob demanda;

## Instâncias Reservadas
- instâncias reservadas são um desconto de cobrança aplicado ao uso de instâncias sob demanda em sua conta;

## Instâncias Spot
- instâncias spot são ideais para cargas de trabalho com horários de início e término flexíveis ou que toleram interrupções;
- as instâncias spot usam a capacidade de computação não utilizada do Amazon EC2 e têm uma economia de até 90% de desconto em relação aos preços das instâncias sob demanda;

## Hosts Dedicados
- hosts dedicados são servidores físicos com capacidade de instância do Amazon EC2 totalmente dedicada ao uso do cliente;


# Scaling do Amazon EC2

## Escalabilidade
- a escalabilidade envolve começar apenas com os recursos de que você precisa e projetar sua arquitetura para responder automaticamente às alterações de demanda, fazendo aumentos ou reduções;

## Amazon EC2 Auto Scaling
- o Amazon EC2 Auto Scaling permite que você adicione ou remova automaticamente instâncias do Amazon EC2 em resposta à alteração da demanda do aplicativo;
- No Amazon EC2 Auto Scaling, há duas abordagens disponíveis: scaling dinâmico e scaling preditivo:
    1. o scaling dinâmico responde às alterações na demanda;
    2. o scaling preditivo programa automaticamente o número correto de instância do Amazon EC2 com base na demanda prevista;
- a capacidade mínima é o número de instâncias do Amazon EC2 que são executadas imediatamente após a criação do grupo do Auto Scaling;
- você pode definir a capacidade desejada como duas instâncias do Amazon EC2, mesmo que o aplicativo precise de um mínimo de uma única instância do Amazon EC2 para que seja executado;
- a terceira configuração que você pode definir em um grupo do Auto Scaling é a capacidade máxima. Por exemplo, você pode configurar o grupo do Auto Scaling para aumentar em resposta à demanda elevada, mas apenas para um máximo de quatro instâncias do Amazon EC2;

# Direcionamento de Tráfego com o Elastic Load Balancing
## Elastic Load Balancing
- o Elastic Load Balancing é o serviço AWS que distribui automaticamente o tráfego de entrada de aplicativos entre vários recursos, como instâncias do Amazon EC2;
- um balanceador de carga atua como um ponto único de contato para todo o tráfego da web de entrada no seu grupo do Auto Scaling;

# Sistema de Mensagens e Enfileiramento
## 