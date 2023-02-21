from tkinter import *

def buttonpress(num):
    global ecuatia_text
    ecuatia_text+=str(num)
    ecuatia_label.set(ecuatia_text)
def equal():
    global ecuatia_text
    total=str(eval(ecuatia_text))
    ecuatia_label.set(total)
    ecuatia_text=total
def clear():
    ecuatia_label.set('')


windows=Tk()
windows.title('Tanase Alexandru Calculator')
windows.geometry('400x400')
ecuatia_text=""
ecuatia_label= StringVar()
label=Label(windows,textvariable=ecuatia_label,bg='white',width=40,height=3)
label.pack()
frame=Frame(windows)
frame.pack()
#butoanele cifre
button1=Button(frame,text='1',height=3,width=9,command=lambda:buttonpress(1))
button1.grid(row=0,column=0)
button2=Button(frame,text='2',height=3,width=9,command=lambda:buttonpress(2))
button2.grid(row=0,column=1)
button3=Button(frame,text='3',height=3,width=9,command=lambda:buttonpress(3))
button3.grid(row=0,column=2)
button4=Button(frame,text='4',height=3,width=9,command=lambda:buttonpress(4))
button4.grid(row=1,column=0)
button5=Button(frame,text='5',height=3,width=9,command=lambda:buttonpress(5))
button5.grid(row=1,column=1)
button6=Button(frame,text='6',height=3,width=9,command=lambda:buttonpress(6))
button6.grid(row=1,column=2)
button7=Button(frame,text='7',height=3,width=9,command=lambda:buttonpress(7))
button7.grid(row=2,column=0)
button8=Button(frame,text='8',height=3,width=9,command=lambda:buttonpress(8))
button8.grid(row=2,column=1)
button9=Button(frame,text='9',height=3,width=9,command=lambda:buttonpress(9))
button9.grid(row=2,column=2)
button0=Button(frame,text='0',height=3,width=9,command=lambda:buttonpress(0))
button0.grid(row=3,column=1)
button1plus=Button(frame,text='+',height=3,width=9,command=lambda:buttonpress('+'))
button1plus.grid(row=0,column=3)
button1min=Button(frame,text='-',height=3,width=9,command=lambda:buttonpress('-'))
button1min.grid(row=1,column=3)
button1div=Button(frame,text='\\',height=3,width=9,command=lambda:buttonpress('\\'))
button1div.grid(row=2,column=3)
button1in=Button(frame,text='*',height=3,width=9,command=lambda:buttonpress('*'))
button1in.grid(row=3,column=3)
buttonclear=Button(frame,text='clear',height=3,width=9,command=lambda:clear())
buttonclear.grid(row=4,column=1)
buttonn1=Button(frame,text='=',height=3,width=9,command=lambda:equal())
buttonn1.grid(row=3,column=0)
buttonn=Button(frame,text=',',height=3,width=9,command=lambda:buttonpress('.'))
buttonn.grid(row=3,column=2)





windows.mainloop()