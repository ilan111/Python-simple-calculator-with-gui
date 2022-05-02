from cmath import exp
from tkinter import *
# from unittest import result

window = Tk()
window.title("Calculator")
window.geometry("600x600+100+200")
window.configure(bg="#171717")
window.resizable(False, False)
result_label = Label(window, width=30, height=2, text="", font=("arial", 30))
result_label.pack()
expression = ""
evaluated = False


def show(val):
    global expression
    global evaluated
    symbols = ['+', '-', '/', '*', '%', '.']

    if evaluated and val not in symbols:
        expression = ""
        evaluated = False
        pass

    if expression != "":
        if val in symbols and expression[-1] in symbols:
            expression = expression[:-1]

        if expression[0]=='0' and len(expression)==1 and val not in symbols:
            expression = ""
            expression += val

        else:
            expression += val

    else:
        if val in symbols:
            pass
        else:
            expression += val

    evaluated = False
    result_label.config(text=expression)


def clear():
    global expression
    expression = ""
    result_label.config(text=expression)


def calculate():
    global expression
    global evaluated
    result = ""

    if expression != "":
        try:
            result = eval(expression)
            evaluated = True

        except:
            result = "error"
            expression = ""

    expression = str(result)
    result_label.config(text=result)


# 1st line buttons -> "C" "/" "%" "X"
Button(window, text="C", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)
Button(window, text="/", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("/")).place(x=160, y=100)
Button(window, text="%", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("%")).place(x=310, y=100)
Button(window, text="X", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("*")).place(x=460, y=100)

# 2nd line buttons -> "7" "8" "9" "-"
Button(window, text="7", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("7")).place(x=10, y=200)
Button(window, text="8", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("8")).place(x=160, y=200)
Button(window, text="9", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("9")).place(x=310, y=200)
Button(window, text="-", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("-")).place(x=460, y=200)

# 3d line buttons -> "4" "5" "6" "+"
Button(window, text="4", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("4")).place(x=10, y=300)
Button(window, text="5", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("5")).place(x=160, y=300)
Button(window, text="6", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("6")).place(x=310, y=300)
Button(window, text="+", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("+")).place(x=460, y=300)

# 4th line buttons -> "1" "2" "3" "="
Button(window, text="1", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("1")).place(x=10, y=400)
Button(window, text="2", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("2")).place(x=160, y=400)
Button(window, text="3", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("3")).place(x=310, y=400)
Button(window, text="=", width=5, height=3, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=460, y=400)

# 5th line buttons -> "." "0"
Button(window, text=".", width=5, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show(".")).place(x=310, y=500)
Button(window, text="0", width=11, height=1, font=("arial", 30, "bold"),
       bd=1, fg="#fff", bg="#575757", command=lambda: show("0")).place(x=10, y=500)


window.mainloop()
