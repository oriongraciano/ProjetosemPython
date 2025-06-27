import os
import requests
from dotenv import load_dotenv
from .auth import gerar_token
from datetime import date

load_dotenv()
BASE_URL = "https://api.sicoob.com.br/conta-corrente/v4"
CONTA_CORRENTE = os.getenv("CONTA_CORRENTE")

def obter_extrato(mes, ano, dia_inicial, dia_final):
    token = gerar_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    url = f"{BASE_URL}/extrato/mes/ano"
    
    params = {
        "mes": mes.date.today().month,
        "ano": ano.date.today().year,
        "diaInicial": dia_inicial,
        "diaFinal": dia_final,
        "agruparCNAB": True,
        "numeroContaCorrente": CONTA_CORRENTE
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()
