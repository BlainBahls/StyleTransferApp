import os
from hashlib import new
import tkinter as tk
window=tk.Tk()
window.title(" Pythonista Planet Desktop App ")
window.geometry("600x400")
newlabel = tk.Label(text = " Visit Pythonista Planet to improve your Python skills ")
newlabel.grid(column=0,row=0)
window.mainloop()



os.system("python C:\Users\bahls\ENGT4050CapstoneFastStyle\fast-style-transfer-master\fast-style-transfer-master\evaluate.py --dir")
