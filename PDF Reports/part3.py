from fpdf import FPDF

title = "PDF Creation Tutorial"

class PDF(FPDF):
    def header(self):
        
        self.set_font("helvetica", "B", 15)

        #Calculate the width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w)/2)

        #Set colors of frame, background and text
        self.set_draw_color(0, 80, 180)     #border = blue
        self.set_fill_color(230, 230, 0)    #bg = yellow
        self.set_text_color(220, 50, 50)    #text = red

        #Thickness of the frame (border)
        self.set_line_width(1)

        #Title
        self.cell(title_w, 10, title, border = True, ln = True, align = "C", fill = True)
        self.ln(10)

    def footer(self):
        
        self.set_y(-15)
        self.set_font("helvetica", "I", 10)
        self.set_text_color(169,169,169)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align = "C")

    def chapter_body(self, name):

        #Reading Text File
        with open(name, "r") as fh:
            txt = fh.read().decode("latin-1")

        #Set Font
        self.set_font("times", "", 12)

        #Insert Text
        self.multi_cell(0, 5, txt)
        self.ln()



#--------------------------------------------------------------
# CREATE AN FPDF OBJECT
#--------------------------------------------------------------

pdf = PDF("P", "mm", "Letter")
pdf.alias_nb_pages()

#--------------------------------------------------------------
# EDIT THE FILE
#--------------------------------------------------------------

#Set auto page break
pdf.set_auto_page_break(auto=True, margin = 15) 

pdf.add_page()

pdf.chapter_body("Txt Files/chp1.txt")
pdf.chapter_body("Txt Files/chp2.txt")


#--------------------------------------------------------------
# CREATE (RUN) THE PFD FILE
#--------------------------------------------------------------

if __name__ == "__main__":
    pdf.output("PDF Reports/PDF Outputs/Test_part3.pdf")

