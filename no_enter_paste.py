# input without enter. or not a input just code from

import tkinter as tk
from tkinter import scrolledtext
import sys
import io

def execute_code(event=None):
    code = text_area.get("1.0", tk.END).strip()

    if code:
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
      
        try:
            exec(code, globals())
        except Exception as e:
            print(f"Error: {e}")
        finally:
            sys.stdout = old_stdout

        output = redirected_output.getvalue()
        output_area.config(state=tk.NORMAL)
        output_area.delete("1.0", tk.END)
        output_area.insert(tk.END, output)
        output_area.config(state=tk.DISABLED)

def on_paste(event):
    root.after(100, execute_code)

root = tk.Tk()
root.title("Paste and Execute Python Code")
bg_color = "#2e2e2e"
fg_color = "#ffffff"
insert_bg_color = "#00ff00"
output_bg_color = "#1e1e1e"
button_bg_color = "#3e3e3e"
button_fg_color = "#ffffff"

root.configure(bg=bg_color)

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, bg=bg_color, fg=fg_color, insertbackground=insert_bg_color)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, state=tk.DISABLED, bg=output_bg_color, fg=fg_color)
output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

execute_button = tk.Button(root, text="Execute", command=execute_code, bg=button_bg_color, fg=button_fg_color)
execute_button.pack(pady=10)

text_area.bind("<<Paste>>", on_paste)

root.mainloop()



