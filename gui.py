from tkinter import *
from tkinter import scrolledtext
from pymedia import video_check

def getffmpeg():
    filename = filedialog.askopenfilename()
    txt2.insert(0, filename)

def getvideodir():
    dirname = filedialog.askdirectory()
    txt1.insert(0, dirname)

def do_check():
    dirname = txt1.get()
    ffmpeg = txt2.get()
    #txtfield.insert(INSERT, dirname)
    #txtfield.insert(INSERT, ffmpeg)
    video_check(ffmpeg, dirname)
    txtfield.insert(INSERT, 'All Done!')

window = Tk()
window.title('Videofile parameters check')
window.geometry('680x200')
lbl = Label(window, text='Getting videofile info: codec, size, fps, color encoding.', padx=2)
txt1 = Entry(window, width=50)
btn1 = Button(window, text='Выбрать путь к папке с видеофайлами', command=getvideodir)
txt2 = Entry(window, width=50)
btn2 = Button(window, text='Выбрать путь к ffmpeg', command=getffmpeg)
txtfield = scrolledtext.ScrolledText(window, width=80, height=5)
btn3 = Button(window, text='Выполнить проверку', command=do_check)

lbl.grid(column=0, row=0, columnspan=2)
txt1.grid(column=0, row=1)
btn1.grid(column=1, row=1)
txt2.grid(column=0, row=2)
btn2.grid(column=1, row=2)
txtfield.grid(column=0, row=3, columnspan=2)
btn3.grid(column=0, row=4, columnspan=2)

window.mainloop()