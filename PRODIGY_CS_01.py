import tkinter as tk

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + (shift if mode == 'encrypt' else -shift)) % 26
            result += chr(start + offset)
        else:
            result += char
    return result

def process_message(action):
    message = entry_message.get()
    shift = int(entry_shift.get())
    if action == 'encrypt':
        result = caesar_cipher(message, shift, 'encrypt')
    else:
        result = caesar_cipher(message, shift, 'decrypt')
    label_result.config(text=f"{action.capitalize()}ed: {result}")

root = tk.Tk()
root.title("Caesar Cipher GUI")

tk.Label(root, text="Message:").grid(row=0, column=0, padx=10, pady=5)
entry_message = tk.Entry(root, width=40)
entry_message.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Shift:").grid(row=1, column=0, padx=10, pady=5)
entry_shift = tk.Entry(root, width=5)
entry_shift.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Encrypt", command=lambda: process_message('encrypt')).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Decrypt", command=lambda: process_message('decrypt')).grid(row=2, column=1, padx=10, pady=5)

label_result = tk.Label(root, text="", wraplength=300)
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

