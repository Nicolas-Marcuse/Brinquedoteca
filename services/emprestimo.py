from datetime import date
from repositories.db_fake import *
from domain.models import Emprestimo

def criar_emprestimo(crianca_id, brinquedo_id):
    crianca = next((c for c in criancas if c.id == crianca_id), None)
    brinquedo = next((b for b in brinquedos if b.id == brinquedo_id), None)

    if not crianca or not brinquedo:
        return {"erro": "dados inválidos"}

    if crianca.bloqueada:
        return {"erro": "crianca bloqueada"}

    if not brinquedo.disponivel:
        return {"erro": "brinquedo indisponivel"}

    ativos = [e for e in emprestimos if e.crianca_id == crianca_id and e.status == "ativo"]
    if len(ativos) >= 2:
        return {"erro": "limite atingido"}

    emp = Emprestimo(
        id=len(emprestimos)+1,
        crianca_id=crianca_id,
        brinquedo_id=brinquedo_id,
        data_emprestimo=date.today()
    )

    brinquedo.disponivel = False
    emprestimos.append(emp)

    return emp


def devolver(id):
    emp = next((e for e in emprestimos if e.id == id), None)

    if not emp:
        return {"erro": "nao achou"}

    emp.status = "finalizado"
    emp.data_devolucao = date.today()

    dias = (emp.data_devolucao - emp.data_emprestimo).days

    if dias > 7:
        atraso = dias - 7
        emp.multa = atraso * 2

        crianca = next(c for c in criancas if c.id == emp.crianca_id)
        crianca.atrasos += 1

        if crianca.atrasos >= 3:
            crianca.bloqueada = True

    brinquedo = next(b for b in brinquedos if b.id == emp.brinquedo_id)
    brinquedo.disponivel = True

    return emp