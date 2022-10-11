import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
#from testing import readImage
import testing
from testing import TestClass

import cv2

root=tk.Tk()
root.title("Handwritten Text Recognition")
root.geometry("500x600")
root.configure(background="sky blue")

font1=('times', 18, 'bold')
label = tk.Label(root,text='Browse Image',width=34,font=font1)  
label.place(x=10,y=5)
button = tk.Button(root, text='Upload File', width=20,command = lambda:upload_file())
button.place(x=175,y=50) 

def upload_file():
    
    global img,filename
    #f_types = [('Jpg Files', '*.jpg')]#, 'JPEG Files', '*.jpeg')]#, '*.JPEG'
    #path= "hello.jpeg"
    filename = filedialog.askopenfilename()
    img=Image.open(filename)
    #img=ImageTk.PhotoImage(Image.open(filename))
    img_resized=img.resize((400,300)) # new width & height
    img = ImageTk.PhotoImage(img_resized)
    b2 =tk.Button(root,image=img) # using Button 
    b2.place(x=45,y=150)
    
    #b2 = tk.Button(root, image = img)
    #b2.pack(fill = "both", expand = "yes")
    
    
    
    
label2=tk.Label(root,width=60,height=28)
label2.place(x=35,y=90)
    
button2 = tk.Button(root,text="Predict",width=25,command = lambda:predict())
button2.place(x=175,y=550)

def predict():
    obj = TestClass()
    print(filename)
    img=cv2.imread(filename)
    #cv2.imshow('image',img);
    obj.readImage(image_uri=filename,user_interface=root)  
    
root.mainloop()


#self.test = testLabel.TestClass()
 #       self.setImage(self.shownImage)
 #       self.initialze()


#def setStr(self,strFinal):
 #       self.strFinal = strFinal
