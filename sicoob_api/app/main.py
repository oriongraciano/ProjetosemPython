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

    # caminho ABSOLUTO ou relativo para salvar dentro de extratos/
    import os
    pasta_extratos = os.path.join(os.getcwd(), "extratos")
    os.makedirs(pasta_extratos, exist_ok=True)  # garante que a pasta existe

    caminho_arquivo = os.path.join(pasta_extratos, nome_arquivo)

    # gerar e salvar no caminho
    gerar_pdf_extrato(resultado_json, nome_arquivo=caminho_arquivo)
    
    # e retornar para download no navegador
    return FileResponse(caminho_arquivo, media_type="application/pdf", filename=nome_arquivo)

