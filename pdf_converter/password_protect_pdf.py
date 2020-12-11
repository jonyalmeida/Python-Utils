from fpdf import FPDP
from PyPDF2 import PdfFileWriter, PdfFileReader


def encrypt_pdf(file, password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)

    # read in the pdf file
    for page in range(pdf.numPages):
        # for every page in the pdf file, add that to the new file
        parser.addPage(pdf.getPage(page))
    # opens the encrypted file
    with open(f"encrypted_{file}", "wb") as f:
        parser.write(f)
        f.close()
    print(f"encrypted_{file} Created...")


if __name__ == "__main__":
    file = "kivy.pdf"
    password = "python_genius"
    encrypt_pdf(file, password)
