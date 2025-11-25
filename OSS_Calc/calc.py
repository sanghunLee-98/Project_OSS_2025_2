import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x420")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 새로 추가한 기능 버튼: x², 1/x, |x|
        buttons = [
            ['x²', '1/x', '|x|', 'C'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""

        # 새 기능: 제곱
        elif char == 'x²':
            try:
                if self.expression == "":
                    return
                value = eval(self.expression)
                self.expression = str(value ** 2)
            except Exception:
                self.expression = "error"

        # 새 기능: 역수
        elif char == '1/x':
            try:
                if self.expression == "":
                    return
                value = eval(self.expression)
                self.expression = str(1 / float(value))
            except Exception:
                self.expression = "error"

        # 새 기능: 절댓값
        elif char == '|x|':
            try:
                if self.expression == "":
                    return
                value = eval(self.expression)
                self.expression = str(abs(float(value)))
            except Exception:
                self.expression = "error"

        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "error"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
