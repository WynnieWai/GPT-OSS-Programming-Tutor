# tutor.py
"""
Tutor - Complete GPT-OSS Programming Tutor (using external knowledge_base.py)
"""

from transformers import AutoTokenizer
from colorama import Fore, Style, init
import re
from knowledge_base import knowledge_base

init(autoreset=True)

MODEL_PATH = r"C:\\Users\\user\\Downloads\\python_tutor\\gpt-oss-20b"

class CompleteGPTOSSTutor:
    def __init__(self):
        print(Fore.YELLOW + "[INFO] Initializing Complete GPT-OSS Programming Tutor..." + Style.RESET_ALL)

        # Load GPT-OSS tokenizer
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
            print(Fore.GREEN + "[SUCCESS] GPT-OSS tokenizer loaded successfully!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[WARNING] Failed to load tokenizer: {e}" + Style.RESET_ALL)
            self.tokenizer = None

        # Load external knowledge base
        self.knowledge_base = knowledge_base
        self.conversation_history = []
        self.max_history = 5

    def analyze_with_gpt_oss_tokenizer(self, query: str) -> int:
        """Tokenize query or fallback to word count"""
        try:
            if self.tokenizer:
                return len(self.tokenizer.encode(query))
            return len(query.split())
        except Exception:
            return len(query.split())

    def find_best_match(self, query: str):
        """Simple regex-based matching"""
        query_lower = query.lower()
        for concept, data in self.knowledge_base.items():
            for pattern in data["patterns"]:
                if re.search(pattern, query_lower):
                    return concept
        return None

    def generate_response(self, query: str):
        token_count = self.analyze_with_gpt_oss_tokenizer(query)
        matched = self.find_best_match(query)
        if matched:
            data = self.knowledge_base[matched]
            return (data["code"] + "\n\n" + 
                    Fore.GREEN + "Explanation: " + Style.RESET_ALL + data["explanation"] +
                    f"\n\n{Fore.YELLOW}[Processed {token_count} tokens]{Style.RESET_ALL}")
        else:
            return f"Sorry, I don't have code for '{query}'. Try asking about Fibonacci, BankAccount class, file ops, etc."

    def chat(self):
        print(Fore.CYAN + "="*70)
        print("=== COMPLETE GPT-OSS PROGRAMMING TUTOR ===")
        print("="*70 + Style.RESET_ALL)

        while True:
            try:
                user_input = input(Fore.BLUE + "\n🎯 You > " + Style.RESET_ALL).strip()
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print(Fore.MAGENTA + "👋 Goodbye!" + Style.RESET_ALL)
                    break
                response = self.generate_response(user_input)
                print(Fore.MAGENTA + "\n🤖 Tutor > " + Style.RESET_ALL)
                print(response)
            except KeyboardInterrupt:
                print(Fore.RED + "\nExiting tutor..." + Style.RESET_ALL)
                break
            except Exception as e:
                print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    tutor = CompleteGPTOSSTutor()
    tutor.chat()
