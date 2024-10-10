from fpdf import FPDF

name = input("Your name: ")
pdf = FPDF("portrait","mm", "A4")
pdf.add_page()
pdf.image("shirtificate.png", x=10, y=70, h=200, w=190)
title = "CS50 Shirtificate"


pdf.set_font("Times", "B", 50)
pdf.cell(0, 30, f"{title}", align="C")


pdf.set_font("Times", "B", 30)
pdf.set_text_color(214, 150, 170)
pdf.set_x(50)
pdf.set_y(66)
pdf.cell(0, 150, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")      


