from fpdf import FPDF
from datetime import datetime

class ExtratoPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Extrato Bancário - Sicoob", border=False, ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

def gerar_pdf_extrato(json_data: dict, nome_arquivo: str = "extrato.pdf"):
    pdf = ExtratoPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Saldo inicial
    pdf.cell(0, 10, f"Saldo Anterior: R$ {json_data['resultado']['saldoAnterior']}", ln=True)
    pdf.cell(0, 10, f"Saldo Atual: R$ {json_data['resultado']['saldoAtual']}", ln=True)
    pdf.cell(0, 10, f"Limite: R$ {json_data['resultado']['saldoLimite']}", ln=True)
    pdf.ln(5)

    # Cabeçalho da Tabela
    pdf.set_font("Arial", "B", 10)
    pdf.cell(25, 10, "Data", 1)
    pdf.cell(25, 10, "Tipo", 1)
    pdf.cell(40, 10, "Valor (R$)", 1)
    pdf.cell(100, 10, "Descrição", 1)
    pdf.ln()

    # Transações
    pdf.set_font("Arial", size=9)
    for transacao in json_data["resultado"]["transacoes"]:
        data_formatada = datetime.fromisoformat(transacao["data"]).strftime("%d/%m/%Y %H:%M")
        pdf.cell(25, 10, data_formatada, 1)
        pdf.cell(25, 10, transacao["tipo"], 1)
        pdf.cell(40, 10, transacao["valor"], 1)
        descricao = transacao["descricao"][:50]  # limitar para não quebrar o layout
        pdf.cell(100, 10, descricao, 1)
        pdf.ln()

    pdf.output(nome_arquivo)
