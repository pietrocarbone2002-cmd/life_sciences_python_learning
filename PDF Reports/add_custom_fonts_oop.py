from fpdf import FPDF

title = "PDF Creation Tutorial"

class PDF(FPDF):

    def __init__(self, **kwargs):
        super(PDF, self).__init__(**kwargs)

        #Adding custom google fonts
        self.add_font("Lato Black", "",
             r"PDF Reports\Fonts\Lato-Black.ttf",
             uni=True)

        self.add_font("Lato Regular", "",
                    r"PDF Reports\Fonts\Lato-Regular.ttf",
                    uni=True)

        #Adding System Fonts
        self.add_font("Impact Standard", "",
             r"C:\Windows\Fonts\impact.ttf",
             uni=True)


    def header(self):
        
        self.set_font("Lato Black", "", 15)

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
        self.set_font("Lato Regular", "", 10)
        self.set_text_color(169,169,169)

        #Enter page counter
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align = "C")

    def chapter_title(self, chp_num, chp_title, link):

        #Set link location
        self.set_link(link)

        #Chapter Title formatting
        self.set_font("Impact Standard", "", 12)
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
        self.set_font("Lato Regular", "", 12)

        #Insert Text and line break
        self.multi_cell(0, 5, txt)
        self.ln()

        #End each chapter
        self.set_font("times", "I", 12)
        self.cell(0,5, "End of Chapter")

    def print_chapter(self, chp_num, chp_title, name, link):

        #Creates a new page for each chapter
        self.add_page()

        self.chapter_title(chp_num, chp_title, link)
        self.chapter_body(name)

#--------------------------------------------------------------
# CREATE AN FPDF OBJECT
#--------------------------------------------------------------

#For OOP Fonts you need to make the parameters arguments
pdf = PDF(orientation="P", unit="mm", format="Letter")

#--------------------------------------------------------------
# ADD METADATA
#--------------------------------------------------------------

pdf.set_title(title)
pdf.set_author("HeavenDude")


#--------------------------------------------------------------
# EDIT THE FILE
#--------------------------------------------------------------

#Get total page number
pdf.alias_nb_pages()

#Set auto page break
pdf.set_auto_page_break(auto=True, margin = 15) 

pdf.add_page()

pdf.image(
    "PDF Reports/Images/python.png", 
    x = -0.5,       #-0.5 and pdf.w + 1 make the image span along the whole page
    w = pdf.w + 1
)

#--------------------------------------------------------------
# ADD LINKS
#--------------------------------------------------------------

website = "https://github.com/pietrocarbone2002-cmd/life_sciences_python_learning"

chp1_link = pdf.add_link()
chp2_link = pdf.add_link()

#Attach list
pdf.cell(0, 10, "Text Source", ln=True, link = website)
pdf.cell(0, 10, "Chapter 1", ln=True, link = chp1_link)
pdf.cell(0, 10, "Chapter 2", ln=True, link = chp2_link)

#--------------------------------------------------------------
# CREATE (RUN) THE PFD FILE
#--------------------------------------------------------------

#Create Chapters
pdf.print_chapter(1, "Chapter 1.0", "PDF Reports/Txt Files/chp1.txt", chp1_link)
pdf.print_chapter(2, "Chapter 2.0", "PDF Reports/Txt Files/chp2.txt", chp2_link)

if __name__ == "__main__":
    pdf.output("PDF Reports/PDF Outputs/Test_custom_fonts_oop.pdf")
