import tkinter as tk

def on_click(char):
    entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ゼロ割りエラー")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "エラー")

root = tk.Tk()
root.title("GUI電卓")

entry = tk.Entry(root, width=20, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(root, text='C', width=5, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)

root.mainloop()
