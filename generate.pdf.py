from fpdf import FPDF

title = 'THINK PYTHON: How to Think Like a Computer Scientist'

class PDF(FPDF):
    def header(self):
        # Arial bold 16
        self.set_font('Arial', 'B', 16)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        # 
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 120, 210)
        self.set_fill_color(200, 200, 0)
        self.set_text_color(225, 55, 55)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 10
        self.set_font('Arial', 'I', 10)
        # Text color in gray
        self.set_text_color(128)
        # Insert Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Font: Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

pdf = PDF()
pdf.set_title(title)
pdf.set_author('Allen Downey')
pdf.print_chapter(1, 'The way of the program', 'think_python_chapter1.txt')
pdf.print_chapter(2, 'Variables, expressions and statements', 'think_python_chapter2.txt')
pdf.output('think_python.pdf', 'F')