import tkinter as tk
from tkinter.filedialog import askopenfile
import PyPDF2

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
# logo = Image.open('logo.JPG')
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=1, row=0)

instructions = tk.Label(root, text="Deneme programi")
instructions.grid(columnspan=3, column=0, row=0)
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(),
                       bg="#20bebe", fg="white", width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


def open_file():
    browse_text.set("loading..")
    file = askopenfile(parent=root, mode='rb', title="choose file ", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf=PyPDF2.PdfFileReader(file)
        page=read_pdf.getPage(0)
        page_content = page.extractText()
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")



root.mainloop()
