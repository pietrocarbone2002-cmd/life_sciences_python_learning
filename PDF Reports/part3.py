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

        #Footer formatting
        self.set_y(-15)
        self.set_font("helvetica", "I", 10)
        self.set_text_color(169,169,169)

        #Enter page counter
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align = "C")

    def chapter_title(self, chp_num, chp_title):

        #Chapter Title formatting
        self.set_font("helvetica", "", 12)
        self.set_fill_color(200, 220, 255)

        #Chapter title
        chapter_title = f"Chapter {chp_num} : {chp_title}"
        self.cell(0, 5, chapter_title, ln=True, fill=True)
        self.ln()

    def chapter_body(self, name):

        #Reading Text File
        with open(name, "rb") as fh:
            txt = fh.read().decode("latin-1")

        #Set Font
        self.set_font("times", "", 12)

        #Insert Text and line break
        self.multi_cell(0, 5, txt)
        self.ln()

        #End each chapter
        self.set_font("times", "I", 12)
        self.cell(0,5, "End of Chapter")

    def print_chapter(self, chp_num, chp_title, name):

        #Creates a new page for each chapter
        self.add_page()

        self.chapter_title(chp_num, chp_title)
        self.chapter_body(name)

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

pdf.print_chapter(1, "Chapter 1.0", "PDF Reports/Txt Files/chp1.txt")
pdf.print_chapter(2, "Chapter 2.0", "PDF Reports/Txt Files/chp2.txt")


#--------------------------------------------------------------
# CREATE (RUN) THE PFD FILE
#--------------------------------------------------------------

if __name__ == "__main__":
    pdf.output("PDF Reports/PDF Outputs/Test_part3.pdf")

