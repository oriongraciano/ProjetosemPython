import os
import requests
import tempfile
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding, PrivateFormat, NoEncryption
from dotenv import load_dotenv

#Gerando AccessToken
load_dotenv()

AUTH_URL = "https://auth.sicoob.com.br/auth/realms/cooperado/protocol/openid-connect/token"
CLIENT_ID = os.getenv("CLIENT_ID")
SCOPE = "cco_extrato cco_consulta openid"
CERT_PATH = "C:/Users/orion.graciano/Desktop/InstaladoresUAU/Certificado Digital/REMO INCORPORADORA E EMPREENDIMENTOS LTDA.pfx"
CERT_PASSWORD = os.getenv("CERT_PASSWORD")

def gerar_token():
    with open(CERT_PATH, 'rb') as f:
        pfx_data = f.read()

    private_key, certificate, _ = pkcs12.load_key_and_certificates(
        pfx_data,
        CERT_PASSWORD.encode()
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pem") as cert_file:
        cert_file.write(certificate.public_bytes(Encoding.PEM))
        cert_file_path = cert_file.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".key") as key_file:
        key_file.write(private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption()
        ))
        key_file_path = key_file.name

    response = requests.post(
        AUTH_URL,
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "scope": SCOPE
        },
        cert=(cert_file_path, key_file_path),
        verify=True
    )

    os.remove(cert_file_path)
    os.remove(key_file_path)

      # Trata resposta
    if response.status_code == 200:
        token = response.json()["access_token"]
        print("TOKEN GERADO COM SUCESSO!")
    else:
        print("Erro ao obter token:", response.status_code, response.text)
        return None



#Consumindo /extrato   
def consultar_extrato(mes, ano, diaInicial, diaFinal, agruparCNAB, numeroContaCorrente):
    token = gerar_token()
    baseUrl = os.getenv("BASE_URL")
    endpoint = f"/extrato/{mes:02}/{ano}"
    url = f"{baseUrl}{endpoint}"

    headers = {
        "Authorization": f"Bearer {token}",
        "client_id": CLIENT_ID
    }

    params = {
        "diaInicial": diaInicial,
        "diaFinal": diaFinal,
        "agruparCNAB": str(agruparCNAB).lower(),
        "numeroContaCorrente": numeroContaCorrente
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao consultar extrato: {response.status_code} {response.text}")
    
    
