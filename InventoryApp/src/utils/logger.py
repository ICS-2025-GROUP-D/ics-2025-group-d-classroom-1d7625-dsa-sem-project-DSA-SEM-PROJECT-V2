from datetime import datetime

def log_event(message):  # 👈 this must accept one parameter
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}")
