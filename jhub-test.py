import os
import subprocess

print("Testing shell spawn...")
try:
    os.system("/bin/bash")
except Exception as e:
    print(f"Blocked as expected: {e}")

print("Testing package installation...")
try:
    subprocess.check_call(["pip", "install", "requests"])
except Exception as e:
    print(f"Blocked pip install: {e}")

print("Testing raw socket access...")
try:
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.connect(("8.8.8.8", 80))
except Exception as e:
    print(f"Blocked raw socket: {e}")
