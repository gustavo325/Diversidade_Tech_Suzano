![imagem_2023-01-21_004003898.png](https://s2.loli.net/2023/01/21/Wu4tfyV81EOpDjR.png)

_____

- **Proposta do projeto:** 

  - Sua SQUAD foi contratada para modelar um banco de dados relacional para abrigar dados de utilizados para manutenção preditiva de máquinas. Com objetivo de subsidiar a construção do banco de dados foi lhes entregue uma série de arquivos contendo exemplos dos dados que são coletados. Estes são compostos pelos seguintes dados:

    **Condições e uso da máquina**: As condições de operação de uma máquina, por ex. dados coletados de sensores.

    **Histórico de falhas**: O histórico de falhas de uma máquina ou componente dentro da máquina. **Histórico de manutenção**: O histórico de reparos de uma máquina, por ex. códigos de erro, atividades de manutenção anteriores ou substituições de componentes. **Características da máquina**: As características de uma máquina, por ex. tamanho do motor, marca e modelo, localização.

    Detalhes Dados de:

    **Série temporal de telemetria** (`PdM_telemetry.csv`): Consiste na média horária de tensão, rotação, pressão e vibração coletada de 100 máquinas para o ano de 2015.

    **Erro** (`PdM_errors.csv`): São os erros encontrados pelas máquinas durante o funcionamento. Como esses erros não desligam as máquinas, não são considerados como falhas. A data e hora do erro são arredondadas para a hora mais próxima, pois os dados de telemetria são coletados por hora.

    **Manutenção** (`PdM_maint.csv`): Se um componente de uma máquina for substituído, isso é capturado como um registro nesta tabela. Os componentes são substituídos em duas situações: 1. Durante a visita regular agendada, o técnico substituiu (Manutenção Proativa) 2. Um componente quebra e então o técnico faz uma manutenção não programada para substituir o componente (Manutenção Reativa). Isso é considerado uma falha e os dados correspondentes são capturados em Falhas. Os dados de manutenção têm registros de 2014 e 2015. Esses dados são arredondados para a hora mais próxima, pois os dados de telemetria são coletados por hora.

    **Falhas** (`PdM_failures.csv`): Cada registro representa a substituição de um componente devido a falha. Esses dados são um subconjunto dos dados de manutenção. Esses dados são arredondados para a hora mais próxima, pois os dados de telemetria são coletados por hora.

    **Metadados de máquinas** (`PdM_Machines.csv`): tipo de modelo e idade das máquinas.

    Utilizando os arquivos e a descrição do problema acima elabore uma apresentação comercial para equipe técnica do seu cliente contendo:

    - Descrição do Banco de Dados utilizado (MySQL ou SQLite, conforme organização prévia de grupos)
      1. Histórico
      2. Presença no Mercado
      3. Principais Utilizações
      4. Preço, se aplicável
      5. Ferramentas de gerenciamento e acesso disponíveis.
    - O Diagrama do Modelo Entidade Relacionamento Conceitual (Peter Chen) respeitando a 1FN, 2FN e a 3FN.
    - O Diagrama do Modelo Entidade Relacionamento Lógico (James Martin) com base no item anterior.
    - O Modelo físico para o banco definido (Diagrama, se disponível e arquivo `.sql`).
    - Script Python ou SQL com a carga dos dados das planilhas para o banco.
    - Backup do Bando de Dados ao Final de Carga.

​	**Link dos dados: https://www.kaggle.com/datasets/arnabbiswas1/microsoft-azure-predictive-maintenance**

____

- **Descrição de arquivos:** 

  1. **data_load_projeto.ipynb**

     - Notebook utilizado para visualização, ajustes nas tabelas e carga no banco de dados; 

  2. **Dump20230108.sql**

     - Banco de dados com carga realizada; 

  3. **Projeto_1_logico.png**

     - **Modelo lógico** 

       ![Projeto_1_logico.png](https://s2.loli.net/2023/01/21/qvPXpctwiJI29MW.png)

  4. **Projeto_1.brM3**

     - **Modelo conceitual**

       ![imagem_2023-01-22_003849647.png](https://s2.loli.net/2023/01/22/HsePkBhu5p6bWZK.png)
  
  5. **CSVs**
  
     - Contém todas as tabelas utilizadas para alimentar o banco; 

_______

##### **Participantes** :busts_in_silhouette:

- Alecsander Guimarães;
- Gabriel ícaro;
- Giselly Landim;
- Gustavo Henrique; 
- Joelson da Silva;
- Rafael Alves. 

______

