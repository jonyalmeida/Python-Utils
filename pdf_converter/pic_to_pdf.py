import os
import pdf2image
from PIL import Image
from pdf2image import convert_from_path


class Pic_to_Pdf(object):
    def __init__(self, filepath):
        self.filepath = filepath.split("\\")
        self.filename = self.filepath[-1]
        self.fileext = self.filename.split(*self.filepath)
        self.main()

    def __repr__(self):
        return f"{self.filename} Converted..."

    def main(self):
        if self.fileext == "pdf":
            pages = convert_from_path(self.filepath, 500)
            for page in pages:
                page.save(self.file_path.replace(".pdf", ".png"), "PNG")
        else:
            picture = Image.open(self.filepath)
            parsed = picture.convert("RGB")
            return parsed.save(self.file_path.replace(f".{self.fileext}", ".pdf"))


if __name__ == "__main__":
    print("\nDrag and Drop file here: ")
    file = input(r" >> ")
    pdf_tool = Pic_to_Pdf(file)
    print(pdf_tool)
