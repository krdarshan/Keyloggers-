# 🛡️ Keylogger (Educational Mini Project)

This is a **simple keylogger** written in Python using the `pynput` library. It captures all keystrokes made on a system and logs them into a file (`keylogs.txt`) with timestamps.

> ⚠️ **Disclaimer**: This project is intended for **educational purposes only**. Unauthorized use of keyloggers is unethical and may be illegal. Always use responsibly.

---

## 📁 Features

- Captures normal and special key strokes (e.g., space, enter, backspace)
- Saves logs to a single file with timestamps
- Auto-stops on pressing `ESC` key
- Easy to run and extend

---

## 🚀 Getting Started

### 📦 Requirements

- Python 3.x
- `pynput` library

### 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/krdarshan/Keyloggers-.git

# Navigate into the folder
cd Keyloggers-

# Install dependencies
pip install pynput
keylogger/
├── keylogger/
│   ├── __init__.py
│   └── main.py          # Main keylogging logic
├── tests/
│   └── test_main.py     # Pytest unit tests
├── keylogs.txt          # Captured keystrokes (auto-created)
├── .gitignore
├── README.md
└── pyproject.toml       # Dependencies and configs
