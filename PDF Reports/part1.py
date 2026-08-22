from fpdf import FPDF

#--------------------------------------------------------------
# CREATE AN FPDF OBJECT
#--------------------------------------------------------------
#Layout:    ("P", "L")
#Unit:      ("mm", "cm", "inc")
#Format     ("A3", "A4" (default), "A5", "Letter", "Legal", (custom, custom))

pdf = FPDF("P", "mm", "Letter")

#--------------------------------------------------------------
# ADD A PAGE AND FONT
#--------------------------------------------------------------

pdf.add_page()

#specify font - ("times", "courier", "helvetica", "symbol", "zpfdongbats")
#"B" (bold), "U" (underline), "I" (italic), "" (regular), combintion (i.e. ("BU"))

pdf.set_font("helvetica", "", 16)
pdf.set_text_color(220,50,50)    #RGB

#--------------------------------------------------------------
# ADD TEXT
#--------------------------------------------------------------

#w = width
#h = height
#w and h will be in the unit format specified at the object's creation!
#ln=True tell that the next cell will be on the next line
#border=True will draw a border around the cell

pdf.cell(120, 10, "Hello World", ln = True)    #Setting the cell width high will create more space between the cells
pdf.cell(80, 100, "Goodbye World", border = True)            #Setting the cell height high will create more spece between lines

#--------------------------------------------------------------
# CREATE (RUN) THE PFD FILE
#--------------------------------------------------------------

if __name__ == "__main__":
    pdf.output("PDF Reports/Test_part1.pdf")
