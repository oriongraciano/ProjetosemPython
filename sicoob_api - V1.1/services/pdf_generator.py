from fpdf import FPDF
import os

def gerar_pdf(dados, nome_arquivo):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Extrato Bancário Sicoob", ln=True, align="C")

    for item in dados.get("lancamentos", []):
        pdf.cell(200, 10, txt=str(item), ln=True)

    path = os.path.join("app", "output")
    os.makedirs(path, exist_ok=True)
    caminho_arquivo = os.path.join(path, nome_arquivo)
    pdf.output(caminho_arquivo)

    return caminho_arquivo
