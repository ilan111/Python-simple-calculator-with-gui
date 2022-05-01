import tkinter
from tkinter import *
from unittest import result

window = Tk()
window.title("Calculator")
window.geometry("600x600+100+200")
window.configure(bg="#171717")
window.resizable(False, False)

result_label = Label(window, width=30, height=2, text="", font=("arial", 30))
result_label.pack()

# 1st line buttons -> "C" "/" "%" "X"
Button(window, text="C", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#3697f5").place(x=10, y=100)
Button(window, text="/", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=160, y=100)
Button(window, text="%", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=310, y=100)
Button(window, text="X", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=460, y=100)

# 2nd line buttons -> "7" "8" "9" "-"
Button(window, text="7", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=10, y=200)
Button(window, text="8", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=160, y=200)
Button(window, text="9", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=310, y=200)
Button(window, text="-", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=460, y=200)

# 3d line buttons -> "4" "5" "6" "+"
Button(window, text="4", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=10, y=300)
Button(window, text="5", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=160, y=300)
Button(window, text="6", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=310, y=300)
Button(window, text="+", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=460, y=300)

# 4th line buttons -> "1" "2" "3" "="
Button(window, text="1", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=10, y=400)
Button(window, text="2", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=160, y=400)
Button(window, text="3", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=310, y=400)
Button(window, text="=", width=5, height=3, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#fe9037").place(x=460, y=400)

# 5th line buttons -> "." "0"
Button(window, text=".", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=310, y=500)
Button(window, text="0", width=11, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757").place(x=10, y=500)



window.mainloop()
