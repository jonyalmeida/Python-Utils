from _tkinter import *
from _tkinter.ttk import *
from _tkinter import ttk
from _tkinter import filedialog as fd
from functions import docx_files, pic_files, text_files


class Pdf_Tool(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        self.filepath = ""
        self.options = ["Text", "Docx", "Picture", "Pdf"]

        self.selections_frame = LabelFrame(
            root, text="PDF Convertion Tool", height=100, width=100)
        self.selection_frame.grid(column=0, row=0, padx=10, pady=10)

        self.file_label = Label(self.selections_frame, text="File: ")
        self.file_label.grid(colum=0, row=0, padx=5)
        self.file_entry = Entry(self.selections_frame, width=25)
        self.file_entry.grid(column=1, row=0, padx=5)
        self.set_button = Button(
            self.selections_frame, text="Set", command=self.file_field)
        self.set_button.grid(column=2, row=0, padx=5)

        self.file_label = Label(self.selections_frame, text="Format: ")
        self.file_label.grid(column=0, row=1, padx=5)
        self.from_menu = ttk.Combobox(
            self.selections_frame, values=self.options)
        self.from_menu.current(0)
        self.convert_button = Button(
            self.selections_frame, text="Convert!", command=self.file_extension)
        self.convert_button.grid(column=2, row=1)

        self.result_label = Label(self.selections_frame, text="")
        self.result_label.grid(column=0, row=2, columnspan=3)

    def file_extension(self):
        file_ext = self.filepath.split("\\")[-1]
        file_ext = file_ext.split(".")[-1]
        file_formats = {"pdf": text_files, "png": pic_files,
                        "txt": text_files, "docx": docx_files}
        convertion()
        self.result_label.configure(text="File converted!")


if __name__ == "__main__":
    root = Tk()
    Pdf_Tool(root)
    root.mainloop()
