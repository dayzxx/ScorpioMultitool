import requests
import os
import subprocess
import platform
import socket
import threading
import webbrowser
import json
import signal
import sys
import base64
from colorama import Fore, init
import time
from PIL import Image
from PIL.ExifTags import TAGS
import PyPDF2
import whois
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

init(autoreset=True)

if os.name == "nt":
    os.system("title Scorpio Multitool by dayzx")

def flush_input():
    if os.name == "nt":
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

logo = r"""

""" + "\033[38;2;255;0;0m" + r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣶⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡀⠻⠿⣿⠿⣿⣿⣿⠏⣰⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣶⡆⠀⠀⠀⠀⠉⠀⠻⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠙⠛⣉⣭⣙⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⣉⠛⣛⣉⠁⠀⠀⢀⣤⣴⣦⣤⣀⣶⡆⣾⣿⣿⣿⣯⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡏⠀⠀⣰⠟⠉⠉⠙⢿⣿⣿⣇⢻⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡟⠀⠀⠀⠁⠀⠀⠀⠀⢸⣿⣿⣿⣦⡙⠿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢋⣩⣭⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⢠⣴⡾⣿⣿⡛⢋⠉⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠟⣉⣤⣶⣤⣤⡀⠀⠀⣴⣿⠟⠁⣩⣿⣿⣿⣿⣿⣻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢇⣾⣿⣿⣿⣿⣿⣿⡆⠺⠿⠋⢀⣾⣿⡿⢫⣾⣿⠟⢮⣝⠿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣳⣾⣷⡄⠀⠈⢿⢸⣿⣿⣿⡿⣫⣶⣿⣿⣿⣷⣄⢻⡿⢋⣴⣿⣿⠟⣠⣴⡿⠷⣟⣯⣤⣶⡶⣶⣄⡀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡿⠃⠈⠛⢿⣦⣀⣈⡈⢿⣿⡟⣼⣿⣿⣿⣿⣿⠿⣛⣃⣀⣘⠿⠟⢣⣾⣿⡿⠃⣴⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⣼⡿⠋⠉⠀⠀⠀⠀⠀⠘⠿⣸⠧⡄⠻⠁⣿⣿⣿⣿⢏⣴⣿⣿⣿⣿⣿⣷⣄⢻⡟⠋⠀⣼⣿⣿⣿⠋⠉⠵⠿⣿⣿⣿⣿⣿⢋⣷⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⠋⠀⢠⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⣶⣶⣆⣻⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠁⣀⣠⣴⣮⢻⠇⠀⣷⡄⠀⠀⠹⣿⣿⣷⣿⣿⣿⣿⣷⣤⡀⠀
⠀⠀⠀⠀⣿⡇⠀⢰⣯⣽⠉⠉⢩⣍⣉⣉⣩⣭⣥⣭⣍⣻⣥⣭⣭⣜⠿⣿⣿⣿⣿⣿⣿⣿⠿⢛⡸⢿⣿⣿⡿⠀⠀⠀⢹⣷⣀⣀⠀⠀⠁⢿⣿⣿⣿⣿⣿⣿⣿⣆
⠀⠀⢀⣼⠿⠃⠀⢸⣿⡇⠀⢸⣿⠻⠟⠿⠿⠿⠿⢿⣿⣿⠋⠛⣻⣭⣴⣶⣄⠉⠛⠿⠟⢫⣾⣿⣿⣆⣀⡈⠀⠀⠀⠀⠀⠉⠛⠉⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿
⣠⡴⠟⠛⠁⠀⠀⢸⣿⡧⠀⣾⣿⡀⠀⢠⣼⡻⣿⣿⣿⣿⣿⣿⠎⣿⠿⠟⠃⣀⣴⣿⣿⠈⣙⡻⠿⠃⢾⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⢿⣿⡇⠀⣼⣿⡇⠉⠙⠛⠋⠉⠀⠀⠀⠀⠀⣾⡛⠻⣿⡇⠀⣿⣧⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠿⠿⠃⠀⢠⣤⣴⡆
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⢸⣿⡇⠀⣿⣿⡇⠀⠀⠀⣠⠾⠛⢿⣿⣷⣿⣿⣿⣧⠹⠃⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇⠀⠀⠀⠀⣼⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠇⢸⣶⡅⢐⡿⠏⠀⠀⠀⢀⣴⣿⣷⡌⠿⠿⠿⠿⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡏⠀⠀⠀⠀⢀⣤⣿⣿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠜⠋⠀⠀⠀⢻⣧⠘⣿⣦⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢀⣼⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡏⠀⠘⢿⣧⠀⢸⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠛⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠟⠀⠀⠀⢰⣿⠆⢸⣿⣿⣿⣿⢿⣿⣧⣤⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⢸⣿⣿⡿⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣠⣤⣤⣤⣤⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⣿⣿⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠇⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣉⠉⠻⠋⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⠿⠋⢰⣿⣿⣧⣦⡀⣀⣴⣶⣤⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    
                  ____                       _        
                 / ___|  ___ ___  _ __ _ __ | | ___   
                 \___ \ / __/ _ \| '__| '_ \| |/ _ \ 
                  ___) | (_| (_) | |  | |_) |_| (_) | 
                 |____/ \___\___/|_|  | .__/(_)\___/ 
                                      |_|             

