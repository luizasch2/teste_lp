"""
Dicionarios com quantidade ja estabelecidos
"""


massa = {}
molho = {}
queijo = {}
cobertura = {}


def montar(dic1: dict, dic2: dict,dic3:dict, dic4: dict) -> tuple:
    """Montar a pizza e calcular o valor

    :param dic1: dicionario com a massa e quantidade
    :type dic1: dict
    :param dic2: dicionario com o molho e quantidade
    :type dic2: dict
    :param dict3: dicionario com o queijo e quantidade
    :type dict3: dict
    :param dict4: dicionario com o cobertura e quantidade
    :type dict4: dict
    :return: pizza montada e preço
    :rtype: tuple
    """
    preco_total = 0
    tipos = [massa, molho, queijo, cobertura]
    tipo = 0
    for dic in [dic1, dic2, dic3, dic4]:
        for elemento in dic.items():
            if elemento[0] in tipos[tipo]:
                for i in tipos[tipo].items():
                    if i[0] == elemento[0]:
                        preco_total += elemento[1] * i[1]
                tipo += 1
            else:
                tipo += 1
                raise AttributeError('Não tem a opção disponível')
            
    pizza_montada = dict(dic1.items()+dic2.items() + dic3.items() + dic4.items())
    return pizza_montada,preco_total


def cadastrar(tipo: str,nome:str,preco: float) -> dict: 
    """cadastra mais um ingrediente no respectivo dicionário

    :param tipo: tipo do elemento a ser cadastrado
    :type tipo: str
    :param nome: nome do ingrediente
    :type nome: str
    :param preco: preço do ingrediente
    :type preco: float
    :return: dicionario com novo elemento cadastrado
    :rtype: dict
    """    
    if tipo == 'massa':
        massa[nome] = preco
        return massa
    elif tipo == 'molho':
        molho[nome] = preco
        return molho
    elif tipo == 'queijo':
        queijo[nome] = preco
        return queijo
    elif tipo == 'cobertura':
        cobertura[nome] = preco
        return cobertura
    else:
        raise KeyError('tipo inexistente')
    


def remover(tipo: str, nome: str) -> dict:
    """remover  um ingrediente no respectivo dicionário

    :param tipo: tipo do elemento a ser removido
    :type tipo: str
    :param nome: nome do ingrediente
    :type nome: str
    :return: dicionario com novo elemento removido
    :rtype: dict
    """
    try:
        if tipo == 'massa':
            massa.pop(nome)
            return massa
        elif tipo == 'molho':
            molho.pop(nome)
            return molho
        elif tipo == 'queijo':
            queijo.pop(nome)
            return queijo
        elif tipo == 'cobertura':
            cobertura.pop(nome)
            return cobertura
        else:
            raise Exception('tipo inexistente')
    except KeyError:
        return 'nome inválido'


def listar(tipo:str) -> dict:
    """lista de um tipo

    :param tipo: tipo do que quer ser listado
    :type tipo: str
    :return: dicionario com tudo listado
    :rtype: dict
    """    
    
    if tipo == 'massa':
        return massa
    elif tipo == 'molho':
        return molho
    elif tipo == 'queijo':
        return queijo
    elif tipo == 'cobertura':
        return cobertura
    else:
        raise KeyError('tipo inexistente')
   
