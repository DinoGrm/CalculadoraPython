import tkinter as tk
from functools import partial

# Funções
def press(key):
    entry_text.set(entry_text.get() + str(key))

def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(str(result))
    except:
        entry_text.set("Erro")

def clear():
    entry_text.set("")

# Janela principal
root = tk.Tk()
root.title("Calculadora")
root.configure(bg="#2e2e2e")  # Modo escuro

# Campo de entrada
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=10, insertwidth=2, width=14,
                 borderwidth=4, bg="#201e1e", fg="white", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões (texto, linha, coluna)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = calculate
    elif text == 'C':
        cmd = clear
    else:
        cmd = partial(press, text)

    btn = tk.Button(root, text=text, padx=20, pady=20, bd=5, fg="white",
                    bg="#4b4b4b", font=("Arial", 14, "bold"), command=cmd)
    btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

# Layout responsivo
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
# Fim do código