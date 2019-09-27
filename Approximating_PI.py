#Program to approximate value of PI
#pi = 3.14159265358979  .......
#Logic inspired by coading train video "https://youtu.be/5cNnf_7e92Q", just implementation in python.

import tkinter
from tkinter import *
from numpy import * #to use double
import random
import math

circ_count = 0
tot_count = 0
def calculateDistance(x1,y1,x2,y2):
    dist = double(math.sqrt(double(double(x2 - x1)**2) + double(double(y2 - y1)**2)))
    return dist
pie = 0
root = Tk()
root.title('Approximating_PI_By_RAKi')
root.geometry('600x600')
root.config(bg='white')
canvas = Canvas(root,height = 500,width = 500,bg = 'white')
canvas.place(x=0,y=0)

rect = canvas.create_rectangle(0,0,500,500,outline = 'black')
circ = canvas.create_oval(0,0,500,500,fill = 'red')
global Pi_label
Pi_label = Label(root,text = pie,bg = 'white', fg = 'blue')
Pi_label.place(x = 200,y = 550)
Label(root,text = "Approximating Pi :",bg = 'white', fg = 'blue').place(x = 200,y = 530)

while(True):
    for i in range(1,2000):
        x = random.randint(0,500)
        y = random.randint(0,500)
        tot_count+=1
        dist = calculateDistance(250,250,x,y)
        if(dist < 250):
            circ_count+=1
            canvas.create_oval(x,y,x,y,fill = 'blue',outline = 'blue')
            #root.update()
        else:
            canvas.create_oval(x,y,x,y,fill = 'green',outline = 'green')
            #root.update()
        pie = 4*(circ_count/tot_count)
        Pi_label.config(text = pie)
    
    root.update()
    print(pie)
    

root.mainloop()
