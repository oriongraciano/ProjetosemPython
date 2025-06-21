from fastapi import FastAPI
from datetime import datetime
from services.sicoob_service import obter_extrato
from services.pdf_generator import gerar_pdf

app = FastAPI()

@app.get("/extrato")
def gerar_extrato_pdf():
    mes = mes.date.today().month,
    ano = ano.date.today().year,
    dia_inicial = 1
    dia_final = dia_final.date.today().day
   

    dados = obter_extrato(mes, ano, dia_inicial, dia_final)
    nome_arquivo = f"extrato_{dia_final.strftime('%Y-%m-%d')}.pdf" 
    caminho = gerar_pdf(dados, nome_arquivo)

    return {"status": "sucesso", "arquivo": caminho}
