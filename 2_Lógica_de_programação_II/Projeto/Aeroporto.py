import random
import string

pista1_geral = {'nome': "Pista 1", 'Fila de decolagem': [], 
'Fila de aterrisagem': [], 'Pousos de emergência': 0, 'estado': 'livre'}

pista2_geral = {'nome': "Pista 2", 'Fila de decolagem': [], 
'Fila de aterrisagem': [], 'Pousos de emergência': 0, 'estado': 'livre'}

pista3_geral = {'nome': "Pista 3", 'Fila de decolagem': [], 
'Fila de aterrisagem': [], 'Pousos de emergência': 0, 'estado': 'livre'}

tempos_decolagem_geral = []
tempos_aterrisagem_geral = []
avioes_gerados_geral = []
n_id_geral = 100

def tamanho(fila: str, pista_aa: dict, pista_bb: dict, pista_cc: dict) -> int: 
    ''' Tem como parâmetro o nome da fila e retorna o tamanho
    dessa fila nas três pistas somados. 
    '''
    tamanho = 0
    tamanho += len(pista_aa[fila])
    tamanho += len(pista_bb[fila]) 
    tamanho += len(pista_cc[fila])
    return tamanho

def max_avioes(pista_a: dict, pista_b: dict, pista_c: dict ): 
    ''' Recebe o número de elementos que já existem nas filas, para subtrair da 
    quantidade máxima de aviões gerados para decolagem e aterrissagem e retorna 
    esses valores.
    '''
    tamanho_decolagem = tamanho(fila = 'Fila de decolagem', 
    pista_aa = pista_a, pista_bb = pista_b, pista_cc = pista_c)
    
    tamanho_aterrisagem = tamanho('Fila de aterrisagem', 
    pista_aa = pista_a, pista_bb = pista_b, pista_cc = pista_c)

    tam_max_decolagem = 3 - tamanho_decolagem 
    tam_max_aterrisagem = 9 - tamanho_aterrisagem
    return tam_max_decolagem, tam_max_aterrisagem

def define_id(id_local: int):
    ''' Faz o sorteio de três números e três letras e concatena tudo
    em uma string e faz o retorno, ela é chamada como valor de chave ID
    assim quando o avião é gerado.
    '''    
    if id_local >= 999: 
        id_local = 100
    
    letras = string.ascii_uppercase
    id = ''

    id += str(id_local)
    id_local += 1
    
    while len(id) < 6:
        id += letras[random.randint(0,25)]
        
    return id_local, id

def gerar_aviao(max: int, avioes_local: list, id_local2: int):
    '''Tem um parâmetro número, que será utilizado
    como segundo argumento do randint para definir 
    a quantidade máxima da randomização do número de aviões gerados.
    '''    
    quantidade_randomica = random.randint(0,max)
    contador = 1 

    while contador <= quantidade_randomica:
        id_local2, id = define_id(id_local = id_local2)
        avioes_local.append({'ID' : id, 'combustível' : random.randint(2,20), 
        'tempo espera decolagem': 0, 'tempo espera aterrissagem': 0, 'tempo limite': 1})
        contador += 1
    return avioes_local, id_local2

def aterrisagem(pista: dict, avioes_local2: list):
    ''' Tem como parâmetro a variável pista e a lista de aviões gerados, 
    sendo responsável por mover os aviões para as filas de aterrissagem.
    '''
    contador = 3 -len(pista['Fila de aterrisagem']) 
    while contador > 0:
        if len(avioes_local2) > 0: 
            aviao = avioes_local2.pop(0)
            pista['Fila de aterrisagem'].append(aviao)
        else: 
            break
        contador -=1
    return pista, avioes_local2

