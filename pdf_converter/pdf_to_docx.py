import os
import PyPDF2
from pdf2docx import parse


class Pdf_to_Docx(object):
    def __init__(self, filepath):
        self.filepath = filepath.split("\\")
        self.filename = self.filepath[-1]
        self.fileext = self.filename.split(".")[-1]
        self.filepath = os.path.join(*self.filepath)
        self.main()

    def __repr__(self):
        return f"{self.filename} Converted..."

    def main(self):
        if self.fileext == "pdf":
            pdf = PyPDF2.PdfFileReader(open(self.filepath, "rb"))
            with open(self.filepath.replace(".pdf", ".docx"), "a") as file:
                for page in pdf.pages:
                    file.write(page.extractText())
        else:
            new_filename = self.filepath.replace(".pdf", ".docx")
            return parse(self.filepath, new_filename, start=0, end=1)


if __name__ == "__main__":
    file = input(r"Drag and Drop file here:\n >> ")
    pdf_tool = Pdf_to_Docx(file)
    print(pdf_tool)
