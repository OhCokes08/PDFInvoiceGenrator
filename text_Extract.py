from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Bonus/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    doctitle = filename.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{doctitle}", ln=2)
    with open(filepath,"r") as file:
        doc = file.read()
    pdf.set_font(family="Times", size=8)
    pdf.multi_cell(w=0, h=6, txt=doc)

pdf.output("animaltext.pdf")

