import tkinter as tk
from PIL import Image
import sys

from tkinter import filedialog

def UploadAction(event=None):

    filename = filedialog.askopenfilename()


    print('Selected:', filename)
    img = Image.open(filename)
    #if jpg convert to png,tiff,....
    img.save('new.ANY_FORMAT')
    #sys.exit() will close the window after the process is completed
    sys.exit()
	#example
	#img('new.jpg')
	#img('new.png')
	#img('new.tiff')

root = tk.Tk()
button = tk.Button(root, text='Open', command=UploadAction)
button.pack()


root.mainloop()
                                                                                                                                                                                                                                                                                                                                          
