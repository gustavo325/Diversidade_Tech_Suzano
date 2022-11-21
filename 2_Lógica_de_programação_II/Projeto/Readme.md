- **Projeto II - Sistema de gerenciamento de Voos:**

  

  ![Diagrama_Aeroporto_Fundo_Branco2.png](https://s2.loli.net/2022/10/27/4ciBsmD89PTZKoA.png)

  

- Nesse projeto, a equipe desenvolveu um sistema de gerenciamento de voos que funciona com as seguintes condições: 
  
  - O sistema inicia com o usuário digitando um valor do tipo inteiro, que será utilizado como unidade de tempo, cada vez que esse número é decrementado no sistema, entende-se que uma rodada passou.
  
  _____
  
  - Existem três pistas no aeroporto, conforme mostra a imagem, a Pista 2 é a única que serve para decolagem e aterrissagem, sendo que as aterrissagens que ocorrem nessa pista são preferencialmente em casos de emergência. Outra condição associada a pista 2 é que, mesmo ela sendo de decolagem e aterrissagem, em uma rodada de tempo ela só pode fazer uma operação por vez. A quantidade máxima de aviões permitida é 3 por pista, exceto na pista 2, que pode ter até 6 aviões, sendo 3 na fila de decolagem e 3 na fila de aterrissagem. 
  
  _____
  
  - Cada avião tem uma condição para ser gerado, os IDs possuem no mínimo 6 caracteres, sendo 3 números seguidos por 3 letras, o combustível dos aviões é definido por um random de número inteiro que pode variar de 2 até 20. O tempo de espera para decolagem e aterrissagem, são compostos por um número inteiro que vai sendo incrementado a cada rodada que o avião permanece na fila de decolagem ou aterrissagem (a fila que o avião aparece vai depender de uma função dentro do programa que é responsável por mover os aviões para as filas, respeitando o limite de quantidade). 
  
  _____
  
  - Aterrissagem de emergência: Existem uma função no programa chamada mover em emergência, que vai priorizar os aviões que estiverem com menor quantidade de combustível naquela rodada para realizar a aterrissagem, pois caso o combustível do avião seja zero, será exibida a informação em tela de que o avião caiu, juntamente com o seu respectivo ID. 
  
  _____
  
  - Aterrissagem: Os aviões que estiverem com maior quantidade de combustível, irão realizar a aterrissagem nas pista 1 ou 3. A ordem de aterrisagem dos aviões que não estão com pouco combustível ocorre por ordem de chegada, em um sistema de fila.
  
  _____
  
  - Decolagem: Só ocorre quando a pista 2 está livre, ou seja, quando não possui nenhum avião para aterrissar. 
  
  ____
  
  - A cada execução o usuário recebera na tela a seguinte informação: 
    - O número da rodada que o sistema está processando seguido pelos IDs dos aviões que estão se movimentando na rodada, a operação que estão realizando (decolagem ou aterrissagem) e a pista em que cada avião está realizando a operação.  
    - Abaixo dessa informação é exibido o estado de cada pista (que pode ser livre ou ocupada, esse estado, serve para impedir que a pista 2 realize mais de uma operação por rodada); 
    - A posição, o ID e o combustível de cada avião, nas filas das pistas, seguido pela quantidade de pousos emergenciais na pista. Por fim, é exibido o tempo médio de decolagem e por último o de aterrissagem, sendo a média de todas as pistas desde a primeira rodada até a rodada atual. 
  
  _____
  
  - No encerramento do programa, é gerado um arquivo CSV, com o nome "Dados aeroporto", que contém: 
    - Total de queda de aviões; 
    - Quantidade de pousos emergenciais; 
    - Tempo médio de espera para decolagem, seguido pelo de aterrissagem; 
    - Total de rodadas executadas.
  
  ____
  
  - Simulações realizadas: 
  
    - **Simulação 1:**
      - **Total de rodadas:** 4500;
      - **Percentual de queda:** cerca de 8%
      - **Pousos de emergência:** cerca de 3%
      - **Tempo médio de espera para decolagem:** Aproximadamente 8 rodadas; 
      - **Tempo médio de espera para aterrissagem:** Aproximadamente 2 rodadas; 
  
    ____
  
    - **Simulação 2:**
      - **Total de rodadas:** 6000;
      - **Percentual de queda:** cerca de 7%
      - **Pousos de emergência:** cerca de 5%
      - **Tempo médio de espera para decolagem:** Aproximadamente 8 rodadas; 
      - **Tempo médio de espera para aterrissagem:** Aproximadamente 2 rodadas; 

____

#### :busts_in_silhouette: Participantes:   

- Joelson Silva 
  - Linkedin: https://br.linkedin.com/in/joelsons 
- Jhaidan Ribeiro 
  - Linkedin: https://br.linkedin.com/in/jhaidan42
- Gustavo Henrique Siqueira
  - Linkedin: www.linkedin.com/in/gustavo-henriques

____