def mover_para_fila(operacao: str, avioes_local: list, pista_a: dict, pista_b: dict, pista_c: dict):
    ''' Tem como parâmetro uma variável operacao e a lista de aviões gerados, 
    sendo utilizada para mover todos os aviões paras as filas de decolagem e aterrissagem.
    '''
    if operacao == 'Decolagem':
        for aviao in avioes_local: 
            pista_b['Fila de decolagem'].append(aviao)
        avioes_local.clear() # apagando itens da lista
    elif operacao == 'Aterrisagem': 
        pista_c, avioes_local = aterrisagem(pista = pista_c, 
        avioes_local2 = avioes_local)
        
        pista_a, avioes_local = aterrisagem(pista = pista_a, 
        avioes_local2 = avioes_local)
        
        pista_b, avioes_local = aterrisagem(pista = pista_b, 
        avioes_local2 = avioes_local)
        
        avioes_local.clear()
    return pista_a, pista_b, pista_c, avioes_local

def alterar_estado(pista_local: dict, novo_estado: str) -> dict:
    ''' Função utilizada para alterar o estado da pista, que pode ser ocupada ou livre. 
    Serve como controle, para que os aviões da pista2 só decolem quando não tiver nenhum avião 
    aterrissando na pista2, impedindo que ela realize mais de uma operação por vez.
    '''
    pista_local['estado'] = novo_estado
    return pista_local

def decolar(pista: dict, tempos_decolagem_local: list):
    ''' Tem como parâmetro a pista2, que é a única que usada para decolagem, removendo 
    da fila de decolagem e alterando o estado da pista para ocupado, para que não tenha
    aterrissagem nessa pista na rodada que estiver decolando. Essa função também 
    armazena o tempo de espera do avião para decolar. 
    '''
    if len(pista['Fila de aterrisagem']) == 0 and len(pista['Fila de decolagem']) > 0:
        aviao = pista['Fila de decolagem'].pop(0)
        pista = alterar_estado(pista_local = pista, novo_estado = 'ocupada')
        print(f'O avião de ID {aviao["ID"]} está decolando nesta rodada na {pista["nome"]}!')
        tempos_decolagem_local.append(aviao['tempo espera decolagem'])

    return pista, tempos_decolagem_local

def tempo_espera(pista: dict, fila:str, tempo: str) -> dict:
    ''' Tem três parâmetros, sendo a pista e a fila em que o avião está, 
    e o tempo de espera a ser incrementado, que pode ser para decolar ou aterrissar, 
    ambos são chaves que foram criadas na função gerar_avião. 
    Tendo como nomes tempo espera decolagem e tempo espera aterrissagem, respectivamente. 
    '''
    if len(pista[fila]) > 0: 
        for aviao in pista[fila]: 
            aviao[tempo] += 1
    return pista

def tempo_limite(pista: dict) -> dict: 
    ''' Calcula o tempo limite dos aviões que estão na fila de aterrissagem da 
    pista informada. Tempo limite é calculado através da operação:
    (valor do seu combustível - a sua posição na fila de aterrissagem).
    Serve como forma de prever em quantas rodadas o avião consegue ficar no ar.
    Quando seu número chega a um e não tem pistas disponíveis para aterrissar, 
    significa que o avião vai cair.
    '''
    if len(pista['Fila de aterrisagem']) > 0 and len(pista['Fila de aterrisagem']) <= 3: 
        for i, aviao in enumerate(pista['Fila de aterrisagem']): 
            if aviao['combustível'] - i > 0: 
                aviao['tempo limite'] = aviao['combustível'] - i
            else: 
                aviao['tempo limite'] = 0
    return pista

