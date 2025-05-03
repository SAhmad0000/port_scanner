# ⚡ Async Port Scanning Detection Tool

This is a fast and lightweight Port Scanner built with **Python**, **Streamlit**, and **Asyncio**.  
It can scan thousands of ports within seconds using asynchronous socket connections.

## 🚀 Features
- Scan a domain name or IP address easily
- Detect open ports very fast (parallel scanning)
- Set custom port ranges
- Set custom timeout
- User-friendly Streamlit web interface
- Lightweight and easy to deploy

## 🛠 Tech Stack
- Python 3.8+
- Streamlit
- Asyncio

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/port-scanner-async.git
   cd port-scanner-async

   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

    ```

3. Run the Streamlit app:
   ```bash
    streamlit run app.py

    ``` 

## ✨ Usage
- Enter a target domain (example: scanme.nmap.org) or an IP address.
- Select start port and end port (example: 20 to 100).
- Set the timeout (lower = faster).
- Click Scan Now to detect open ports.

## ⚠️ Disclaimer
This tool is for educational purposes and authorized testing only.

Unauthorized scanning of networks that you do not own or have permission to test is illegal.
