from tkinter import*
window=Tk()
window.geometry("500x500")
window.resizable(0, 0)
window.configure(bg="#7A5CA7")
window.title("CALCULATOR")
#window['background']='#0B7F77'

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""
expression = ""  

input_text = StringVar()


frame=Frame(window,width=200,height=50,bd=0,bg="#eee",highlightthickness = 1)
frame.pack(side = TOP)

field = Entry(frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
field.grid(row = 0, column = 0)
field.pack(ipady = 10)

btns_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

button7=Button(btns_frame,text="7",width=8,height=4,bd=0,bg="#0B7F77", command =lambda: btn_click(7))
button7.grid(row=1,column=0)

button8=Button(btns_frame,text="8",width=8,height=4,bd=0,bg="#0B7F77", command =lambda: btn_click(8))
button8.grid(row=1,column=1)

button9=Button(btns_frame,text="9",width=8,height=4,bd=0,bg="#0B7F77", command =lambda: btn_click(9))
button9.grid(row=1,column=2)

minus=Button(btns_frame,text="-",width=8,height=4,bd=0,bg="#0B7F77",command =lambda: btn_click("-"))
minus.grid(row=1,column=3)

button4=Button(btns_frame, text="4",width=8,height=4,bg="#0B7F77",bd=0,command =lambda: btn_click(4))
button4.grid(row=2,column=0)

button5=Button(btns_frame,bd=0, text="5",width=8,height=4,bg="#0B7F77",command =lambda: btn_click(5))
button5.grid(row=2,column=1)

button6=Button(btns_frame,bd=0, text="6",width=8,height=4,bg="#0B7F77",command =lambda: btn_click(6))
button6.grid(row=2,column=2)

plus=Button(btns_frame,bd=0, text="+",width=8,height=4,bg="#0B7F77",command =lambda: btn_click("+"))
plus.grid(row=2,column=3)

button1=Button(btns_frame, text="1",width=8,height=4,bg="#0B7F77",bd=0,command =lambda: btn_click(1))
button1.grid(row=3,column=0)

button2=Button(btns_frame, text="2",width=8,height=4,bg="#0B7F77",bd=0,command =lambda: btn_click(2))
button2.grid(row=3,column=1)

button3=Button(btns_frame, text="3",width=8,height=4,bg="#0B7F77",bd=0,command =lambda: btn_click(3))
button3.grid(row=3,column=2)

mul=Button(btns_frame, text="*",width=8,height=4,bg="#0B7F77",bd=0,command =lambda: btn_click("*"))
mul.grid(row=3,column=3)

zero=Button(btns_frame,text="0",width=16,height=4,bg="#0B7F77",bd=0,command = lambda:btn_click("0"))
zero.grid(row=4,column=0,columnspan=2)

dec=Button(btns_frame,text=".",width=8,height=4,bg="#0B7F77",bd=0,command = lambda:btn_click("."))
dec.grid(row=4,column=2)

equal=Button(btns_frame,text="=",width=8,height=4,bg="#0B7F77",bd=0,command = lambda:btn_equal())
equal.grid(row=4,column=3)

clear=Button(btns_frame,text="Clear",width=26,height=4,bd=0,bg="#0B7F77",command =lambda: btn_clear())
clear.grid(row=0,column=0,columnspan=3)

div=Button(btns_frame,text="/",width=8,height=4,bd=0,bg="#0B7F77",command = lambda:btn_click("/"),)
div.grid(row=0,column=3)


window.mainloop()