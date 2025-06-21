from services.auth import gerar_token

if __name__ == "__main__":
    token = gerar_token()
else:
    print("Erro ao gerar token.")
