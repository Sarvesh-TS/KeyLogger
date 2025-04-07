# 🔐 Python Keylogger (Educational Use Only)

> **⚠️ WARNING:** This tool is strictly for **educational purposes only**. Do **not** use it without proper authorization. Unauthorized monitoring of devices may be illegal and unethical.

## 📋 Description

This is a Python-based keylogger that captures keystrokes in real-time, logs them to a file, and periodically sends the logs via email. It includes stealth mode to hide the console window on Windows systems.

## 🚀 Features

- Captures keystrokes including special keys.
- Saves logs in timestamped `.log` files inside a `logs/` directory.
- Sends logs to a specified email at regular intervals.
- Stealth mode hides the console window (Windows only).
- Simple and extensible structure.

## ⚙️ Requirements

- Python 3.x
- Modules:
  - `pynput`
  - `smtplib`
  - `email`
  - `threading`
  - `pywin32` (only for Windows stealth mode)

Install dependencies:
```bash
pip install pynput pywin32
```

## 🛠️ Configuration

Edit these variables at the top of `keylogger.py`:

```python
LOG_INTERVAL = 60  # in seconds
EMAIL_ADDRESS = "your_sender_email@gmail.com"
EMAIL_PASSWORD = "your_email_password_or_app_password"
RECEIVER_EMAIL = "your_receiver_email@gmail.com"
STEALTH_MODE = True  # Set False to see the console
```

> It's recommended to use an app-specific password for Gmail (2FA-enabled).

## ▶️ Usage

```bash
python keylogger.py
```

The program will:
- Start capturing keystrokes.
- Send logs to your email every `LOG_INTERVAL` seconds.
- Run in the background (stealth mode on Windows).

## 📁 Output

- Logs are saved in the `logs/` directory.
- Email reports contain plain text logs of captured keystrokes.

## ❌ Exit

To stop the keylogger:
- Press `Ctrl+C` in the terminal.
- Or terminate the script from Task Manager / Activity Monitor.

## 🛡️ Disclaimer

This script is intended for **educational** and **authorized** security research only. The author is not responsible for any misuse of this tool.

