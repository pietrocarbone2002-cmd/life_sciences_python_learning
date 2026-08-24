from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        #Image
        self.image("PDF Reports/Images/duck.png", 10, 8, 25)
        #Font
        self.set_font("helvetica", "B", 20)
        #Padding
        self.cell(80)
        #Title
        self.cell(30,10,"Title", border = True, ln=True, align="C")
        #Line break
        self.ln(20)

    def footer(self):
        #Set the position
        self.set_y(-15)
        #Set font
        self.set_font("helvetica", "I", 10)
        #Include Page Number
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align = "C")

#--------------------------------------------------------------
# CREATE AN FPDF OBJECT
#--------------------------------------------------------------

pdf = PDF("P", "mm", "Letter")

#Get total page number
pdf.alias_nb_pages()

#--------------------------------------------------------------
# EDIT THE FILE
#--------------------------------------------------------------

#Set auto page break
pdf.set_auto_page_break(
    auto=True, 
    margin = 15                 #How far from the bottom the break happens
) 

pdf.add_page()

pdf.set_font("helvetica", "", 16)

for i in range(1,40):
    pdf.cell(
        0,                      #Width 0 = the whole page width
        10, 
        f"This is line {i} :D", 
        ln=True                 #Makes each line appear on a new line
    )  

#--------------------------------------------------------------
# CREATE (RUN) THE PFD FILE
#--------------------------------------------------------------

if __name__ == "__main__":
    pdf.output("PDF Reports/PDF Outputs/Test_part2.pdf")