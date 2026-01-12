import socket

HOST = "127.0.0.1"
PORT = 5000

def send_command(cmd: str):
    """Send a raw command string to C# Bonzi server"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(cmd.encode())
    s.close()

def speak(text: str):
    """Tell Bonzi to speak"""
    send_command(f"Speak:{text}")

def play(animation: str):
    """Tell Bonzi to play an animation"""
    send_command(f"Play:{animation}")
