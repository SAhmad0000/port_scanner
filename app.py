import streamlit as st
import asyncio
from scanner_detection import detect_open_ports

st.title("⚡ Fast Port Scanning Detection Tool (Async)")

st.write("""
Scan a target IP address or domain name to detect open ports very fast using Asyncio.
""")

target = st.text_input("Enter Target (IP or Domain Name)", value="scanme.nmap.org")

col1, col2 = st.columns(2)
with col1:
    start_port = st.number_input("Start Port", min_value=1, max_value=65535, value=20)
with col2:
    end_port = st.number_input("End Port", min_value=1, max_value=65535, value=100)

timeout = st.slider("Timeout (seconds)", min_value=0.1, max_value=5.0, value=1.0)

async def main():
    if target:
        with st.spinner("Scanning in progress..."):
            open_ports = await detect_open_ports(target, (start_port, end_port), timeout)
        
        if open_ports is None:
            st.error("❌ Invalid IP address or domain name. Please check your input.")
        elif open_ports:
            st.success(f"✅ Open Ports Detected: {open_ports}")
            for port in open_ports:
                st.write(f"🔵 Port {port} is open.")
        else:
            st.info("No open ports detected.")
    else:
        st.warning("Please enter a valid target.")

if st.button("Scan Now"):
    asyncio.run(main())