""" + "\033[90;5;26;0;0m" + " ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"


# ---------------- CLEAR ----------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------- PING ----------------
def ping_host(ip):
    system = platform.system().lower()
    if system == "windows":
        command = ["ping", "-n", "1", "-w", "1000", ip]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

# ---------------- PORT CHECK ----------------
def check_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

# ---------------- PORT SCANNER ----------------
def scan_ports(ip, ports):
    open_ports = []

    def worker(port):
        if check_port(ip, port):
            print(f"{Fore.GREEN}[OPEN] {port}")
            open_ports.append(port)

    threads = []
    try:
        for port in ports:
            t = threading.Thread(target=worker, args=(port,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("\nScan stopped.")

    return open_ports


# ---------------- MAIN LOOP ----------------
while True:
    clear()
    print(logo)
    print()
    print("[1] Ip Lookup        [5] URL Shortener    [9] Whois Lookup")
    print("[2] Webhook Sender   [6] Username Lookup  [10] Phone Lookup")
    print("[3] Ip Pinger        [7] Metadata Scanner [11] Reverse Img")
    print("[4] Port Scanner     [8] DNS Lookup\n")

    x = input("Option: ")
    x = x.strip()

    # -------- IP LOOKUP --------
    if x == "1":
        clear()
        ip = input("Enter IP: ")
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            data = r.json()
            if data.get("status") == "success":
                print("\nRESULTS\n")
                print(f"Country: {data['country']}")
                print(f"Region: {data['regionName']}")
                print(f"City: {data['city']}")
                print(f"Zip: {data['zip']}")
                print(f"Timezone: {data['timezone']}")
                print(f"Lat: {data['lat']}")
                print(f"Lon: {data['lon']}")
                print(f"Isp: {data['isp']}")
                print(f"As: {data['as']}")
            else:
                print("Invalid IP.")
        except Exception as e:
            print("Error:", e)
        input("\nPress enter...")

    # -------- WEBHOOK --------
    elif x == "2":
        clear()
        url = input("Webhook URL: ")
        message = input("Message: ")
        name = input("Webhook Name: ")
        try:
            requests.post(url, json={"content": message, "username": name})
            print("Sent.")
        except:
            print("Error sending.")
        input("\nPress enter...")

    # -------- PINGER --------
    elif x == "3":
        clear()
        ip = input("Enter IP: ")
        port = input("Port (optional): ")
        port = int(port) if port else None
        print("\nCtrl+C to stop\n")
        try:
            while True:
                if port:
                    if check_port(ip, port):
                        print(f"{Fore.GREEN}{ip}:{port} OPEN")
                    else:
                        print(f"{Fore.RED}{ip}:{port} CLOSED")
                else:
                    if ping_host(ip):
                        print(f"{Fore.GREEN}{ip} ONLINE")
                    else:
                        print(f"{Fore.RED}{ip} OFFLINE")
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nStopped.")
            time.sleep(0.3)
            input("Press enter to return...")

    # -------- PORT SCANNER --------
    elif x == "4":
        clear()
        ip = input("Enter IP: ")
        print("\n[1] Common ports")
        print("[2] Custom range")
        choice = input("Choice: ")
        if choice == "1":
            ports = [21,22,23,25,53,80,110,139,143,443,445,3389]
        elif choice == "2":
            start = int(input("Start: "))
            end = int(input("End: "))
            ports = range(start, end+1)
        else:
            continue
        print("\nScanning... Ctrl+C to stop\n")
        open_ports = scan_ports(ip, ports)
        print("\nDone.")
        print("Open ports:", open_ports)
        input("\nPress enter...")

    # -------- URL SHORTENER --------
    elif x == "5":
        clear()
        url = input("Enter URL: ")
        try:
            r = requests.get(f"http://tinyurl.com/api-create.php?url={url}", timeout=5)
            if r.status_code == 200:
                print(f"\nShortened URL: {r.text}")
            else:
                print("Error shortening URL.")
        except Exception as e:
            print("Error:", e)
        input("\nPress enter...")

    # -------- USERNAME LOOKUP --------
    elif x == "6":
        clear()
        username = input("Enter username: ").strip()
        if not username:
            print("No username entered.")
            input("\nPress enter...")
        else:
            sites = {
                "GitHub": f"https://github.com/{username}",
                "Reddit": f"https://www.reddit.com/user/{username}",
                "Twitter/X": f"https://twitter.com/{username}",
                "Instagram": f"https://www.instagram.com/{username}",
                "TikTok": f"https://www.tiktok.com/@{username}",
                "Twitch": f"https://www.twitch.tv/{username}",
                "YouTube": f"https://www.youtube.com/@{username}",
                "Pinterest": f"https://www.pinterest.com/{username}",
                "Steamcommunity": f"https://steamcommunity.com/id/{username}",
                "Spotify": f"https://open.spotify.com/user/{username}",
                "Snapchat": f"https://www.snapchat.com/add/{username}",
                "LinkedIn": f"https://www.linkedin.com/in/{username}",
                "Facebook": f"https://www.facebook.com/{username}",
                "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
                "Minecraft": f"https://namemc.com/profile/{username}",
                "Discord": f"https://discord.com/users/{username}",
                "Telegram": f"https://t.me/{username}",
                "Medium": f"https://medium.com/@{username}",
                "Pastebin": f"https://pastebin.com/u/{username}",
                "SoundCloud": f"https://soundcloud.com/{username}",
                "Flickr": f"https://www.flickr.com/people/{username}",
                "Tumblr": f"https://www.tumblr.com/{username}",
                "DeviantArt": f"https://www.deviantart.com/{username}",
                "Kick": f"https://kick.com/{username}",
                "TryHackMe": f"https://tryhackme.com/p/{username}",
                "HackTheBox": f"https://app.hackthebox.com/profile/{username}",
            }

            print(f"\nSearching for '{username}'...\n")

            for site, url in sites.items():
                try:
                    r = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
                    if r.status_code == 200:
                        print(f"{Fore.GREEN}[FOUND] {site}: {url}")
                    else:
                        print(f"{Fore.RED}[NOT FOUND] {site}")
                except:
                    print(f"{Fore.YELLOW}[ERROR] {site}")

            input("\nPress enter...")

    # -------- METADATA SCANNER --------
    elif x == "7":
        clear()
        flush_input()
        path = input("Enter file path (.jpg/.png/.pdf): ").strip().strip('"')
        while not path:
            path = input("Enter file path (.jpg/.png/.pdf): ").strip().strip('"')

        try:
            if path.lower().endswith((".jpg", ".jpeg", ".png")):
                img = Image.open(path)
                exif_data = img._getexif()
                if exif_data:
                    print(f"\n{Fore.CYAN}EXIF Metadata:\n")
                    for tag_id, value in exif_data.items():
                        tag = TAGS.get(tag_id, tag_id)
                        if tag == "GPSInfo":
                            try:
                                gps = value
                                lat = gps[2]
                                lat_ref = gps[1]
                                lon = gps[4]
                                lon_ref = gps[3]
                                lat_deg = lat[0] + lat[1]/60 + lat[2]/3600
                                lon_deg = lon[0] + lon[1]/60 + lon[2]/3600
                                if lat_ref == "S":
                                    lat_deg = -lat_deg
                                if lon_ref == "W":
                                    lon_deg = -lon_deg
                                lat_deg = round(float(lat_deg), 6)
                                lon_deg = round(float(lon_deg), 6)
                                print(f"{Fore.GREEN}Latitude:  {Fore.WHITE}{lat_deg}")
                                print(f"{Fore.GREEN}Longitude: {Fore.WHITE}{lon_deg}")
                                print(f"{Fore.GREEN}Maps:      {Fore.WHITE}https://maps.google.com/?q={lat_deg},{lon_deg}")
                            except:
                                print(f"{Fore.GREEN}GPSInfo: {Fore.WHITE}{value}")
                        else:
                            print(f"{Fore.GREEN}{tag}: {Fore.WHITE}{value}")
                else:
                    print("No EXIF data found.")

            elif path.lower().endswith(".pdf"):
                with open(path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    meta = reader.metadata
                if meta:
                    print(f"\n{Fore.CYAN}PDF Metadata:\n")
                    for key, value in meta.items():
                        print(f"{Fore.GREEN}{key}: {Fore.WHITE}{value}")
                else:
                    print("No metadata found.")

            else:
                print("Unsupported file format.")

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error:", e)

        input("\nPress enter...")

    # -------- DNS LOOKUP --------
    elif x == "8":
        clear()
        flush_input()
        domain = input("Enter domain (ex: google.com): ").strip()
        while not domain:
            domain = input("Enter domain (ex: google.com): ").strip()

        try:
            print(f"\nDNS Lookup for '{domain}'...\n")
            ip = socket.gethostbyname(domain)
            print(f"{Fore.GREEN}IP Address: {Fore.WHITE}{ip}")

            infos = socket.gethostbyname_ex(domain)
            if infos[1]:
                print(f"{Fore.GREEN}Aliases: {Fore.WHITE}{', '.join(infos[1])}")
            if len(infos[2]) > 1:
                print(f"{Fore.GREEN}All IPs: {Fore.WHITE}{', '.join(infos[2])}")

        except socket.gaierror:
            print("Domain not found.")
        except Exception as e:
            print("Error:", e)

        input("\nPress enter...")

    # -------- WHOIS LOOKUP --------
    elif x == "9":
        clear()
        flush_input()
        domain = input("Enter domain (ex: google.com): ").strip()
        while not domain:
            domain = input("Enter domain (ex: google.com): ").strip()

        try:
            print(f"\nWhois lookup for '{domain}'...\n")
            w = whois.whois(domain)

            fields = {
                "Domain": w.domain_name,
                "Registrar": w.registrar,
                "Created": w.creation_date,
                "Expires": w.expiration_date,
                "Updated": w.updated_date,
                "Status": w.status,
                "Emails": w.emails,
                "Name Servers": w.name_servers,
                "Owner": w.name,
                "Country": w.country,
            }

            for key, value in fields.items():
                if value:
                    if isinstance(value, list):
                        value = value[0]
                    print(f"{Fore.GREEN}{key}: {Fore.WHITE}{value}")

        except Exception as e:
            print("Error:", e)

        input("\nPress enter...")

    # -------- PHONE LOOKUP --------
    elif x == "10":
        clear()
        flush_input()
        number = input("Enter phone number (ex: +33612345678): ").strip()
        while not number:
            number = input("Enter phone number (ex: +33612345678): ").strip()

        try:
            parsed = phonenumbers.parse(number)

            if not phonenumbers.is_valid_number(parsed):
                print("Invalid phone number.")
            else:
                print(f"\n{Fore.CYAN}Phone Info:\n")
                print(f"{Fore.GREEN}Valid:        {Fore.WHITE}Yes")
                print(f"{Fore.GREEN}Country:      {Fore.WHITE}{geocoder.description_for_number(parsed, 'en')}")
                print(f"{Fore.GREEN}Carrier:      {Fore.WHITE}{carrier.name_for_number(parsed, 'en') or 'Unknown'}")
                print(f"{Fore.GREEN}Timezones:    {Fore.WHITE}{', '.join(timezone.time_zones_for_number(parsed))}")
                print(f"{Fore.GREEN}Intl format:  {Fore.WHITE}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
                print(f"{Fore.GREEN}Local format: {Fore.WHITE}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)}")

        except phonenumbers.phonenumberutil.NumberParseException:
            print("Invalid format. Use international format ex: +33612345678")
        except Exception as e:
            print("Error:", e)

        input("\nPress enter...")

    # -------- REVERSE IMAGE SEARCH --------
    elif x == "11":
        clear()
        flush_input()
        path = input("Enter image URL or local path: ").strip().strip('"')
        while not path:
            path = input("Enter image URL or local path: ").strip().strip('"')

        try:
            if path.startswith("http"):
                image_url = path
            else:
                print("Uploading image...")
                with open(path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode("utf-8")
                r = requests.post(
                    "https://api.imgbb.com/1/upload",
                    data={"key": "373b4ae480debb56eed6571cc96279ee", "image": encoded}
                )
                image_url = r.json()["data"]["url"]
                print(f"{Fore.GREEN}Uploaded: {Fore.WHITE}{image_url}\n")

            print(f"{Fore.CYAN}Reverse Image Search Links:\n")
            print(f"{Fore.GREEN}Google Lens: {Fore.WHITE}https://lens.google.com/uploadbyurl?url={image_url}")
            print(f"{Fore.GREEN}TinEye:      {Fore.WHITE}https://tineye.com/search?url={image_url}")
            print(f"{Fore.GREEN}Yandex:      {Fore.WHITE}https://yandex.com/images/search?url={image_url}&rpt=imageview")

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error:", e)

        input("\nPress enter...")

    else:
        print("Invalid.")
        input("Press enter...")