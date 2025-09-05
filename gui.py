"""
Improved GPT-OSS Programming Tutor GUI using Tkinter
Design: Modern AI Chatbox (ChatGPT / Copilot inspired)
Enhanced with color-coded messages for clarity
"""

import tkinter as tk
from tkinter import scrolledtext, ttk
import importlib.util
import os, threading, queue, time, re


class TutorGUI:
    def __init__(self, root):
        self.root = root
        self.tutor = None
        self.response_queue = queue.Queue()
        self.setup_gui()
        self.load_tutor_framework()

    def setup_gui(self):
        """Setup Tkinter GUI"""
        self.root.title("🤖 GPT-OSS Programming Tutor")
        self.root.geometry("950x750")
        self.root.configure(bg="#202123")

        # Header
        header = tk.Label(
            self.root,
            text="GPT-OSS Programming Tutor",
            font=("Segoe UI", 16, "bold"),
            fg="white", bg="#343541", pady=12
        )
        header.pack(fill=tk.X)

        # Chat area
        self.chat_text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, font=("Consolas", 11),
            bg="#2B2B2B", fg="white", insertbackground="white",
            padx=12, pady=12
        )
        self.chat_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
        self.chat_text.insert(tk.END, self.get_welcome_message())
        self.chat_text.config(state=tk.DISABLED)

        # Add text tags for colors
        self.chat_text.tag_configure("user", foreground="#61afef", font=("Consolas", 11, "bold"))
        self.chat_text.tag_configure("user_msg", foreground="#61afef")
        self.chat_text.tag_configure("tutor", foreground="#98c379", font=("Consolas", 11, "bold"))
        self.chat_text.tag_configure("tutor_msg", foreground="#98c379")
        self.chat_text.tag_configure("error", foreground="#e06c75", font=("Consolas", 11, "bold"))
        self.chat_text.tag_configure("info", foreground="#abb2bf", font=("Consolas", 11, "italic"))
        self.chat_text.tag_configure("code", foreground="#e5c07b", background="#3e4451")

        # Input frame
        input_frame = tk.Frame(self.root, bg="#202123")
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 5))

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            input_frame, textvariable=self.input_var,
            font=("Segoe UI", 12), bg="#40414f", fg="white",
            insertbackground="white", relief="flat"
        )
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 8))

        # 🔹 Pressing Enter triggers send_message
        self.input_entry.bind("<Return>", lambda e: self.send_message())

        send_btn = tk.Button(
            input_frame, text="Send",
            font=("Segoe UI", 11, "bold"),
            bg="#10a37f", fg="white",
            activebackground="#0e8c6d",
            relief="flat", padx=15, pady=5,
            command=self.send_message
        )
        send_btn.pack(side=tk.RIGHT)

        # Quick examples dropdown
        examples = [
            "Create a BankAccount class",
            "Write a recursive Fibonacci function",
            "Count lines in a text file",
            "Validate email addresses using regex",
            "Check if a number is prime",
            "Merge two dictionaries",
            "Write a list of strings to a file",
        ]
        examples_frame = tk.Frame(self.root, bg="#202123")
        examples_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(examples_frame, text="💡 Quick Examples:",
                 font=("Segoe UI", 10), fg="white", bg="#202123").pack(side=tk.LEFT)

        self.example_var = tk.StringVar()
        example_combo = ttk.Combobox(
            examples_frame, textvariable=self.example_var,
            values=examples, width=60, state="readonly"
        )
        example_combo.pack(side=tk.LEFT, padx=(10, 0))
        example_combo.bind("<<ComboboxSelected>>", self.on_example_selected)

        # Bottom status bar
        self.status_var = tk.StringVar(value="✅ Ready")
        status_bar = tk.Label(
            self.root, textvariable=self.status_var,
            font=("Segoe UI", 9), anchor="w",
            fg="white", bg="#343541", pady=4
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def get_welcome_message(self):
        welcome = "═══════════════════════════════════════════════════════════════\n"
        welcome += "🤖 Welcome to GPT-OSS Programming Tutor!\n"
        welcome += "Ask me about Python code, algorithms, OOP, files, regex, etc.\n"
        welcome += "═══════════════════════════════════════════════════════════════\n"
        return welcome

    def load_tutor_framework(self):
        """Load tutor from external file (tutor9.py)"""
        try:
            framework_path = r"C:\Users\user\Downloads\python_tutor\tutor.py"
            if not os.path.exists(framework_path):
                self.status_var.set("❌ Framework not found!")
                return False

            spec = importlib.util.spec_from_file_location("tutor_framework", framework_path)
            tutor_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(tutor_module)

            tutor_class = getattr(tutor_module, "CompleteGPTOSSTutor", None)
            if tutor_class:
                self.tutor = tutor_class()
                self.status_var.set("✅ Framework loaded successfully")
                return True
            else:
                self.status_var.set("❌ Tutor class not found")
                return False
        except Exception as e:
            self.status_var.set(f"❌ Load error: {str(e)}")
            return False

    def send_message(self):
        query = self.input_var.get().strip()
        if not query:
            return
        # Insert user message and stay at that position
        self.update_chat("user", query, autoscroll=False)
        self.input_var.set("")
        self.status_var.set("⏳ Thinking...")

        thread = threading.Thread(target=self.process_response, args=(query,), daemon=True)
        thread.start()

    def process_response(self, query):
        try:
            if not self.tutor:
                self.response_queue.put(("error", "Tutor not loaded"))
                return
            response = self.tutor.generate_response(query)
            self.response_queue.put(("tutor", response))
        except Exception as e:
            self.response_queue.put(("error", str(e)))

    def update_chat(self, sender, message, autoscroll=True):
        self.chat_text.config(state=tk.NORMAL)
        timestamp = time.strftime("%H:%M:%S")

        if sender == "user":
            self.chat_text.insert(tk.END, f"\n[{timestamp}] 🧑 You:\n", "user")
            self.chat_text.insert(tk.END, f"{message}\n", "user_msg")
        elif sender == "tutor":
            formatted = self.format_code_response(message)
            self.chat_text.insert(tk.END, f"\n[{timestamp}] 🤖 Tutor:\n", "tutor")
            self.chat_text.insert(tk.END, f"{formatted}\n", "tutor_msg")
        elif sender == "error":
            self.chat_text.insert(tk.END, f"\n[{timestamp}] ❌ Error: {message}\n", "error")

        # 🔹 Only autoscroll for tutor messages, not for user input
        if autoscroll:
            self.chat_text.see(tk.END)

        self.chat_text.config(state=tk.DISABLED)

    def format_code_response(self, response):
        """Format tutor output with code highlighting"""
        response = re.sub(r"\x1b\[[0-9;]*m", "", response)
        lines, formatted = response.split("\n"), []
        code_mode = False
        for line in lines:
            if line.strip().startswith("```python"):
                code_mode = True
                self.chat_text.insert(tk.END, "\n╔════════ CODE ════════\n", "code")
            elif line.strip() == "```":
                code_mode = False
                self.chat_text.insert(tk.END, "╚═══════════════════════\n", "code")
            else:
                if code_mode:
                    self.chat_text.insert(tk.END, f"    {line}\n", "code")
                else:
                    formatted.append(line)
        return "\n".join(formatted)

    def on_example_selected(self, event):
        example = self.example_var.get()
        self.input_var.set(example)
        self.example_var.set("")

    def check_queue(self):
        try:
            while True:
                sender, content = self.response_queue.get_nowait()
                # Tutor responses still autoscroll
                self.update_chat(sender, content, autoscroll=True)
                self.status_var.set("✅ Ready")
        except queue.Empty:
            pass
        self.root.after(100, self.check_queue)


def main():
    root = tk.Tk()
    app = TutorGUI(root)
    root.after(100, app.check_queue)
    root.mainloop()


if __name__ == "__main__":
    main()
