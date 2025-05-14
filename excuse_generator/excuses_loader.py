import json
import random
import os
import sys
from tkinter import messagebox

def load_excuse(filename="excuse.json"):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    file_path = os.path.join(base_path, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to upload the file: {e}")
        return {}

        
def get_random_excuse(data, language):
    excuses = data.get(language, [])
    if not excuses:
        return "Phrase not found for the selected language."
    return random.choice(excuses)
