import socket
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) 
        result = s.connect_ex((ip, port)) 
        if result == 0:
            print(f"[OPEN] Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error on port {port}: {e}")

if __name__ == "__main__":
    print("Simple Python Port Scanner\n")
    target = input("Enter Target IP or Domain (e.g. 127.0.0.1 ya google.com): ")

    start_port = int(input("Enter starting port numbers (e.g. 1): "))
    end_port = int(input("Enter ending port numbers (e.g. 100): "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("\nScan complete ✅")
