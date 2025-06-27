from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from app.sicoob import consultar_extrato
from app.utils.pdf import gerar_pdf_extrato

app = FastAPI(title="API de Extrato Sicoob")

# endpoint JSON padrão
@app.get("/extrato/{mes}/{ano}")
def extrato(
    mes: int,
    ano: int,
    diaInicial: int = Query(...),
    diaFinal: int = Query(...),
    agruparCNAB: bool = Query(True),
    numeroContaCorrente: int = Query(...)
):
    return consultar_extrato(mes, ano, diaInicial, diaFinal, agruparCNAB, numeroContaCorrente)


# endpoint para PDF
@app.get("/extrato/pdf/{mes}/{ano}")
def extrato_em_pdf(
    mes: int,
    ano: int,
    diaInicial: int = Query(...),
    diaFinal: int = Query(...),
    agruparCNAB: bool = Query(True),
    numeroContaCorrente: int = Query(...)
):
    resultado_json = consultar_extrato(mes, ano, diaInicial, diaFinal, agruparCNAB, numeroContaCorrente)
    nome_arquivo = f"extrato_{mes}_{ano}.pdf"
    gerar_pdf_extrato(resultado_json, nome_arquivo=nome_arquivo)
    return FileResponse(nome_arquivo, media_type="application/pdf", filename=nome_arquivo)
