from fastapi import FastAPI, Query, Path
from sicoob import consultar_extrato

app = FastAPI(title="API Sicoob - Consulta Extrato")

@app.get("/extrato/{mes}/{ano}")
def extrato_bancario(
    mes: int = Path(..., ge=1, le=12),
    ano: int = Path(..., ge=2000, le=2100),
    diaInicial: int = Query(..., ge=1, le=31),
    diaFinal: int = Query(..., ge=1, le=31),
    agruparCNAB: bool = Query(True),
    numeroContaCorrente: int = Query(419672)
):
    """
    Consulta o extrato bancário da conta do cooperado no Sicoob.
    """
    return consultar_extrato(mes, ano, diaInicial, diaFinal, agruparCNAB, numeroContaCorrente)
