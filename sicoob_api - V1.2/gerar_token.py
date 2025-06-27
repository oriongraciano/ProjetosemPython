from services.auth import gerar_token

if __name__ == "__main__":
    token = gerar_token()
    print("TOKEN GERADO COM SUCESSO:")
    print(token)
else:
    print("Erro ao gerar token.")
