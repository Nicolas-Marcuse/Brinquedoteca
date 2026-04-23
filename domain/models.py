from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass
class Crianca:
    id: int
    nome: str
    idade: int
    responsavel: str
    bloqueada: bool = False
    atrasos: int = 0

@dataclass
class Brinquedo:
    id: int
    nome: str
    categoria: str
    faixa_etaria_minima: int
    disponivel: bool = True

@dataclass
class Emprestimo:
    id: int
    crianca_id: int
    brinquedo_id: int
    data_emprestimo: date
    data_devolucao: date = None
    status: str = "ativo"
    multa: float = 0.0