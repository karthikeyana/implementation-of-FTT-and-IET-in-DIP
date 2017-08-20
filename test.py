import Tkinter as tk
import Image
import ImageTk
import numpy as np
import tkFileDialog 
import scipy.misc
import numpy, math
from scipy.misc.pilutil import Image
import math, numpy 
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image
from scipy.fftpack import rfft, irfft, fftfreq
import pylab as plt

class DIP(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent) 
        self.parent = parent        
        self.initUI()

    def initUI(self):
        self.parent.title("Digital Image Processing Application")
        self.pack(fill = tk.BOTH, expand = 1)

        menubar = tk.Menu(self.parent)
        self.parent.config(menu = menubar)

        self.label1 = tk.Label(self, border = 25)
        self.label2 = tk.Label(self, border = 25)
        self.label1.grid(row = 1, column = 1)
        self.label2.grid(row = 1, column = 2)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label = "Open", command = self.onOpen)
        menubar.add_cascade(label = "File", menu = fileMenu)
        
        basicMenu = tk.Menu(menubar)
        basicMenu.add_command(label="1DDFT",command = self.onOdft)
        basicMenu.add_command(label="2DDFT",command = self.onTdft)
        basicMenu.add_command(label="Comparision of 1DDFT,2DDFT")
        basicMenu.add_separator()
        basicMenu.add_command(label = "Negative", command = self.onNeg)
        basicMenu.add_command(label="Log Transformation",command = self.onLog)
        basicMenu.add_command(label="Power Log transformation",command = self.onPow)
        basicMenu.add_command(label="Comparision of IN,LT,PLT")
        menubar.add_cascade(label = "Basic", menu = basicMenu)

    def onOdft(self):
        I2 = abs(fftim.fft(self.I))
        I3 = fftim.fftshift(I2)
        im = Image.fromarray(np.uint8(I3))
        photo2 = ImageTk.PhotoImage(im)
        self.label2.configure(image = photo2)
        self.label2.image = photo2

    def onTdft(self):
        I2 = abs(fftim.fft2(self.I))
        I3 = fftim.fftshift(I2)
        im = Image.fromarray(np.uint8(I3))
        photo2 = ImageTk.PhotoImage(im)
        self.label2.configure(image = photo2)
        self.label2.image = photo2
        
    def onNeg(self):
        I2 = 255-self.I;
        im = Image.fromarray(np.uint8(I2))
        photo2 = ImageTk.PhotoImage(im)
        self.label2.configure(image = photo2)
        self.label2.image = photo2 

    def onLog(self):
        I2 = (255.0*numpy.log(1+self.I))/numpy.log(1+self.I)
        im = Image.fromarray(np.uint8(I2))
        photo2 = ImageTk.PhotoImage(im)
        self.label2.configure(image = photo2)
        self.label2.image = photo2

    def onPow(self):
        gamma = 0.5
        I2 = numpy.log(self.I)*gamma
        I3 = numpy.exp(I2)*255.0
        im = Image.fromarray(np.uint8(I3))
        photo2 = ImageTk.PhotoImage(im)
        self.label2.configure(image = photo2)
        self.label2.image = photo2
        
        
    def setImage(self):
        self.img = Image.open(self.fn)
        self.I = np.asarray(self.img)
        l, h = self.img.size
        text = str(2*l+100)+"x"+str(h+50)+"+0+0"
        self.parent.geometry(text)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image = photo)
        self.label1.image = photo 

    def onOpen(self):
        ftypes = [('Image Files', '*.tif *.jpg *.png')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        filename = dlg.show()
        self.fn = filename
        self.setImage()
  
def main():

    root = tk.Tk()
    DIP(root)
    root.geometry("320x240")
    root.mainloop()  


if __name__ == '__main__':
    main()
