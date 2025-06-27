from fastapi import FastAPI, Query
from services.sicoob_service import obter_extrato
from services.pdf_generator import gerar_pdf

app = FastAPI()

@app.get("/extrato/{mes}/{ano}")
def gerar_extrato_pdf(
    mes: int,
    ano: int,
    diaInicial: int = Query(..., alias="diaInicial"),
    diaFinal: int = Query(..., alias="diaFinal"),
    agruparCNAB: bool = Query(True, alias="agruparCNAB"),
    numeroContaCorrente: int = Query(..., alias="numeroContaCorrente")
):
    dados = obter_extrato(mes, ano, diaInicial, diaFinal, agruparCNAB, numeroContaCorrente)
    nome_arquivo = f"extrato_{ano}-{mes:02d}-{diaInicial:02d}_a_{diaFinal:02d}.pdf"
    caminho = gerar_pdf(dados, nome_arquivo)

    return {"status": "sucesso", "arquivo": caminho}
