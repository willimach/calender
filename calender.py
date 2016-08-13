import tkinter as tk
from ping_lib import *
import time

tasks=[
    ['Bad&WC',    7],
    ['Mist',      7],
    ['Biomuell',   7],
    ['Bett',      10]
    ]

def myfilereader(filename):
    f=open(filename,'r')
    cfile=f.read()
    f.close()
    clines=cfile.split('\n')
    clines.pop(-1)
    return(clines)

a=1
def adder():
    global a
    a=a+1
    btn4_text.set(a)

def label_updater():
    label.config(text='  last time offline: '+str(last_down)+'\n'+'current time: '+mytime()[0]+'\n'+'up: '+speed[2]+'   dn: '+speed[3]+'   ping: '+speed[4])
    label.after(1000,label_updater)

def toggle_text(i):
    tasks.append(tasks[i])
    del tasks[i]
    btn0_text.set(tasks[0][0]), btn1_text.set(tasks[1][0]), btn2_text.set(tasks[2][0]), btn3_text.set(tasks[3][0])
    
        
last_down=myfilereader('pinglog_compressed.txt')[-1][12:30]
speed=myfilereader('speedlog.txt')[-1].split('\t')

#speed=speed.split('\t')

# define window:
root = tk.Tk()
#Fullscreen:
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

#define title:
root.title("Calender")

#define label:
label = tk.Label(root, fg="dark green")
btn0_text=tk.StringVar()
btn1_text=tk.StringVar()
btn2_text=tk.StringVar()
btn3_text=tk.StringVar()
btn4_text=tk.StringVar()
btn5_text=tk.StringVar()

label_updater()
label.pack()

h=2
#define buttons:
button0 = tk.Button(root, textvariable=btn0_text,width=100,height=h, command=lambda: toggle_text(0))
button1 = tk.Button(root, textvariable=btn1_text, width=100,height=h, command=lambda: toggle_text(1))
button2 = tk.Button(root, textvariable=btn2_text, width=100,height=h, command=lambda: toggle_text(2))
button3 = tk.Button(root, textvariable=btn3_text, width=100,height=h, command=lambda: toggle_text(3))

button4 = tk.Button(root, textvariable=btn4_text, width=100,height=h, command=adder)
button5 = tk.Button(root, textvariable=btn5_text, width=100,height=h, command=root.destroy)

btn0_text.set(tasks[0][0]), btn1_text.set(tasks[1][0]), btn2_text.set(tasks[2][0]), btn3_text.set(tasks[3][0])

btn4_text.set(a)
btn5_text.set("Stop")

button0.pack(), button1.pack(), button2.pack(), button3.pack(), button4.pack(), button5.pack()

root.mainloop()

