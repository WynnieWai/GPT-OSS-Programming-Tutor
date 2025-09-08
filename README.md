# GPT-OSS-Programming-Tutor: Local & Private Python Programming Tutor  

**Hackathon Submission for GPT-OSS Hackathon - Best Local Agent & For Humanity**  

GPT-OSS-Programming-Tutor is a powerful, offline AI programming assistant that leverages the **GPT-OSS-20B tokenizer** for advanced query analysis. It provides detailed code examples and explanations for a wide range of Python concepts, running entirely on your local machine.  

No API keys, no internet connection, and no data ever leaves your computer.  

---

## 🚀 Hackathon Submission Details
- **Categories**: Best Local Agent, For Humanity  
- **GPT-OSS Component Used**: gpt-oss-20b Tokenizer  
- **Team**: Individual Submission  
- **Video Demo**: [Link to your demonstration video here]  

---

## ✨ Features
- 🧠 **GPT-OSS Tokenizer Analysis**: Uses the GPT-OSS-20B tokenizer for sophisticated query processing and token counting.  
- 🔒 **Absolute Privacy**: All processing happens locally — ideal for sensitive environments where code cannot leave your machine.  
- 📚 **Comprehensive Knowledge Base**: Covers OOP, algorithms, file operations, web scraping, data validation, and more.  
- 🎯 **Smart Pattern Matching**: Advanced regex-based matching system to find the most relevant code examples.  
- 💻 **Dual Interface**: Choose between a clean command-line interface (`tutor.py`) or a graphical user interface (`gui.py`).  

---

## 🗂️ Project Structure
```
.
├── tutor.py              # Main command-line tutor application
├── gui.py                # Graphical user interface version
├── knowledge_base.py     # Comprehensive programming knowledge base
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

---

## 📋 Prerequisites
- Python 3.8 or higher  
- ~40 GB of free disk space for the GPT-OSS-20B model  
- At least 8 GB of RAM  

---

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/WynnieWai/GPT-OSS-Programming-Tutor.git
cd GPT-OSS-Programming-Tutor
```

### 2. Create a Virtual Environment
```bash
# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# On Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat

# On Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install transformers colorama
```

### 4. Download the GPT-OSS-20B Model
Required for tokenizer functionality:  
1. Visit the official model page: https://huggingface.co/openai/gpt-oss-20b  
2. Download the model to your local machine:
```bash
git lfs install
git clone https://huggingface.co/openai/gpt-oss-20b
```
⚠️ Note: The download is large (~40 GB) and will take time.  

3. Verify the path in `tutor.py` matches your download location:  
```python
MODEL_PATH = r"C:\Users\user\Downloads\python_tutor\gpt-oss-20b"
```

---

## 🚀 Usage

### Command Line Interface (Recommended)
```bash
python tutor.py
```

### Graphical User Interface
```bash
python gui.py
```

### Example Queries
- Create a BankAccount class with deposit and withdraw methods  
- Write a function to find the maximum of three numbers  
- How do I validate an email address with regex?  
- Show me how to scrape titles from a webpage  
- Write a function to check if a number is prime  

Type `exit`, `quit`, or `bye` to end the session in CLI mode.  

---

## 🔧 How It Works
1. **Query Analysis**: User input is processed using the GPT-OSS-20B tokenizer for token counting and analysis.  
2. **Pattern Matching**: Regex patterns match the query against the knowledge base.  
3. **Response Generation**: Retrieves the most relevant code example with explanations.  
4. **Local Processing**: All operations occur entirely on your local machine — no data leaves.  

---

## 🌍 For Humanity: Our Impact
- **Democratizing Access**: Free forever after initial model download.  
- **Secure Development**: Safe for regulated industries (healthcare, finance, defense).  
- **Offline Learning**: Works in areas without internet, enabling global access.  
- **Cost Reduction**: No API costs or cloud fees.  

---

## 📜 License
This project is licensed under the **MIT License** — see [Apache 2.0 License details](https://choosealicense.com/licenses/apache-2.0/).  
> Note: The GPT-OSS-20B model weights are governed by their own license from OpenAI.  

---

## 🙏 Acknowledgments
- **OpenAI** for GPT-OSS-20B model  
- **Hugging Face** for `transformers` library and hosting  
- Hackathon organizers for pushing the frontier of open models  
