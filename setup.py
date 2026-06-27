import subprocess
import sys
import webbrowser
import os

print("Installing dependencies...")

packages = [
    "requests",
    "colorama",
    "pillow",
    "pypdf2",
    "python-whois",
    "phonenumbers"
]

for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

webbrowser.open("https://guns.lol/dayzx")

print("\nDone! Launching MultiTool...")

script_dir = os.path.dirname(os.path.abspath(__file__))
multitool_path = os.path.join(script_dir, "MultiTool.py")

subprocess.Popen([sys.executable, multitool_path])