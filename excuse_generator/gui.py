import tkinter as tk
from excuses_loader import load_excuse, get_random_excuse 

def start_app9():
    data = load_excuse()
    
    
    root = tk.Tk()
    root.title("Excuse generator")
    root.geometry("550x400")
    root.resizable(False, False)
    
    tk.Label(root, text="Choose a language:", font=("Arial", 12)).pack(pady=10)
    language_var = tk.StringVar(value="en")
    langs = [("English", "en"), ("Українська", "uk")]
    for text, code in langs: 
        tk.Radiobutton(root, text=text, variable=language_var, value=code).pack()
        
        
    result_label = tk.Label(root, text="", wraplength=380, font=("Arial", 12), pady=10, 
                            bg="white", relief="solid", bd=1, width=50, height=4, anchor="center", justify="center")
    result_label.pack(pady=10)
    
    
    def show_excuse():
        lang = language_var.get()
        excuse = get_random_excuse(data, lang)
        result_label.config(text=excuse)
         
         
    tk.Button(root, text="Get an excuse", command=show_excuse).pack(pady=15)  
    
    
    window_width = 550
    window_height = 400
    
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    offset_y = int(screen_height * 0.2)
        
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - ( window_height // 2) - offset_y
    
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    root.mainloop()   
    
    
