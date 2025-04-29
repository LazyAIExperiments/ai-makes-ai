import requests
import tkinter as tk
from tkinter import scrolledtext

# URL of the raw .txt file on GitHub (update this to your file)
GITHUB_RAW_URL = "https://raw.githubusercontent.com/LazyAIExperiments/ai-makes-ai/refs/heads/main/predefinedset/txt.txt"

def fetch_text_from_github(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Failed to load text from GitHub:\n{e}"

def show_gui(text):
    window = tk.Tk()
    window.title("Random Sentence Generation, powered by HUMAN WRITING")
    window.geometry("600x400")

    text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(expand=True, fill='both')
    text_area.insert(tk.END, text)
    text_area.config(state='disabled')  # make it read-only

    window.mainloop()

if __name__ == "__main__":
    content = fetch_text_from_github(GITHUB_RAW_URL)
    show_gui(content)
