from fastapi import APIRouter
from repositories.db_fake import *
from services.emprestimo_service import *

router = APIRouter()

@router.post("/criancas")
def criar_crianca(c: dict):
    criancas.append(c)
    return c

@router.get("/criancas")
def listar_criancas():
    return criancas

@router.post("/brinquedos")
def criar_brinquedo(b: dict):
    brinquedos.append(b)
    return b

@router.get("/brinquedos")
def listar_brinquedos():
    return brinquedos

@router.post("/emprestimos")
def criar(e: dict):
    return criar_emprestimo(e["crianca_id"], e["brinquedo_id"])

@router.get("/emprestimos")
def listar_emp():
    return emprestimos

@router.put("/emprestimos/{id}/devolver")
def devolver_emp(id: int):
    return devolver(id)