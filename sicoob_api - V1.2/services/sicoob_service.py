import os
import requests
from dotenv import load_dotenv
from .auth import gerar_token

load_dotenv()

BASE_URL = "https://api.sicoob.com.br/conta-corrente/v4"

def obter_extrato(mes, ano, dia_inicial, dia_final, agrupar_cnab, numero_conta_corrente):
    token = gerar_token()
    headers = {"Authorization": f"Bearer {token}"}

    mes_formatado = f"{int(mes):02d}"
    url = f"{BASE_URL}/extrato/{mes_formatado}/{ano}"

    params = {
        "diaInicial": dia_inicial,
        "diaFinal": dia_final,
        "agruparCNAB": agrupar_cnab,
        "numeroContaCorrente": numero_conta_corrente
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
