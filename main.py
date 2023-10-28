from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from reportlab.pdfgen import canvas
from PIL import Image, ImageTk
import os


root = Tk()
root.title("University Card Generator")

mainframe = ttk.Frame(root, padding="6 6 24 24")
mainframe.grid(column=4, row=4, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

first_name = StringVar()
ttk.Label(mainframe, text="First name").grid(column=0, row=0, sticky=(W, E))
first_name_entry = ttk.Entry(mainframe, width=14, textvariable=first_name)
first_name_entry.grid(column=1, row=0, sticky=(W, E))

last_name = StringVar()
ttk.Label(mainframe, text="Last name").grid(column=2, row=0, sticky=(W, E))
last_name_entry = ttk.Entry(mainframe, width=14, textvariable=last_name)
last_name_entry.grid(column=3, row=0, sticky=(W, E))

roll_number = StringVar()
ttk.Label(mainframe, text="Roll Number").grid(column=0, row=2, sticky=(W, E))
roll_number_entry = ttk.Entry(mainframe, width=14, textvariable=roll_number)
roll_number_entry.grid(column=1, row=2, sticky=(W, E))

major = StringVar()
ttk.Label(mainframe, text="Major").grid(column=2, row=2, sticky=(W, E))
major_entry = ttk.Entry(mainframe, width=14, textvariable=major)
major_entry.grid(column=3, row=2, sticky=(W, E))

date = StringVar()
ttk.Label(mainframe, text="Expiry Date").grid(column=0, row=3, sticky=(W, E))
date_entry = ttk.Entry(mainframe, width=14, textvariable=date)
date_entry.grid(column=1, row=3, sticky=(W, E))

b1 = ttk.Button(mainframe, text='Upload File', width=14, command = lambda:upload_file()).grid(column=3, row=3, sticky=(W, E))
b2 = ttk.Button(mainframe, text='Generate', width=14, command = lambda:create_pdf()).grid(column=1, row=4, sticky=(W, E))
filename = './assets/dummy.png'
def upload_file():
    f_types = [('Jpg Files', '*.jpeg')]
    global filename
    filename =  filedialog.askopenfilename(filetypes=f_types)


def create_pdf():
    c = canvas.Canvas("uni_card.pdf")
    # c.setPageSize((600, 200))
    c.drawString(100, 750, f"{first_name_entry.get()}")
    c.drawString(100, 735, f"{last_name_entry.get()}")
    c.drawString(100, 705, f"{roll_number_entry.get()}")
    c.drawString(100, 675, f"{major_entry.get()}")
    c.drawString(100, 645, "Valid Upto:")
    c.drawString(100, 630, f"{date_entry.get()}")

    image_path = os.path.join(os.getcwd(), "./assets/fc_logo.png")
    left_fc_logo = os.path.join(os.getcwd(), "./assets/left_fc_logo.png")
    right_bar = os.path.join(os.getcwd(), "./assets/right_bar.jpeg")

    c.drawImage(image_path, 300, 700, width=200, height=200,  preserveAspectRatio=True, mask='auto')
    c.drawImage(left_fc_logo, -100, 620, width=200, height=180, preserveAspectRatio=True, mask='auto')
    c.drawImage(filename, 350, 580, width=160, height=200, preserveAspectRatio=True, mask='auto')
    c.drawImage(right_bar, 500, 600, width=160, height=250, preserveAspectRatio=True, mask='auto')
    print(filename)

    c.save()

create_pdf()

root.mainloop()
