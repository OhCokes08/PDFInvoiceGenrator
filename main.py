import pandas as pd
import glob
import openpyxl
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_num = filename.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice Number. {invoice_num}")
    pdf.output(f"PDFs/{filename}.pdf")