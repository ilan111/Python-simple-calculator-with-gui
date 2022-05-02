from tkinter import *


class Calculator:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("600x600+100+200")
        self.window.configure(bg="#171717")
        self.window.resizable(False, False)
        self.result_label = Label(
            self.window, width=30, height=2, text="", font=("arial", 30))
        self.result_label.pack()
        self.buttons = [
            Button(self.window, text="C", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#3697f5", command=lambda: self.clear()).place(x=10, y=100),
            Button(self.window, text="/", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("/")).place(x=160, y=100),
            Button(self.window, text="%", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("%")).place(x=310, y=100),
            Button(self.window, text="X", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("*")).place(x=460, y=100),
            Button(self.window, text="7", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("7")).place(x=10, y=200),
            Button(self.window, text="8", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("8")).place(x=160, y=200),
            Button(self.window, text="9", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("9")).place(x=310, y=200),
            Button(self.window, text="-", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("-")).place(x=460, y=200),
            Button(self.window, text="4", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("4")).place(x=10, y=300),
            Button(self.window, text="5", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("5")).place(x=160, y=300),
            Button(self.window, text="6", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("6")).place(x=310, y=300),
            Button(self.window, text="+", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("+")).place(x=460, y=300),
            Button(self.window, text="1", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("1")).place(x=10, y=400),
            Button(self.window, text="2", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("2")).place(x=160, y=400),
            Button(self.window, text="3", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("3")).place(x=310, y=400),
            Button(self.window, text="=", width=5, height=3, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#fe9037", command=lambda: self.calculate()).place(x=460, y=400),
            Button(self.window, text=".", width=5, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show(".")).place(x=310, y=500),
            Button(self.window, text="0", width=11, height=1, font=("arial", 30, "bold"),
                   bd=1, fg="#fff", bg="#575757", command=lambda: self.show("0")).place(x=10, y=500)
        ]
        self.expression = ""
        self.evaluated = False

    def show(self, val):
        symbols = ['+', '-', '/', '*', '%', '.']

        if self.evaluated and val not in symbols:
            self.expression = ""
            self.evaluated = False
            pass

        if self.expression != "":
            if val in symbols and self.expression[-1] in symbols:
                self.expression = self.expression[:-1]

            if self.expression[0] == '0' and len(self.expression) == 1 and val not in symbols:
                self.expression = ""
                self.expression += val

            else:
                self.expression += val

        else:
            if val in symbols:
                pass
            else:
                self.expression += val

        self.evaluated = False
        self.result_label.config(text=self.expression)

    def clear(self):
        self.expression = ""
        self.result_label.config(text=self.expression)

    def calculate(self):
        result = ""

        if self.expression != "":
            try:
                result = eval(self.expression)
                self.evaluated = True

            except:
                result = "error"
                self.expression = ""

        self.expression = str(result)
        self.result_label.config(text=result)


def main():
    calc = Calculator()
    calc.window.mainloop()


if __name__ == "__main__":
    main()
