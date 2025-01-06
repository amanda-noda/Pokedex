from ast import Dict, List

class icone(object):
    foto:Dict[str]
    pass

class Movimentos(object):
    Movimentos:4
    nome:str
    level:int
    pass


class Status(object):
    hp:int
    defesa:int
    ataque:int
    speed:int
    sp_atk:int
    sp_def:int
    pass

class Habilidade(object):
    nome:str
    hb_escondida:bool
    pass

class Pokemon:
    dex:int
    dex:int
    nome:str
    tipo:str
    altura:float
    peso:float
    habilidade:List[Habilidade]
    pass