def mover_em_emergencia(pista_b: dict, pista_a: dict):
    if len(pista_a['Fila de aterrisagem']) > 0:
        if pista_a['Fila de aterrisagem'][0]['tempo limite'] > 1:
            if len(pista_a['Fila de aterrisagem']) <= 2: 
                if len(pista_b['Fila de aterrisagem']) == 3: 
                    if pista_b['Fila de aterrisagem'][1]['tempo limite'] == 1:
                        aviao = pista_b['Fila de aterrisagem'].pop(1)
                        pista_a['Fila de aterrisagem'].insert(0,(aviao))
                if len(pista_b['Fila de aterrisagem']) == 2: 
                    if pista_b['Fila de aterrisagem'][1]['tempo limite'] == 1:
                        aviao = pista_b['Fila de aterrisagem'].pop(1)
                        pista_a['Fila de aterrisagem'].insert(0,(aviao))
                    
            else: 
                if len(pista_b['Fila de aterrisagem']) == 3: 
                    if pista_b['Fila de aterrisagem'][1]['tempo limite'] == 1:
                        aviao = pista_b['Fila de aterrisagem'].pop(1)
                        pista_a['Fila de aterrisagem'].insert(0,(aviao))
                        aviao2 = pista_a['Fila de aterrisagem'].pop(3)
                        pista_b['Fila de aterrisagem'].append(aviao2)
                if len(pista_b['Fila de aterrisagem']) == 2: 
                    if pista_b['Fila de aterrisagem'][1]['tempo limite'] == 1:
                        aviao = pista_b['Fila de aterrisagem'].pop(1)
                        pista_a['Fila de aterrisagem'].insert(0,(aviao))
                        aviao2 = pista_a['Fila de aterrisagem'].pop(3)
                        pista_b['Fila de aterrisagem'].append(aviao2)

    else: # repete a partir da 4ª linha desta função, pois o len é 0
        if len(pista_b['Fila de aterrisagem']) == 3: 
            if pista_b['Fila de aterrisagem'][1]['tempo limite'] == 1:
                aviao = pista_b['Fila de aterrisagem'].pop(1)
                pista_a['Fila de aterrisagem'].insert(0,(aviao))
            if len(pista_b['Fila de aterrisagem']) == 2: 
                if pista_b['Fila de aterrisagem'][1]['tempo limite'] == 1:
                    aviao = pista_b['Fila de aterrisagem'].pop(1)
                    pista_a['Fila de aterrisagem'].insert(0,(aviao))

    return pista_b, pista_a

def aterrisar(pista: dict, tempos_aterrisagem_local: list):
    ''' Tem como parâmetro a pista, que será utilizada para acessar a fila de aterrissagem e 
    caso a pista esteja livre, o avião será removido de fila de aterrissagem e irá aterrissar. 
    Ela também é responsável por verificar se o avião está pousando em emergência e contar
    quantos aviões pousaram em emergência nessa pista, informação que será visualizada no 
    relatório final.
    '''
    if pista['estado'] == 'livre':  
        if len(pista['Fila de aterrisagem']) > 0:
            aviao = pista['Fila de aterrisagem'].pop(0)
            tempos_aterrisagem_local.append(aviao['tempo espera aterrissagem'])
            if aviao['combustível'] == 1:
                pista['Pousos de emergência'] += 1
            pista = alterar_estado(pista_local = pista, novo_estado = 'ocupada')
            print(f'O avião de ID {aviao["ID"]} está aterrissando nesta rodada na {pista["nome"]}!')

    return pista, tempos_aterrisagem_local

def reduz_combustivel(pista: dict) -> dict: 
    ''' Responsável por percorrer a fila de aterrissagem da pista informada 
    (aviões que estão voando) e decrementar a chave combustível de todos os aviões.
    '''
    for aviao in pista['Fila de aterrisagem']: 
        aviao['combustível'] -=1
    return pista

def exibir_status(pista: dict, operacao: str):
    ''' Tem como parâmetro a pista e a operação, que pode ser aterrissagem ou decolagem. 
    Percorre a pista informada e retorna o painel de informaçõas:
    (quantidade de aviões na fila da operação especificada, os IDs dos aviões e posição na fila,
    quantidade de pousos emergenciais e tempo médio de decolagem e aterrissagem).
    '''
    print(f"{pista['nome']}: \n{' '*2}Quantidade de aviões na fila {operacao}: "\
        f"{len(pista['Fila de ' + operacao])}\n{' '*2} Estado da pista: {pista['estado']}\n"\
        f"{' '*4} Aviões nesta fila:")
    for indice, valor in enumerate(pista['Fila de ' + operacao]): 
        print(f"{' '*6} Posição{indice} : {valor['ID']}; Combustível: {valor['combustível']}")
    print(f'{" "*2} Quantidade de pousos emergenciais da {pista["nome"]}: {pista["Pousos de emergência"]}')
    print('')
    return None

