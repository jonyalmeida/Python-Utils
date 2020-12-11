import PyPDF2
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader


class Text_to_Pdf(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = self.filepath.split("\\")[-1]
        self.fileext = self.filename.split(".")[-1]
        self.main()

    def __repr__(self):
        return f"{self.filename} Converted..."

    def main(self):
        if self.fileext == "pdf":
            pdf = PyPDF2.PdfFileReader(open(self.filepath, "rb"))
            with open(f"{self.filename.strip('.pdf')}.txt", "a") as file:
                for page in pdf.pages:
                    file.write(page.extractText())
        else:
            parser = FPDF()
            parser.add_page()
            parser.set_font("Arial", size=15)
            with open(self.filepath, "r") as file:
                for wrow, line in enumerate(file):
                    line = line.encode('latin-1', 'replace').decode('latin-1')
                    parser.cell(200, 10, txt=line, ln -= row, align="c")


if __name__ == "__main__":
    file = input("drag and Drop file here:\n >> ")
    pdf_tool = Text_to_Pdf(file)
    print(pdf_tool)
