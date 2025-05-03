import asyncio
import socket

async def scan_port(target_ip, port, timeout):
    try:
        conn = asyncio.open_connection(target_ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return port
    except:
        return None

async def detect_open_ports(target, port_range=(1, 1024), timeout=1.0):
    open_ports = []
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        return None

    tasks = [scan_port(target_ip, port, timeout) for port in range(port_range[0], port_range[1] + 1)]
    results = await asyncio.gather(*tasks)

    for port in results:
        if port is not None:
            open_ports.append(port)

    return open_ports