def verificar_se_caiu(pista: dict) -> dict:
    ''' Percorre a fila de aterrissagem da pista informada e verifica se a chave combustível 
    está dentro da condição maior que 0 e retorna o número de aviões que caíram nessa fila.
    '''
    avioes_que_cairam = []
    for aviao in pista['Fila de aterrisagem']:
        if aviao['combustível'] == 0:
            print(f'O avião de ID {aviao["ID"]} caiu nesta rodada!')
            avioes_que_cairam.append(aviao)
    for aviao in avioes_que_cairam: 
        if aviao in pista['Fila de aterrisagem']:  
            pista['Fila de aterrisagem'].remove(aviao)
    return pista, len(avioes_que_cairam)

def calcular_medias(lista: list, operacao: str):
    ''' Tem como parâmetro uma lista, que pode ser dos tempos de decolagem ou aterrissagem. 
    Imprime o tempo médio de decolagem ou aterrissagem, que é definido pelo 
    parâmetro operação da função, que pode ser decolagem, ou aterrissagem. 
    '''
    if len(lista) > 0:
        print(f'Tempo médio de {operacao}: {(sum(lista)/len(lista)):.2f} 
              {" rodada" if sum(lista)/len(lista) == 1 else " rodadas"}\n')
        return None

def cria_arquivo(n_quedas: float, pousos_emergenciais: float, 
    espera_media_decolagem: float, espera_media_aterrissagem: float, total_rodadas: float): 
    
    with open(file = 'dados aeroporto.csv', mode = 'a', encoding = 'UTF-8') as linha: 
        linha_1 = f"Total de queda de avioes; QTDE de pousos emergenciais;"\
        " Tempo medio de espera para decolagem; Tempo medio de espera para aterrissagem; Total de rodadas\n"
        
        linha_2 = f'{n_quedas};{pousos_emergenciais};
        {espera_media_decolagem:.2f};{espera_media_aterrissagem:.2f};{total_rodadas}\n'
        linha.write(linha_1)
        linha.write(linha_2)

tempo = int(input("Digite a quantidade de rodadas desejada:\n"))

def inicia_tempo(tempo: int, n_id: int, pista1: dict, pista2: dict, pista3: dict,\
     tempos_decolagem: list, tempos_aterrisagem: list, avioes_gerados: list):
    ''' Responsável por executar as funções do sistema,
    decrementar o tempo em unidade informado pelo usuário e contar a quantidade 
    de rodadas executadas. Retorna os valores que são escritos no arquivo csv. 
    '''
    rodada = 1
    n_quedas = 0
    while tempo > 0:
        print(f"{'='*70}") 
        print(f" Estamos na rodada {rodada}")
        max_decolagem, max_aterrisagem = max_avioes(pista_a = pista1, pista_b = pista2, pista_c = pista3)
        avioes_gerados, n_id = \
        gerar_aviao(max = max_decolagem, avioes_local = avioes_gerados, id_local2 = n_id)
        
        pista1, pista2, pista3, avioes_gerados = \
        mover_para_fila(operacao = 'Decolagem', avioes_local = \
        avioes_gerados, pista_a = pista1, pista_b = pista2, pista_c = pista3)
        
        avioes_gerados, n_id = gerar_aviao(max = \
        max_aterrisagem, avioes_local = avioes_gerados, id_local2 = n_id)
        
        pista1, pista2, pista3, avioes_gerados = \
        mover_para_fila(operacao = 'Aterrisagem', avioes_local = \
        avioes_gerados, pista_a = pista1, pista_b = pista2, pista_c = pista3)

        pista2, tempos_decolagem = decolar(pista = pista2, tempos_decolagem_local = tempos_decolagem)
        
        pista1 = tempo_espera(pista = pista1, \
        fila = 'Fila de decolagem', tempo = 'tempo espera decolagem')

        pista2 = tempo_espera(pista = pista2, \
        fila = 'Fila de decolagem', tempo = 'tempo espera decolagem')

        pista3 = tempo_espera(pista = pista3, \
        fila = 'Fila de decolagem', tempo = 'tempo espera decolagem')
        
        pista1 = tempo_limite(pista = pista1)
        pista2 = tempo_limite(pista = pista2)
        pista3 = tempo_limite(pista = pista3)

        # Movendo da pista 3 pra pista 2... 
        pista3, pista2 = mover_em_emergencia(pista_b = pista3, pista_a = pista2)
        
        # Movendo da pista 1 pra pista 2... 
        pista1, pista2 = mover_em_emergencia(pista_b = pista1, pista_a = pista2)
        
        # Movendo da pista 1 pra pista 3... 
        pista1, pista3 = mover_em_emergencia(pista_b = pista1 ,pista_a = pista3)
        
        # Movendo da pista 3 pra pista 1... 
        pista3, pista1 = mover_em_emergencia(pista_b = pista3, pista_a = pista1)

        pista1, tempos_aterrisagem = \
        aterrisar(pista = pista1, tempos_aterrisagem_local = tempos_aterrisagem)
        pista2, tempos_aterrisagem = \
        aterrisar(pista = pista2, tempos_aterrisagem_local = tempos_aterrisagem)
        pista3, tempos_aterrisagem = \
        aterrisar(pista = pista3, tempos_aterrisagem_local = tempos_aterrisagem)
        
        pista1 = tempo_espera(pista = pista1, fila = \
        'Fila de aterrisagem', tempo = 'tempo espera aterrissagem')

        pista2 = tempo_espera(pista = pista2, fila = \
        'Fila de aterrisagem', tempo = 'tempo espera aterrissagem')

        pista3 = tempo_espera(pista = pista3, fila = \
        'Fila de aterrisagem', tempo = 'tempo espera aterrissagem')
        
        pista1 = reduz_combustivel(pista = pista1)
        pista2 = reduz_combustivel(pista = pista2)
        pista3 = reduz_combustivel(pista = pista3)
        
        exibir_status(pista = pista1, operacao = 'aterrisagem')
        exibir_status(pista = pista2, operacao = 'decolagem')
        exibir_status(pista = pista2, operacao = 'aterrisagem')
        exibir_status(pista = pista3, operacao = 'aterrisagem')
        
        pista1, total_quedas1 = verificar_se_caiu(pista = pista1)
        pista2, total_quedas2 = verificar_se_caiu(pista = pista2)
        pista3, total_quedas3 = verificar_se_caiu(pista = pista3)

        n_quedas += total_quedas1 + total_quedas2 + total_quedas3 
        
        calcular_medias(lista = tempos_decolagem, operacao = 'Decolagem')
        calcular_medias(lista = tempos_aterrisagem, operacao = 'Aterrisagem')
        
        pista1 = alterar_estado(pista_local = pista1, novo_estado = 'livre')
        pista2 = alterar_estado(pista_local = pista2, novo_estado = 'livre')
        pista3 = alterar_estado(pista_local = pista3, novo_estado = 'livre')

        tempo -= 1
        rodada +=1

    if tempo == 0: 
        print('Fim do programa!')
    pousos_emergenciais = pista1["Pousos de emergência"] + \
        pista2["Pousos de emergência"] + pista3["Pousos de emergência"]
        
    espera_decolagem = sum(tempos_decolagem)/len(tempos_decolagem)
    espera_aterrissagem = sum(tempos_aterrisagem)/len(tempos_aterrisagem)
    
    return n_quedas, pousos_emergenciais, espera_decolagem, espera_aterrissagem, (rodada-1) 

n_quedas_geral, pousos_emergenciais_geral, media_decolagem_geral, \
    media_aterrissagem_geral, total_rodadas_geral = \
    inicia_tempo(tempo = tempo, n_id = n_id_geral, pista1 = pista1_geral, \
    pista2 = pista2_geral, pista3 = pista3_geral, tempos_decolagem = \
    tempos_decolagem_geral, tempos_aterrisagem = \
    tempos_aterrisagem_geral, avioes_gerados = avioes_gerados_geral)

cria_arquivo(n_quedas = n_quedas_geral, pousos_emergenciais = pousos_emergenciais_geral, \
espera_media_decolagem = media_decolagem_geral, espera_media_aterrissagem = \
media_aterrissagem_geral, total_rodadas = total_rodadas_geral)








