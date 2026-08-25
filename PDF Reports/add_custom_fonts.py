from fpdf import FPDF

#--------------------------------------------------------------
# CREATE AN FPDF OBJECT
#--------------------------------------------------------------

pdf = FPDF("P", "mm", "Letter")

#Adding system fonts
#Search bar -> "run" -> fonts -> copy path
pdf.add_font("Impact Standard", "",
             r"C:\Windows\Fonts\impact.ttf",
             uni=True)

#Google Fonts

pdf.add_font("Lato Black", "",
             r"PDF Reports\Fonts\Lato-Black.ttf",
             uni=True)

pdf.add_font("Lato Regular", "",
             r"PDF Reports\Fonts\Lato-Regular.ttf",
             uni=True)


#--------------------------------------------------------------
# ADD A PAGE AND FONT
#--------------------------------------------------------------

pdf.add_page()

pdf.set_font("Lato Regular", "", 16)
pdf.set_text_color(220,50,50)    #RGB

pdf.cell(120, 10, "Hello World", ln = True)  


pdf.set_font("Lato Black", "", 16)
pdf.cell(80, 100, "Goodbye World", border = True)            
#--------------------------------------------------------------
# CREATE (RUN) THE PFD FILE
#--------------------------------------------------------------

if __name__ == "__main__":
    pdf.output("PDF Reports/PDF Outputs/Test_custom_font.pdf")